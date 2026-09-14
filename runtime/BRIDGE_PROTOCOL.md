# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.5

Status: `R3.1_DAILY_V4_PUBLIC_CORE_CURRENT_SINGLE_SITE`
Timezone: Asia/Shanghai

## Scheduled Chat

10:15 reads SECURITY_BOUNDARY → CURRENT_PUBLIC → topology → this protocol → DAILY_RUNTIME_CONTRACT_PUBLIC v1.5 → EVIDENCE_POLICY_PUBLIC v1.2 → DAILY_TEMPLATE_PUBLIC → status/latest → recent manifests/correction receipts.

The DAILY_TEMPLATE_PUBLIC machine skeleton is normative for every new Daily candidate. Required `<!-- MODULE:... -->` markers, `<!-- KEY_SIGNAL_CARDS:3-5 -->`, signal-card heading syntax (`### 信号卡N` or `### Signal Card N`) and `<!-- NEXT_VERIFICATION -->` must be preserved exactly. Semantic similarity of headings is not a substitute for machine identity.

## Correction backlog

Before new-day research, check:
1. newer unpromoted Daily candidates;
2. same-date source-identity correction receipts;
3. same-date inline-citation correction receipts;
4. same-date structure/privacy compatibility corrections.

Depth/content correction reuses accepted Evidence with no new research. Source-identity correction allows narrow identity verification. Inline-citation correction is markup-only. Structure compatibility correction may only restore required machine markers/headings and public-safe wording without changing Evidence universe or claim semantics.

## 10:15 order

correction backlog → target D fixed-window research → source identity verification + acquisition receipt → Source Identity v2 gate → expert signal ranking → Chinese V4 public core using exact DAILY_TEMPLATE_PUBLIC skeleton → inline citation gate → exact V4 structure/depth/window/privacy/evidence checks → write/readback public_core → evidence → manifest → status/latest.

`PUBLIC_CORE_ACCEPTED` is forbidden unless:
- Source Identity v2 PASS / guessed_url_count=0;
- inline citation PASS;
- expert signal priority PASS;
- exact V4 machine structure PASS;
- V4 depth PASS;
- privacy forbidden-token scan PASS;
- Evidence/window/write/readback PASS;
- unsupported CORE claims=0.

Public Daily text must not contain JOVO/九丰 or other specific-company non-public operating material, including negative-form disclaimer mentions. Use generic public-safe wording instead.

## Work consumer

12:30 Work does not re-research or rewrite accepted Daily public cores.

Before any mutation it performs a **read-only non-short-circuit preflight** across the full pending Daily queue and all dependent Chat-accepted higher-cycle candidates. It must return one blocker matrix rather than stopping discovery at the oldest product's first failure.

If preflight contains a Chat-side body/Evidence/claim blocker, Canonical mutation and publication remain fail-closed. If preflight passes, Work promotes dependency-aware oldest-first, atomically per product, with durable checkpoints.

Work reruns Source Identity, Inline Citation, exact V4 Product/Depth, privacy, Reader, Lineage, state/identity and freshness gates against the final Canonical/Reader surfaces.

## Single-site publication

Current live topology is `SINGLE_SITE_V4_PUBLIC`.

- sole live Site: `https://energy-cycle-report-share.ljjx2020.chatgpt.site`
- Private Site: `RETIRED_FROM_LIVE_OPERATION`
- no private-layer authoring or private-site publication/readback is part of normal success.

After successful Canonical promotion, Work performs one public distribution build → public deployment → cache-busted real live-origin readback → Download SHA/ZIP integrity → current-derived freshness → GitHub runtime sync.

Site failure never rolls back an accepted Canonical product; report `PACKAGE_SUCCESS_SITE_PENDING`.

## Work rejection feedback

If Work rejects a bridge Daily, keep Canonical/Site fail-closed and report the complete preflight blocker matrix and exact correction class. Do not require one-layer-at-a-time Work debugging.

## Same-date correction

Current-date source, citation, structure or public-safe wording corrections may be republished without changing Current date when bounded to their defect class. Evidence or claim semantics may change only when the correction receipt explicitly requires it.

## Idempotency

Formally promoted unchanged products are SKIP. Explicit correction receipts authorize only their bounded defect class.
