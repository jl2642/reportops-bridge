#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from html.parser import HTMLParser
from pathlib import Path

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https://[^)]+)\)")
EVIDENCE_LABEL_RE = re.compile(r"(E\d+)$", re.I)

def records_of(obj):
    if isinstance(obj.get("records"), list):
        return obj["records"]
    if isinstance(obj.get("sources"), list):
        return obj["sources"]
    return []

def evidence_label(r):
    raw = str(r.get("id") or r.get("evidence_id") or r.get("source_id") or "")
    m = EVIDENCE_LABEL_RE.search(raw)
    return m.group(1).upper() if m else raw

class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack=[]
        self.anchors=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="a":
            d=dict(attrs)
            self.stack.append({"href":d.get("href",""),"text":""})
        elif self.stack:
            self.stack.append(None)
    def handle_data(self, data):
        for item in self.stack:
            if isinstance(item,dict):
                item["text"] += data
    def handle_endtag(self, tag):
        if tag.lower()=="a":
            for i in range(len(self.stack)-1,-1,-1):
                item=self.stack[i]
                if isinstance(item,dict):
                    self.anchors.append(item)
                    self.stack=self.stack[:i]
                    break

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--markdown", required=True)
    ap.add_argument("--html", action="append", default=[])
    ap.add_argument("--json-output", default="")
    a=ap.parse_args()

    evidence=json.loads(Path(a.evidence).read_text("utf-8"))
    md=Path(a.markdown).read_text("utf-8")
    # A bottom source appendix alone cannot satisfy inline citation coverage.
    narrative=re.split(r"(?im)^##\s+(?:Public\s+Sources|Sources|来源|公共来源)\b", md, maxsplit=1)[0]
    md_links=MD_LINK_RE.findall(narrative)
    md_pairs={(t.strip().upper(),u.strip()) for t,u in md_links}

    checks=[]; issues=[]; external=[]
    for r in records_of(evidence):
        url=r.get("url")
        if not url:
            continue
        label=evidence_label(r)
        external.append((label,url))
        ok=(label.upper(),url) in md_pairs
        checks.append({"record":label,"check":"inline_markdown_exact_href","status":"PASS" if ok else "FAIL","url":url})
        if not ok:
            issues.append(f"{label}:MISSING_INLINE_CLICKABLE_CITATION")

    # At least one clickable source must exist inside each signal-card section.
    card_sections=re.split(r"(?im)^###\s+(?=信号卡|Signal Card)", narrative)
    if len(card_sections)>1:
        for idx,section in enumerate(card_sections[1:],1):
            ok=bool(MD_LINK_RE.search(section))
            checks.append({"record":f"SIGNAL_CARD_{idx}","check":"card_has_inline_clickable_source","status":"PASS" if ok else "FAIL"})
            if not ok:
                issues.append(f"SIGNAL_CARD_{idx}:NO_INLINE_CLICKABLE_SOURCE")

    html_results=[]
    for hp in a.html:
        parser=AnchorParser()
        parser.feed(Path(hp).read_text("utf-8",errors="replace"))
        pairs={(x["text"].strip().upper(),x["href"]) for x in parser.anchors}
        missing=[]
        for label,url in external:
            if (label.upper(),url) not in pairs:
                missing.append({"label":label,"url":url})
        html_results.append({"html":hp,"status":"PASS" if not missing else "FAIL","missing":missing})
        for m in missing:
            issues.append(f"{Path(hp).name}:{m['label']}:INLINE_HTML_HREF_MISSING")

    out={
        "status":"PASS" if not issues else "FAIL_INLINE_CITATION_GATE_V1",
        "evidence":a.evidence,
        "markdown":a.markdown,
        "external_evidence_records":len(external),
        "inline_markdown_links":len(md_links),
        "checks":checks,
        "html_results":html_results,
        "issues":issues
    }
    if a.json_output:
        Path(a.json_output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    raise SystemExit(0 if not issues else 1)

if __name__=="__main__":
    main()
