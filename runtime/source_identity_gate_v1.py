#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ALLOWED_IDENTITY = {
    "EXACT_SEARCH_RESULT_CONFIRMED",
    "OPENED_EXACT_DOCUMENT",
    "CANONICAL_REDIRECT_CONFIRMED",
}
DOMAIN_RULES = {
    "reuters": ("reuters.com",),
    "u.s. energy information administration": ("eia.gov",),
    "eia": ("eia.gov",),
    "enbridge": ("enbridge.com",),
}

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="a":
            d=dict(attrs)
            if d.get("href"):
                self.hrefs.append(d["href"])

def records_of(obj):
    if isinstance(obj.get("records"), list):
        return obj["records"]
    if isinstance(obj.get("sources"), list):
        return obj["sources"]
    return []

def get_id(r):
    return r.get("id") or r.get("evidence_id") or r.get("source_id") or "UNKNOWN"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--html", action="append", default=[])
    ap.add_argument("--json-output", default="")
    a=ap.parse_args()
    obj=json.loads(Path(a.evidence).read_text("utf-8"))
    issues=[]; checks=[]; urls=[]
    for r in records_of(obj):
        rid=get_id(r); url=r.get("url"); support=str(r.get("support") or r.get("directness") or "")
        ident=r.get("url_identity_status")
        if not url:
            ok=(support=="METHOD_RESULT" and ident=="METHOD_RESULT_NO_URL")
            checks.append({"record":rid,"check":"null_url_method_rule","status":"PASS" if ok else "FAIL"})
            if not ok: issues.append(f"{rid}:NULL_URL_WITHOUT_METHOD_RESULT")
            continue
        urls.append(url)
        ok=ident in ALLOWED_IDENTITY
        checks.append({"record":rid,"check":"identity_stamp","status":"PASS" if ok else "FAIL","detail":str(ident)})
        if not ok: issues.append(f"{rid}:SOURCE_IDENTITY_NOT_VERIFIED")
        p=urlparse(url)
        ok=p.scheme=="https" and bool(p.netloc)
        checks.append({"record":rid,"check":"https_exact_url","status":"PASS" if ok else "FAIL","detail":url})
        if not ok: issues.append(f"{rid}:INVALID_EXTERNAL_URL")
        pub=str(r.get("publisher","")).strip().lower()
        for key,domains in DOMAIN_RULES.items():
            if key in pub:
                host=p.netloc.lower()
                ok=any(host==d or host.endswith("."+d) for d in domains)
                checks.append({"record":rid,"check":"publisher_domain","status":"PASS" if ok else "FAIL","detail":host})
                if not ok: issues.append(f"{rid}:PUBLISHER_DOMAIN_MISMATCH")
                break
    if obj.get("guessed_url_count", obj.get("source_identity_summary",{}).get("guessed_url_count",0)) not in (0,None):
        issues.append("MANIFEST:GUESSED_URL_COUNT_NONZERO")
    if obj.get("unverified_external_source_count", obj.get("source_identity_summary",{}).get("unverified_external_source_count",0)) not in (0,None):
        issues.append("MANIFEST:UNVERIFIED_EXTERNAL_SOURCE_COUNT_NONZERO")
    html_results=[]
    for hp in a.html:
        parser=LinkParser(); parser.feed(Path(hp).read_text("utf-8",errors="replace"))
        hrefs=set(parser.hrefs)
        missing=[u for u in sorted(set(urls)) if u not in hrefs]
        html_results.append({"html":hp,"accepted_urls":len(set(urls)),"missing":missing,"status":"PASS" if not missing else "FAIL"})
        issues += [f"{Path(hp).name}:HREF_NOT_EQUAL:{u}" for u in missing]
    status="PASS" if not issues else "FAIL_SOURCE_IDENTITY_GATE_V1"
    out={"status":status,"evidence":a.evidence,"checks":checks,"html_results":html_results,"issues":issues}
    if a.json_output:
        Path(a.json_output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    raise SystemExit(0 if not issues else 1)

if __name__=="__main__":
    main()
