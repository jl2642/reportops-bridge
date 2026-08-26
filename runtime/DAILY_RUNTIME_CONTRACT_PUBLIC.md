# ReportOps Daily Public Runtime Contract v1.1

Status: `R3_1_TWO_TASK_DAILY_CONTINUITY_ARCHITECTURE`

## Product role

Daily answers: **what new, verifiable energy-market signals appeared in the fixed reporting window?**

Role: `SIGNAL_RADAR`.

## R3.1 automation role

At `10:15 Asia/Shanghai`, Scheduled Chat is the single Daily continuity controller and primary producer of the public-safe Daily core.

Priority order is mandatory:

1. **Secure target day D first.** Check whether an accepted D manifest already exists. If not, research the fixed D window, persist Evidence, then write `public_core.md` → `evidence.json` → `manifest.json` and read them back.
2. **Scan continuity.** Starting from the last publicly verified Daily pointer plus already accepted GitHub Daily manifests, identify missing/failed dates through D.
3. **Limited recovery.** Only after D is secured, recover at most the two oldest historical gaps in one run. Each historical reconstruction keeps its original fixed window and is labeled `DELAYED_RECOVERY`; it must never be represented as an original same-day Scheduled Chat capture.

There is **no permanent 19:00/19:15 ReportOps insurance run** after R3.1. GitHub persistence itself is the cross-task durability bridge. A missed day is detected and recovered by a later 10:15 continuity scan.

At `12:30 Asia/Shanghai`, Scheduled Work is downstream. It reads the latest Library Authority and GitHub Daily bridge, performs formal reconciliation/private-only layers/gates/Lineage/Canonical Promotion, scans ready-to-publish Daily/Weekly/Monthly/Quarterly/Annual products, and performs one batch publication. Work is not the default public-web Daily research producer and does not author higher-cycle reports.

## Fixed window

For target date D in Asia/Shanghai:

`[D-1 10:00, D 10:00)`

A delayed run or delayed recovery must not shift this window.

## Required analytical coverage

1. Executive Signal Summary
2. Market & Event Delta
3. Price & Spread Delta
4. China Chain Delta
5. Global Energy Delta
6. Research Trigger Board (public-safe labels only)
7. Industry Chain & Operator Exposure (generic/public-safe; no JOVO-specific internal analysis)
8. Evidence, Gaps & Falsifiers
9. Next Verification

## Depth rule

A Daily must explain causality and transmission, not merely list headlines. Key signals should state:

- fact summary;
- why it matters;
- price/supply-demand/value-chain transmission;
- affected sectors/operators;
- evidence boundary;
- next verification;
- falsifier or condition that would weaken the signal.

Weekend/holiday mode must use: prior-week signal review + next-week risk path + data gaps + next-open verification. Do not invent stale prices.

## Claim discipline

Strong claims require strong primary/professional evidence and explicit reasoning. Otherwise downgrade to `WATCH`, `NEEDS_CONFIRMATION`, `DATA_GAP` or `PROXY_USED`.

## Public-safe boundary

The GitHub output may contain only public-market research and generic sector/operator implications. Any JOVO/九丰-specific operating, contract, margin, capital-allocation or opportunity judgment is `PRIVATE_LAYER_REQUIRED` and must not be written to this repository.

## Output status

Scheduled Chat outputs are formal **bridge production inputs** but are not Canonical Authority. `PUBLIC_CORE_ACCEPTED` means the public-safe research/evidence package passed the bridge gates; it does not mean Library Current was promoted or Sites were published.

`MISSING_DAILY != ORIGINAL_CAPTURE_GAP` and `BRIDGE_NOT_VISIBLE != NO_CHAT_DATA`.

GitHub never promotes Library Current or publishes Sites.