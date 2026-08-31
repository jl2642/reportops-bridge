# ReportOps Daily Public Runtime Contract v1.4

Status: `R3_1_DAILY_V4_PUBLIC_CORE_ACTIVE`
Editorial contract: `DAILY_V4_PUBLIC_CORE`
Language: `zh-CN`

## Product role

Daily answers: **固定窗口内出现了哪些新的、可验证、且对能源产业决策最重要的信号，它们通过什么机制影响价格、供需、物流、资产和产业链？** Role: `SIGNAL_RADAR`.

## Runtime role

10:15 Asia/Shanghai Scheduled Chat is the Daily continuity/editorial controller. 12:30 Work is the downstream formal reconciler/publisher and must not redo public-web research or rewrite an Accepted public core.

Before new-day production, Chat compares `CURRENT_PUBLIC`, `status/latest` and recent manifests. Unpromoted newer candidates are correction backlog and must be revalidated before silent continuity.

## Fixed window

`[D-1 10:00, D 10:00) Asia/Shanghai`. Delays never move the window.

## Source identity gate — BLOCKING BEFORE EDITORIAL ACCEPTANCE

Apply `EVIDENCE_POLICY_PUBLIC v1.1`.

For every external CORE/MATERIAL source:
- URL is copied from an observed source/search result; never generated from a title;
- title/publisher/domain identity is verified;
- evidence records include `url_identity_status` and verification date;
- all external CORE/MATERIAL records must pass.

Manifest must record:
- `source_identity_gate_status=PASS`;
- `verified_external_source_count`;
- `unverified_external_source_count=0`;
- `guessed_url_count=0`.

## Expert signal-priority gate — BLOCKING

Passing word counts is not enough. Before selecting 3–5 signal cards, rank eligible evidence by:

1. direct impact on oil/gas/LNG/LPG/refining/shipping/power/fuel economics;
2. magnitude or change in physical supply/demand/flow/price/contract availability;
3. relevance to China/Asia and JOVO-adjacent value chains;
4. timeliness and incremental information versus prior Daily;
5. actionability: a clear next observable, risk path or decision implication.

A lower-priority structural item may appear in Global Energy / Watchlist, but must not displace a materially more relevant same-window energy-market signal from the main cards.

Manifest must record:
- `expert_signal_priority_gate_status=PASS`;
- `primary_signal_count`;
- `secondary_structural_signal_count`;
- a short `signal_selection_rationale`.

## V4 composition

Use semantic markers:
`EXECUTIVE_SIGNAL_SUMMARY`, `KEY_SIGNAL_CARDS:3-5`, `MARKET_AND_EVENT_DELTA`, `PRICE_AND_SPREAD_DELTA`, `CHINA_CHAIN_DELTA`, `GLOBAL_ENERGY_DELTA`, `RESEARCH_TRIGGER_BOARD`, `INDUSTRY_CHAIN_AND_OPERATOR_EXPOSURE`, `EVIDENCE_AND_GAPS`, `NEXT_VERIFICATION`, conditional Proxy Matrix.

Each signal card contains fact summary, why it matters, transmission, affected objects, evidence boundary, next verification and falsifier.

## Exact deterministic public-depth acceptance

`PUBLIC_CORE_ACCEPTED` is forbidden unless:
- 3–5 signal cards;
- Executive ≥150 CJK;
- 今日关键信号 ≥850 CJK;
- every signal card ≥180 CJK;
- China Chain ≥120 CJK;
- Global Energy ≥120 CJK;
- Industry/Operator Exposure ≥120 CJK;
- explicit falsifier/counterevidence;
- explicit next-verification/trigger set;
- material `DATA_GAP` has proxy/boundary or governed no-proxy treatment;
- strong claims have evidence + boundary;
- normal-day body ≥1,800 CJK;
- 2,200–3,500 CJK reference band; weekend mode may be shorter but does not waive section/card depth.

## Public-safe boundary

GitHub contains no JOVO/九丰-specific operating, contract, margin, capital-allocation or opportunity judgment.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest records: V4 depth PASS, source identity PASS, expert signal priority PASS, window/privacy/evidence/write/readback PASS and `unsupported_core_claims=0`.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites.
