# ReportOps Daily Public Runtime Contract v1.5

Status: `R3_1_DAILY_V4_PUBLIC_CORE_ACTIVE`
Editorial contract: `DAILY_V4_PUBLIC_CORE`
Language: `zh-CN`

## Product role

Daily answers: **固定窗口内出现了哪些新的、可验证、且对能源产业决策最重要的信号，它们通过什么机制影响价格、供需、物流、资产和产业链？** Role: `SIGNAL_RADAR`.

## Runtime role

10:15 Asia/Shanghai Scheduled Chat is the Daily continuity/editorial controller. 12:30 Work is the downstream formal reconciler/publisher and must not redo public-web research or rewrite an Accepted public core.

Before new-day production, Chat compares `CURRENT_PUBLIC`, `status/latest` and recent manifests/correction receipts. Unpromoted newer candidates or same-date accepted corrections are correction backlog and must be handled before silent continuity.

## Fixed window

`[D-1 10:00, D 10:00) Asia/Shanghai`. Delays never move the window.

## Source identity gate — BLOCKING

Apply `EVIDENCE_POLICY_PUBLIC v1.1`.

Every external CORE/MATERIAL source URL must be an actually observed/canonical exact-document URL, never generated from a title. Manifest requires `source_identity_gate_status=PASS`, `unverified_external_source_count=0`, `guessed_url_count=0`.

## Inline clickable citation gate — BLOCKING

A correct URL stored only in Evidence Ledger or a bottom Sources appendix is **not sufficient**.

For every external CORE/MATERIAL Evidence record used in the Daily:
- the narrative body must contain a clickable Markdown link using the Evidence label and exact accepted URL, e.g. `[E03](https://...exact.../)`;
- every Signal Card must contain at least one inline clickable source adjacent to its factual basis;
- Executive/Market/China/Global sections must place clickable citations next to material factual claims where used;
- a plain `[E03]` token is not a citation;
- a raw URL only in `Public Sources` does not satisfy narrative citation coverage.

Before acceptance, run `runtime/inline_citation_gate_v1.py --evidence ... --markdown ...`. Manifest records:
- `inline_citation_gate_status=PASS`;
- `inline_clickable_evidence_count`;
- `plain_unlinked_evidence_marker_count=0` for external evidence used in narrative;
- `source_appendix_only_citation_count=0`.

Work must rerun the gate against final Reader HTML via `--html`; each Evidence label anchor must preserve the exact accepted canonical href in the rendered article.

## Expert signal-priority gate — BLOCKING

Before selecting 3–5 cards, rank eligible evidence by:
1. direct impact on oil/gas/LNG/LPG/refining/shipping/power/fuel economics;
2. magnitude/change in physical supply/demand/flow/price/contract availability;
3. China/Asia and JOVO-adjacent value-chain relevance;
4. timeliness/incremental information versus prior Daily;
5. actionability / next observable.

Lower-priority structural items may sit in Global Energy/Watchlist but must not displace materially more relevant same-window signals.

## V4 composition

Required semantic modules:
`EXECUTIVE_SIGNAL_SUMMARY`, `KEY_SIGNAL_CARDS:3-5`, `MARKET_AND_EVENT_DELTA`, `PRICE_AND_SPREAD_DELTA`, `CHINA_CHAIN_DELTA`, `GLOBAL_ENERGY_DELTA`, `RESEARCH_TRIGGER_BOARD`, `INDUSTRY_CHAIN_AND_OPERATOR_EXPOSURE`, `EVIDENCE_AND_GAPS`, `NEXT_VERIFICATION`, conditional Proxy Matrix.

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
- material DATA_GAP has governed boundary;
- strong claims have evidence + boundary;
- normal-day body ≥1,800 CJK;
- 2,200–3,500 CJK reference band.

## Public-safe boundary

GitHub contains no JOVO/九丰-specific operating, contract, margin, capital-allocation or opportunity judgment.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest must show:
- Source Identity PASS;
- Inline Citation PASS;
- Expert Signal Priority PASS;
- V4 Depth PASS;
- Evidence/window/privacy/write/readback PASS;
- unsupported CORE claims = 0.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites.
