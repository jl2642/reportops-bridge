# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.5

Status: `R3.1_DAILY_V4_PUBLIC_CORE_CURRENT_SINGLE_SITE`
Timezone: Asia/Shanghai

## Scheduled Chat

10:15 first persists its heartbeat, then pins the unique formal Library Authority version and immutable file_id, hashes the ZIP, and reads internal CURRENT_POINTER.json. CURRENT_PUBLIC and status/latest are only mirrors. The current policy/template/evidence gates apply to candidate production.

The DAILY_TEMPLATE_PUBLIC machine skeleton is normative. Numerical Daily depth thresholds must be loaded from DAILY_PUBLIC_DEPTH_POLICY_V4.json; duplicated governing threshold numbers in the task prompt are prohibited.

## Correction backlog

Prioritize target-day production. Register historical unpromoted candidates/corrections for the Consumer without blocking target-day acquisition. Depth/content correction reuses accepted Evidence with no new research unless the receipt explicitly requires research review.

## 10:15 order

target D fixed-window research → source identity verification → expert signal ranking → exact-template Chinese V4 public core → inline citation gate → deterministic depth measurement from DAILY_PUBLIC_DEPTH_POLICY_V4.json → structure/window/privacy/evidence checks → write/readback public_core → evidence → strict v2 ledger → manifest → status/latest.

`PUBLIC_CORE_ACCEPTED` is forbidden unless all blocking gates pass and actual deterministic metrics are present.

## Work consumer

12:30 Work does not re-research or rewrite accepted Daily public cores.

Before any mutation it:
1. resolves and pins one formal Library Authority version/immutable file_id, hashes that ZIP, reads its internal Pointer/Reader/Lineage/13 views, and computes the public Daily-depth policy subset;
2. verifies its hash against GitHub DAILY_PUBLIC_DEPTH_POLICY_V4.json;
3. checks only pending eligible targets and dependencies in order, inheriting valid unchanged native receipts.

Policy mirror mismatch is `RUNTIME_CONTRACT_VERSION_DRIFT` / `WORK_DETERMINISTIC_REPAIR`; Work repairs the mirror from Authority and reruns the affected deterministic checks. Correction receipts must derive `required_floor` from the verified policy, never from hand-written constants.

After each successful Daily promotion, Work must reconcile the corresponding GitHub per-product manifest to the final Canonical state and measured actuals. Historical producer failure may remain in explicit provenance fields, but the manifest top-level current state must not contradict Canonical promotion/publication.

Higher-cycle products are consumed only from Chat-accepted Library candidates produced under `HIGHER_CYCLE_CHAT_PRODUCER_CONTRACT_V1`.

## Single-site publication

Current live topology is `SINGLE_SITE_V4_PUBLIC`.
- sole live Site: `https://energy-cycle-report-share.ljjx2020.chatgpt.site`
- Private Site: `RETIRED_FROM_LIVE_OPERATION`

After successful Canonical promotion, Work performs public distribution build → deployment → cache-busted real live-origin readback → Download SHA/ZIP integrity → current-derived freshness → GitHub runtime sync.

Site failure never rolls back an accepted Canonical product; report `PACKAGE_SUCCESS_SITE_PENDING`.

## Runtime sync hard invariant

Before Work may report runtime/freshness overall PASS, it must read back and cross-check status/latest.json, runtime/CURRENT_PUBLIC.json and runtime/DEPLOYMENT_STATE.json against Library Current and Authority package identity.

## Idempotency

Formally promoted unchanged products are SKIP. Explicit correction receipts authorize only their bounded defect class.

## R3 single-Authority commit and read boundary
The same formal Authority file conditional replacement with expected_current_version is the sole commit point, only when the pinned Master Contract enables R3_SINGLE_AUTHORITY_CAS_ACTIVE. Pin one immutable version for all Current, Reader, Lineage, 13-view and dependency reads. External Pointer, sidecar and GitHub state are repairable mirrors. No independent mirror priority or GitHub fallback is permitted. Re-resolve before any commit or Site publication. Confirm the exact committed version and SHA before mirror repair, guard each mirror version, stop old repairs if Authority advances, and reject mismatched mirrors at read time. An unknown write outcome requires readback before retry. A later lawful promotion forbids stale rollback. Site publishing is independent and uses only the latest committed Authority snapshot.
