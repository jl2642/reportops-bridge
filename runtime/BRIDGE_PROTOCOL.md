# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1

Status: R3 AUTOMATION_REWIRED

## Scheduled Chat execution modes

The same Scheduled Chat automation runs twice daily in Asia/Shanghai:

- `10:15` = `PRIMARY_DAILY_PUBLIC_CORE_PRODUCTION`
- `19:15` = `EVENING_PUBLIC_HEALTH_AND_EVIDENCE_INSURANCE`

This keeps the active-task count unchanged while preserving both primary production and same-day fallback insurance.

## Read order for Scheduled Chat

1. `SECURITY_BOUNDARY.md`
2. `runtime/CURRENT_PUBLIC.json`
3. `runtime/DAILY_RUNTIME_CONTRACT_PUBLIC.md`
4. `runtime/EVIDENCE_POLICY_PUBLIC.md`
5. `runtime/DAILY_TEMPLATE_PUBLIC.md`
6. `runtime/RECENT_PUBLIC_CONTEXT.json` if present
7. recent files under `daily/YYYY/MM/` and/or `fallback/YYYY/MM/` only when needed for public-context continuity

GitHub content never overrides a newer Library Canonical state during reconciliation.

## 10:15 primary write order

For target date D:

1. research fixed window `[D-1 10:00, D 10:00) Asia/Shanghai`;
2. build the public-safe Daily core and structured evidence;
3. run fixed-window, evidence and privacy checks;
4. write:
   - `daily/YYYY/MM/YYYY-MM-DD/public_core.md`
   - `daily/YYYY/MM/YYYY-MM-DD/evidence.json`
   - `daily/YYYY/MM/YYYY-MM-DD/manifest.json`
5. only after all writes succeed, update `status/latest.json`.

`production_status=PUBLIC_CORE_ACCEPTED` is allowed only when the required public evidence and privacy gates pass.

## 19:15 insurance mode

1. check the Public Site and the target-date GitHub Daily manifest;
2. if the formal Daily is publicly verified, do nothing except record verification;
3. if an accepted 10:15 GitHub Daily core exists but Work publication is pending, do not duplicate research;
4. only when no accepted Daily core/formal Daily exists, create `fallback/YYYY/MM/YYYY-MM-DD.json` using the fallback schema and update `status/latest.json` after a successful write.

Historical gaps are never silently backfilled by this automation.

## Work consumer contract

The formal Scheduled Work consumer runs after the 10:15 producer. It must:

1. read the latest unique Library Authority first;
2. read the target-date GitHub Daily manifest/core/evidence;
3. revalidate URLs, time ownership, evidence semantics and privacy boundary;
4. add any private-only layer only inside the private Authority environment;
5. run formal Product/Evidence/Lineage/Reader gates;
6. promote only in sequence;
7. publish Private → authenticated readback → Public → readback → Download.

Work must not repeat public-web Daily research merely because the bridge is unavailable. Missing/failed bridge output is fail-closed and remains recoverable through the evening fallback or explicit recovery.

## Idempotency

- One target date has one active R1 path unless an explicit revision suffix is required.
- Before creating a file, check whether the target path already exists.
- If an existing successful packet/output has the same target date and window, do not create a duplicate; update only when a real correction is required.
- `capture_id` / `output_id` must remain stable across retries of the same logical version.

## Fail-closed rules

Do not write `SUCCESS` or `PUBLIC_CORE_ACCEPTED` when:

- GitHub write did not actually succeed;
- privacy screen fails;
- fixed-window compliance cannot be established;
- required evidence fields are materially incomplete;
- the task needs private/internal context unavailable in this public bridge.

Use `PRIVATE_LAYER_REQUIRED` for private-only content, not a fabricated substitute.

## Authority boundary

Scheduled Chat may write bridge artifacts but may not claim to mutate Library Current, Canonical Authority, Private Site, Public Site or Download Center. GitHub remains a public-safe runtime bridge, not Canonical Authority.