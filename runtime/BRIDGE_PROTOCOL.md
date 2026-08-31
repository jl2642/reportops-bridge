# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.4

Status: `R3.1_DAILY_V4_PUBLIC_CORE_CURRENT`
Timezone: Asia/Shanghai

## Scheduled Chat

10:15 reads SECURITY_BOUNDARY → CURRENT_PUBLIC → topology → this protocol → DAILY_RUNTIME_CONTRACT_PUBLIC → EVIDENCE_POLICY_PUBLIC → DAILY_TEMPLATE_PUBLIC → status/latest → recent manifests.

## Correction backlog

Before new-day research, check:
1. newer unpromoted Daily candidates;
2. same-date accepted source-identity correction receipts.

Depth/content correction reuses accepted Evidence with no new research. Source-identity correction may perform narrowly scoped source verification and must preserve claim meaning unless the source itself disproves the claim.

## 10:15 order

correction backlog → target D fixed-window research → **source identity verification** → expert signal ranking → Chinese V4 public core → exact V4 depth/window/privacy/evidence checks → write/readback public_core → evidence → manifest → status/latest.

`PUBLIC_CORE_ACCEPTED` requires:
- source identity PASS / guessed_url_count=0;
- expert signal priority PASS;
- V4 depth PASS;
- Evidence/window/privacy/write/readback PASS;
- unsupported CORE claims = 0.

## Work consumer

12:30 Work does not re-research. It:
- verifies required source-identity metadata is present and PASS;
- verifies every rendered public/private source href exactly equals the accepted evidence canonical URL;
- adds separate private JOVO layer;
- runs Product/Evidence/Reader/Lineage/state/freshness gates;
- publishes Private → authenticated readback → Public → remote readback → Download SHA/ZIP.

External publisher reachability remains non-blocking at Work because paywalls/anti-bot are unstable; **this does not waive Chat source-identity verification**.

## Work rejection feedback

If Work rejects a bridge Daily, keep Canonical/Sites fail-closed and write public-safe feedback to GitHub with failed checks, whether new research is required, and pending Chat correction state.

## Same-date source correction

If current Canonical Daily has an accepted Chat source-identity correction receipt, Work may perform a bounded same-date correction transaction:
- do not change report conclusions except where source verification requires;
- replace only corrected evidence/source URLs and corresponding rendered hrefs;
- rerun evidence, Reader, source-href equality, state/freshness gates;
- republish through normal Private → Public → Download order;
- keep Current date unchanged but increment publication versions and record correction provenance.

## Idempotency

Formally promoted unchanged products are SKIP. Explicit correction receipts authorize only the bounded defect class stated.
