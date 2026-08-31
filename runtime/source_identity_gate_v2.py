#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from urllib.parse import urlparse

ALLOWED_METHODS={"SEARCH_RESULT_OBSERVED","OPENED_EXACT_DOCUMENT","CANONICAL_REDIRECT_CONFIRMED","OFFICIAL_DOCUMENT_LISTING"}
DOMAIN_RULES={
 "reuters":("reuters.com",),
 "u.s. energy information administration":("eia.gov",),
 "eia":("eia.gov",),
 "enbridge":("enbridge.com",),
}

def records_of(obj):
    if isinstance(obj.get("records"),list): return obj["records"]
    if isinstance(obj.get("sources"),list): return obj["sources"]
    return []

def rid(r): return r.get("id") or r.get("evidence_id") or r.get("source_id") or "UNKNOWN"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--evidence",required=True); ap.add_argument("--json-output",default="")
    a=ap.parse_args(); obj=json.loads(Path(a.evidence).read_text("utf-8"))
    issues=[]; checks=[]; ext=0
    for r in records_of(obj):
        url=r.get("url"); support=str(r.get("support") or "")
        if not url:
            ok=support=="METHOD_RESULT" and r.get("url_identity_status")=="METHOD_RESULT_NO_URL"
            checks.append({"record":rid(r),"check":"method_null_url","status":"PASS" if ok else "FAIL"})
            if not ok: issues.append(f"{rid(r)}:NULL_URL_WITHOUT_METHOD_RESULT")
            continue
        ext+=1; rec=rid(r)
        receipt=r.get("source_identity_receipt") or {}
        method=receipt.get("verification_method")
        observed_url=receipt.get("observed_url")
        observed_title=receipt.get("observed_title")
        observed_publisher=receipt.get("observed_publisher")
        verified_at=receipt.get("verified_at")
        title_match=receipt.get("title_match_status")
        canonical=receipt.get("canonical_url") or observed_url

        required=bool(method in ALLOWED_METHODS and observed_url and observed_title and observed_publisher and verified_at and title_match in {"EXACT","SAME_DOCUMENT_UPDATED_TITLE"})
        checks.append({"record":rec,"check":"acquisition_receipt_complete","status":"PASS" if required else "FAIL"})
        if not required: issues.append(f"{rec}:SOURCE_ACQUISITION_RECEIPT_INCOMPLETE")

        ok=(canonical==url)
        checks.append({"record":rec,"check":"receipt_canonical_equals_evidence_url","status":"PASS" if ok else "FAIL"})
        if not ok: issues.append(f"{rec}:RECEIPT_URL_MISMATCH")

        pub=str(r.get("publisher","")).strip().lower(); op=str(observed_publisher or "").strip().lower()
        ok=bool(pub and op and (pub==op or pub in op or op in pub))
        checks.append({"record":rec,"check":"receipt_publisher_match","status":"PASS" if ok else "FAIL"})
        if not ok: issues.append(f"{rec}:RECEIPT_PUBLISHER_MISMATCH")

        p=urlparse(url); ok=p.scheme=="https" and bool(p.netloc)
        if not ok: issues.append(f"{rec}:INVALID_EXTERNAL_URL")
        for key,domains in DOMAIN_RULES.items():
            if key in pub:
                host=p.netloc.lower(); ok=any(host==d or host.endswith("."+d) for d in domains)
                checks.append({"record":rec,"check":"publisher_domain","status":"PASS" if ok else "FAIL","detail":host})
                if not ok: issues.append(f"{rec}:PUBLISHER_DOMAIN_MISMATCH")
                break

    summary=obj.get("source_identity_summary") or {}
    if summary.get("guessed_url_count",obj.get("guessed_url_count",0)) not in (0,None):
        issues.append("GUESSED_URL_COUNT_NONZERO")
    if summary.get("unverified_external_source_count",obj.get("unverified_external_source_count",0)) not in (0,None):
        issues.append("UNVERIFIED_EXTERNAL_SOURCE_COUNT_NONZERO")

    out={"schema_version":"SOURCE_IDENTITY_GATE_V2","status":"PASS" if not issues else "FAIL_SOURCE_IDENTITY_GATE_V2","external_records":ext,"checks":checks,"issues":issues}
    if a.json_output: Path(a.json_output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    raise SystemExit(0 if not issues else 1)

if __name__=="__main__": main()
