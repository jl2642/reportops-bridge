# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1

Status: R2 PRE-CUTOVER

## Read order for Scheduled Chat

1. `SECURITY_BOUNDARY.md`
2. `runtime/CURRENT_PUBLIC.json`
3. `runtime/DAILY_RUNTIME_CONTRACT_PUBLIC.md`
4. `runtime/EVIDENCE_POLICY_PUBLIC.md`
5. `runtime/DAILY_TEMPLATE_PUBLIC.md`
6. `runtime/RECENT_PUBLIC_CONTEXT.json` if present
7. recent files under `daily/YYYY/MM/` and/or `fallback/YYYY/MM/` only when needed for public-context continuity

GitHub content never overrides a newer Library Canonical state during reconciliation.

## Write order

For target date D:

1. research fixed window `[D-1 10:00, D 10:00) Asia/Shanghai`;
2. build structured evidence packet;
3. run privacy screen against `SECURITY_BOUNDARY.md`;
4. write either:
   - `daily/YYYY/MM/YYYY-MM-DD/public_core.md` + `evidence.json` + `manifest.json`, or
   - `fallback/YYYY/MM/YYYY-MM-DD.json` when formal production is not yet enabled/accepted;
5. only after file write succeeds, update `status/latest.json`.

## Idempotency

- One target date has one active R1 path unless an explicit revision suffix is required.
- Before creating a file, check whether the target path already exists.
- If an existing successful packet/output has the same target date and window, do not create a duplicate; update only when a real correction is required.
- `capture_id` / `output_id` must remain stable across retries of the same logical version.

## Fail-closed rules

Do not write `SUCCESS` when:

- GitHub write did not actually succeed;
- privacy screen fails;
- fixed-window compliance cannot be established;
- required evidence fields are materially incomplete;
- the task needs private/internal context unavailable in this public bridge.

Use `PRIVATE_LAYER_REQUIRED` for private-only content, not a fabricated substitute.

## Authority boundary

Scheduled Chat may write bridge artifacts but may not claim to mutate Library Current, Canonical Authority, Private Site, Public Site or Download Center.
