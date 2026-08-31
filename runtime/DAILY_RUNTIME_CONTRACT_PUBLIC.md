# ReportOps Daily Public Runtime Contract v1.3

Status: `R3_1_DAILY_V4_PUBLIC_CORE_ACTIVE`
Editorial contract: `DAILY_V4_PUBLIC_CORE`
Language: `zh-CN` (source titles/identifiers may remain original language)

## Product role

Daily answers: **固定窗口内出现了哪些新的、可验证的能源市场信号，它们通过什么机制影响价格、供需、物流和产业链？** Role: `SIGNAL_RADAR`.

## Runtime role

10:15 Asia/Shanghai Scheduled Chat is the Daily continuity/editorial controller. 12:30 Work is the downstream formal reconciler/publisher and must not redo public-web research or rewrite an Accepted public core.

Before new-day production, Chat compares `runtime/CURRENT_PUBLIC.json` with `status/latest.json` and recent Daily manifests. If a newer bridge Daily exists but has not advanced Canonical Current, Chat must perform an exact V4 public-depth preflight on that candidate. A failed/unpromoted candidate is a **correction backlog**, not a missing-evidence day: reuse its accepted Evidence, make a bounded content-only revision, then re-accept it before/alongside D. Never re-research merely to repair depth.

## Fixed window

`[D-1 10:00, D 10:00) Asia/Shanghai`. Delays never move the window.

## V4 public-core composition

Use exact semantic markers:

1. `MODULE:EXECUTIVE_SIGNAL_SUMMARY`
2. `KEY_SIGNAL_CARDS:3-5` plus heading containing `今日关键信号` and 3–5 `### 信号卡...`
3. `MODULE:MARKET_AND_EVENT_DELTA`
4. `MODULE:PRICE_AND_SPREAD_DELTA`
5. `MODULE:CHINA_CHAIN_DELTA`
6. `MODULE:GLOBAL_ENERGY_DELTA`
7. `MODULE:RESEARCH_TRIGGER_BOARD`
8. `MODULE:INDUSTRY_CHAIN_AND_OPERATOR_EXPOSURE`
9. `MODULE:EVIDENCE_AND_GAPS`
10. `NEXT_VERIFICATION`
11. conditional Proxy Matrix when material `DATA_GAP/PROXY_USED` exists.

Each signal card contains fact summary, why it matters, transmission, affected objects, evidence boundary, next verification and falsifier.

## Exact deterministic public-depth acceptance

`PUBLIC_CORE_ACCEPTED` is forbidden unless the same Daily V4 logic used by Work would pass the public surface:

- 3–5 signal cards;
- Executive Signal Summary ≥150 CJK;
- 今日关键信号 section ≥850 CJK;
- every signal card ≥180 CJK;
- China Chain Delta ≥120 CJK;
- Global Energy Delta ≥120 CJK;
- Industry/Operator Exposure ≥120 CJK;
- explicit falsifier/counterevidence;
- explicit next-verification/trigger set;
- every material `DATA_GAP` has proxy/boundary or governed no-proxy treatment;
- strong claims have evidence + boundary treatment;
- normal-day body ≥1,800 CJK;
- reference band 2,200–3,500 CJK; weekend/holiday may use governed shorter mode but does not waive section/card depth.

The manifest must record `v4_public_depth_gate_status=PASS` plus the measured CJK/card values. Marker/card-count checks alone are not composition acceptance.

## Public-safe boundary

GitHub contains no JOVO/九丰-specific operating, contract, margin, capital-allocation or opportunity judgment. `JOVO_DIRECTIONAL_EXPOSURE` is private-only Work reconciliation.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest records: `editorial_contract=DAILY_V4_PUBLIC_CORE`, `language=zh-CN`, `public_composition_status=PASS`, `v4_public_depth_gate_status=PASS`, signal-card count, window/privacy/evidence/write/readback PASS and `unsupported_core_claims=0`.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites.
