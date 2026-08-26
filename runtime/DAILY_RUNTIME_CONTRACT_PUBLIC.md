# ReportOps Daily Public Runtime Contract v1

Status: R2 PRE-CUTOVER

## Product role

Daily answers: **what new, verifiable energy-market signals appeared in the fixed reporting window?**

Role: `SIGNAL_RADAR`.

## Fixed window

For target date D in Asia/Shanghai:

`[D-1 10:00, D 10:00)`

A delayed run must not shift this window.

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

Before R3 cutover, Scheduled Chat output is a bridge candidate, not Canonical Authority. GitHub never promotes Library Current or publishes Sites.
