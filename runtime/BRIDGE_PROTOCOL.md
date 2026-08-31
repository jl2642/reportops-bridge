# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.3

Status: `R3.1_DAILY_V4_PUBLIC_CORE_CURRENT`
Timezone: Asia/Shanghai

## Scheduled Chat

10:15 = `DAILY_CONTINUITY_CONTROLLER_AND_PUBLIC_CORE_PRODUCER`; no evening task. Read SECURITY_BOUNDARY → CURRENT_PUBLIC → topology → this protocol → DAILY_RUNTIME_CONTRACT_PUBLIC → EVIDENCE_POLICY_PUBLIC → DAILY_TEMPLATE_PUBLIC → status/latest → recent manifests.

### Correction backlog comes before silent continuity

If `status/latest` or a recent Daily manifest is newer than `CURRENT_PUBLIC.current_daily_public`, Chat must not assume “PUBLIC_CORE_ACCEPTED” means Work-promotable. Re-run the exact deterministic V4 public-depth preflight specified in DAILY_RUNTIME_CONTRACT_PUBLIC.

If it fails, preserve the same fixed window and accepted Evidence, create a bounded `CHAT_DEPTH_CORRECTION` revision with no new research, write/readback public_core + manifest, and only then restore `PUBLIC_CORE_ACCEPTED`. This state is not a historical evidence gap and does not consume the max-two research recovery allowance.

## 10:15 normal write order

Correction backlog preflight/repair → target D fixed-window research → Chinese `DAILY_V4_PUBLIC_CORE` → structured evidence → exact V4 public-depth + window/privacy/evidence checks → write/readback public_core → evidence → manifest → status/latest → optional historical evidence recovery.

`PUBLIC_CORE_ACCEPTED` requires exact public V4 depth PASS, 3–5 cards, Evidence PASS, privacy PASS, window PASS, GitHub write/readback PASS and unsupported CORE claims = 0.

## Work consumer and rejection feedback

12:30 Work reads unique Library Authority and accepted GitHub bridge, reuses public core/evidence without re-research, adds separate private `JOVO_DIRECTIONAL_EXPOSURE`, runs blocking V3+V4 Product/Evidence/Reader/Lineage/state/freshness gates, then atomically promotes and publishes Private → authenticated readback → Public → remote readback → Download SHA/ZIP.

If Work rejects a bridge Daily, it must keep Canonical/Sites fail-closed **and write a public-safe reconciliation result back to GitHub** in that date manifest/status surface: `work_reconciliation_status=REJECTED_NEEDS_CHAT_CORRECTION`, failed check names, `new_research_required=false/true`, and formal status. It must not expose private/JOVO content in feedback.

If Work accepts it, GitHub Current is advanced only after remote publication PASS.

## Idempotency

Accepted and formally promoted same-date products are SKIP. A same-date Work rejection authorizes a corrective revision while preserving original provenance/evidence lineage. GitHub never mutates Library Current or Sites.
