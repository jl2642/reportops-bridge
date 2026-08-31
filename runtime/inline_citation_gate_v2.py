#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from html.parser import HTMLParser
from pathlib import Path

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https://[^)]+)\)")
SOURCE_MARKER_RE = re.compile(r"\[(Source:\s*(S\d+)|E\d+)\](?!\()", re.I)

def records_of(obj):
    if isinstance(obj.get("records"), list):
        return obj["records"]
    if isinstance(obj.get("sources"), list):
        return obj["sources"]
    return []

def label_of(r):
    raw=str(r.get("id") or r.get("evidence_id") or r.get("source_id") or "")
    m=re.search(r"(S\d+|E\d+)$", raw, re.I)
    return m.group(1).upper() if m else raw.upper()

class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_article=False; self.depth=0
        self.hrefs=[]; self.text=[]; self.cards=[]; self.current_card=None
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag.lower()=="article" and "ei-article" in d.get("class",""):
            self.in_article=True; self.depth=1; return
        if self.in_article:
            if tag.lower()=="article": self.depth+=1
            if tag.lower()=="a" and d.get("href"):
                self.hrefs.append(d["href"])
                if self.current_card is not None: self.current_card["hrefs"].append(d["href"])
            if tag.lower()=="h3":
                self.current_card={"text":"","hrefs":[]}; self.cards.append(self.current_card)
    def handle_data(self,data):
        if self.in_article:
            self.text.append(data)
            if self.current_card is not None: self.current_card["text"]+=data
    def handle_endtag(self,tag):
        if self.in_article and tag.lower()=="article":
            self.depth-=1
            if self.depth<=0: self.in_article=False
        if self.in_article and tag.lower()=="h3":
            pass

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--evidence",required=True)
    ap.add_argument("--markdown",required=True)
    ap.add_argument("--html",action="append",default=[])
    ap.add_argument("--json-output",default="")
    a=ap.parse_args()

    obj=json.loads(Path(a.evidence).read_text("utf-8"))
    ext=[r for r in records_of(obj) if r.get("url")]
    unique_urls=sorted(set(r["url"] for r in ext))
    external_labels={label_of(r) for r in ext}

    md=Path(a.markdown).read_text("utf-8")
    narrative=re.split(r"(?im)^##\s+(?:Public\s+Sources|Sources|来源|公共来源)\b",md,maxsplit=1)[0]
    md_links=MD_LINK_RE.findall(narrative)
    narrative_urls={u for _,u in md_links}
    issues=[]; checks=[]

    for url in unique_urls:
        ok=url in narrative_urls
        checks.append({"check":"unique_source_url_inline_narrative","url":url,"status":"PASS" if ok else "FAIL"})
        if not ok: issues.append("SOURCE_URL_NOT_INLINE_IN_NARRATIVE:"+url)

    plain=[]
    for m in SOURCE_MARKER_RE.finditer(narrative):
        token=(m.group(2) or m.group(1) or "").upper().replace("SOURCE:","").strip()
        if token in external_labels:
            plain.append(m.group(0))
    if plain:
        issues.append("PLAIN_UNLINKED_EXTERNAL_MARKERS:"+",".join(sorted(set(plain))))
    checks.append({"check":"no_plain_external_markers","status":"PASS" if not plain else "FAIL","count":len(plain)})

    cards=re.split(r"(?im)^###\s+(?=信号卡|Signal Card)",narrative)[1:]
    for i,card in enumerate(cards,1):
        ok=bool(MD_LINK_RE.search(card))
        checks.append({"check":"signal_card_has_inline_clickable_source","card":i,"status":"PASS" if ok else "FAIL"})
        if not ok: issues.append(f"SIGNAL_CARD_{i}:NO_INLINE_CLICKABLE_SOURCE")

    html_results=[]
    for hp in a.html:
        parser=ArticleParser(); parser.feed(Path(hp).read_text("utf-8",errors="replace"))
        hrefs=set(parser.hrefs)
        missing=[u for u in unique_urls if u not in hrefs]
        text=" ".join(parser.text)
        html_plain=[lab for lab in external_labels if re.search(rf"\b(?:Source:\s*)?{re.escape(lab)}\b",text,re.I)]
        # HTML text may contain label text inside linked anchors; href coverage is authoritative.
        status="PASS" if not missing else "FAIL"
        html_results.append({"html":hp,"status":status,"missing_urls":missing,"article_external_href_count":len([h for h in hrefs if h.startswith("https://")])})
        for u in missing: issues.append(f"{Path(hp).name}:ARTICLE_HREF_MISSING:{u}")

    out={
      "schema_version":"INLINE_CITATION_GATE_V2",
      "status":"PASS" if not issues else "FAIL_INLINE_CITATION_GATE_V2",
      "unique_external_source_urls":len(unique_urls),
      "external_evidence_records":len(ext),
      "inline_markdown_links":len(md_links),
      "checks":checks,"html_results":html_results,"issues":issues
    }
    if a.json_output:
        Path(a.json_output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    raise SystemExit(0 if not issues else 1)

if __name__=="__main__": main()
