# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.5

Status: `R3.1_DAILY_V4_PUBLIC_CORE_CURRENT`
Timezone: Asia/Shanghai

## Scheduled Chat

10:15 reads SECURITY_BOUNDARY → CURRENT_PUBLIC → topology → this protocol → DAILY_RUNTIME_CONTRACT_PUBLIC v1.5 → EVIDENCE_POLICY_PUBLIC v1.1 → DAILY_TEMPLATE_PUBLIC → status/latest → recent manifests/correction receipts.

## Correction backlog

Before new-day research, check:
1. newer unpromoted Daily candidates;
2. same-date source-identity correction receipts;
3. same-date inline-citation correction receipts.

Depth/content correction reuses accepted Evidence with no new research. Source-identity correction allows narrow identity verification. Inline-citation correction is markup-only: do not change claim semantics; inject exact clickable Evidence links adjacent to the facts they support.

## 10:15 order

correction backlog → target D fixed-window research → source identity verification + acquisition receipt → Source Identity v2 gate → expert signal ranking → Chinese V4 public core with inline clickable Evidence links → inline citation gate → exact V4 depth/window/privacy/evidence checks → write/readback public_core → evidence → manifest → status/latest.

`PUBLIC_CORE_ACCEPTED` requires:
- Source Identity v2 PASS / guessed_url_count=0;
- inline citation PASS;
- expert signal priority PASS;
- V4 depth PASS;
- Evidence/window/privacy/write/readback PASS;
- unsupported CORE claims=0.

## Work consumer

12:30 Work does not re-research. It:
- verifies source identity metadata and acquisition receipts;
- runs `source_identity_gate_v1.py`;
- runs `inline_citation_gate_v1.py` on accepted Markdown and final Private/Public Reader HTML;
- requires every narrative Evidence anchor to retain the exact accepted canonical href;
- does not accept “all URLs appear only in a Sources appendix” as citation coverage;
- adds separate private JOVO layer;
- runs Product/Evidence/Reader/Lineage/state/freshness gates;
- publishes Private → authenticated readback → Public → remote readback → Download SHA/ZIP.

## Work rejection feedback

If Work rejects a bridge Daily, keep Canonical/Sites fail-closed and write public-safe failed checks and correction need back to GitHub.

## Same-date correction

Current-date source or inline-citation corrections may be republished without changing Current date. Allowed changes are limited to corrected Evidence URLs, Evidence labels/hrefs, source tables and markup-only inline citations unless the correction receipt explicitly states claim semantics must change.

## Idempotency

Formally promoted unchanged products are SKIP. Explicit correction receipts authorize only their bounded defect class.
