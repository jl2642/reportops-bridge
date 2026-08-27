# ReportOps Scheduled Chat ↔ GitHub Bridge Protocol v1.1

Status: R3.1 CURRENT_NORMATIVE
Timezone: Asia/Shanghai

## Scheduled Chat execution mode

ReportOps uses one Scheduled Chat execution point:

- `10:15` = `DAILY_CONTINUITY_CONTROLLER_AND_PUBLIC_CORE_PRODUCER`

There is no ReportOps evening execution point.

## Read order for Scheduled Chat

1. `SECURITY_BOUNDARY.md`
2. `runtime/CURRENT_PUBLIC.json`
3. `runtime/AUTOMATION_TOPOLOGY_R3_1.json`
4. `runtime/BRIDGE_PROTOCOL.md`
5. `runtime/DAILY_RUNTIME_CONTRACT_PUBLIC.md`
6. `runtime/EVIDENCE_POLICY_PUBLIC.md`
7. `runtime/DAILY_TEMPLATE_PUBLIC.md`
8. `runtime/RECENT_PUBLIC_CONTEXT.json` if present
9. recent accepted files under `daily/YYYY/MM/` when needed for continuity

GitHub is a public-safe cross-task bridge, not Canonical Authority.

## 10:15 write order

For target date D:

1. keep fixed window `[D-1 10:00,D 10:00) Asia/Shanghai`;
2. produce current-day public-safe Daily core first;
3. build structured evidence and run fixed-window/evidence/privacy checks;
4. write and read back, in order:
   - `daily/YYYY/MM/YYYY-MM-DD/public_core.md`
   - `daily/YYYY/MM/YYYY-MM-DD/evidence.json`
   - `daily/YYYY/MM/YYYY-MM-DD/manifest.json`
5. only after all three pass, update and read back `status/latest.json`;
6. then scan continuity and recover at most two oldest historical missing public-safe dates with provenance `DELAYED_RECOVERY`.

`production_status=PUBLIC_CORE_ACCEPTED` is allowed only after required evidence, window, privacy, GitHub write and readback checks pass.

Historical recovery must never block current-day persistence.

## Work consumer contract

The 12:30 Scheduled Work consumer:

1. reads the latest unique Library Authority first;
2. scans DAILY / WEEKLY / MONTHLY / QUARTERLY / ANNUAL for already completed and accepted products;
3. consumes GitHub Daily core/evidence/manifest only as public-safe Daily input;
4. performs private reconciliation and blocking Product/Evidence/Reader/Lineage/state gates;
5. atomically promotes eligible products;
6. publishes at most one batch after reconciliation:
   Private → authenticated Private readback → Public → Public readback → Download Center → remote download SHA/ZIP integrity.

Work must not perform default public-web Daily research or author Weekly/Monthly/Quarterly/Annual.

A missing/failed Daily bridge output remains fail-closed for that date but must not prevent Work from processing other already accepted higher-cycle products or existing site-pending publication.

## Idempotency

- Before creating a target-date file, check whether an accepted output already exists.
- Do not regenerate an accepted same-date Daily unless a real correction is required.
- Completed Canonical promotion or remotely verified publication stages must be skipped on resume.
- One failed stage does not roll back earlier accepted Canonical state.

## Fail-closed rules

Do not write `SUCCESS` or `PUBLIC_CORE_ACCEPTED` when:

- GitHub write/readback did not actually succeed;
- privacy screen fails;
- fixed-window compliance cannot be established;
- required evidence is materially incomplete;
- the task needs private/internal context unavailable to Scheduled Chat.

Use `PRIVATE_LAYER_REQUIRED` for private-only content.

## Authority boundary

Scheduled Chat may write only public-safe bridge artifacts. It may not mutate Library Current, Canonical Authority, Private Site, Public Site or Download Center.
