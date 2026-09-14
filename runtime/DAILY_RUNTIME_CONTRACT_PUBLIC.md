# ReportOps Daily Public Runtime Contract v1.5

Status: `R3_1_DAILY_V4_PUBLIC_CORE_ACTIVE_SINGLE_SITE`
Editorial contract: `DAILY_V4_PUBLIC_CORE`
Language: `zh-CN`

## Product role

Daily answers: **固定窗口内出现了哪些新的、可验证、且对能源产业决策最重要的信号，它们通过什么机制影响价格、供需、物流、资产和产业链？** Role: `SIGNAL_RADAR`.

## Runtime role

10:15 Asia/Shanghai Scheduled Chat is the Daily continuity/editorial controller. 12:30 Work is the downstream formal reconciler/promoter/single-site publisher and must not redo public-web research or rewrite an Accepted public core.

Before new-day production, Chat compares `CURRENT_PUBLIC`, `status/latest` and recent manifests/correction receipts. Unpromoted newer candidates or same-date accepted corrections are correction backlog and must be handled before silent continuity.

## Fixed window

`[D-1 10:00, D 10:00) Asia/Shanghai`. Delays never move the window.

## Source identity v2 acquisition-receipt gate — BLOCKING

Apply `EVIDENCE_POLICY_PUBLIC v1.2`.

Every external CORE/MATERIAL source URL must be an actually observed/canonical exact-document URL, never generated from a title. Each record must carry a complete source_identity_receipt matching observed URL/title/publisher and accepted canonical URL. Manifest requires `source_identity_gate_status=PASS_V2`, `unverified_external_source_count=0`, `guessed_url_count=0`.

## Inline clickable citation gate — BLOCKING

Every external CORE/MATERIAL Evidence record used in narrative must have a clickable Markdown Evidence link adjacent to the supported fact. A bottom Sources appendix alone is insufficient. Every Signal Card must include at least one inline clickable source. Work must rerun citation validation against final Reader HTML.

## Expert signal-priority gate — BLOCKING

Before selecting 3–5 cards, rank eligible evidence by physical/economic impact, magnitude, China/Asia relevance, incremental information and actionability. Lower-priority structural items must not displace materially more relevant same-window energy signals.

## Exact V4 machine composition — BLOCKING

The current `runtime/DAILY_TEMPLATE_PUBLIC.md` skeleton is normative, not illustrative.

Required tokens/grammar include:
- `<!-- MODULE:EXECUTIVE_SIGNAL_SUMMARY -->`
- `<!-- KEY_SIGNAL_CARDS:3-5 -->`
- 3–5 card headings beginning `### 信号卡N` or `### Signal Card N`
- `<!-- MODULE:MARKET_AND_EVENT_DELTA -->`
- `<!-- MODULE:PRICE_AND_SPREAD_DELTA -->`
- `<!-- MODULE:CHINA_CHAIN_DELTA -->`
- `<!-- MODULE:GLOBAL_ENERGY_DELTA -->`
- `<!-- MODULE:RESEARCH_TRIGGER_BOARD -->`
- `<!-- MODULE:INDUSTRY_CHAIN_AND_OPERATOR_EXPOSURE -->`
- `<!-- MODULE:EVIDENCE_AND_GAPS -->`
- `<!-- NEXT_VERIFICATION -->`

Semantic similarity, English all-caps headings, merged sections, or numbered headings without the required machine marker/card prefix do **not** satisfy this gate.

`PUBLIC_CORE_ACCEPTED` and `v4_public_depth_gate_status=PASS` are forbidden unless the exact machine composition check passes first.

## Exact deterministic public-depth acceptance

Normal Daily requires:
- 3–5 signal cards;
- Executive ≥150 CJK;
- 今日关键信号 ≥850 CJK;
- every signal card ≥180 CJK;
- China Chain ≥120 CJK;
- Global Energy ≥120 CJK;
- Industry/Operator Exposure ≥120 CJK;
- explicit falsifier/counterevidence;
- explicit next-verification/trigger set;
- governed DATA_GAP boundary;
- strong claims with evidence + boundary;
- normal-day body ≥1,800 CJK;
- 2,200–3,500 CJK reference band.

## Public-safe boundary — BLOCKING

GitHub contains only public-safe generic operator/industry analysis. Public narrative must not include `JOVO` or `九丰` tokens or any specific-company non-public contract, margin, inventory, customer, vessel, financing or project information. Negative-form disclaimers naming a specific company also fail public-safe wording; use generic wording such as “任何特定公司的非公开信息”.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest must show Source Identity PASS, Inline Citation PASS, Expert Signal Priority PASS, exact V4 machine structure PASS, V4 Depth PASS, privacy PASS, Evidence/window/write/readback PASS and unsupported CORE claims = 0.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites. Current live distribution is single-site public; Private Site is retired from live operation.
