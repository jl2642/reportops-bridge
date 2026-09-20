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

Apply `EVIDENCE_POLICY_PUBLIC v1.2`. Every external CORE/MATERIAL source URL must be an actually observed/canonical exact-document URL, never generated from a title.

## Inline clickable citation gate — BLOCKING

Every external CORE/MATERIAL Evidence record used in narrative must have a clickable Markdown Evidence link adjacent to the supported fact. Every Signal Card must include at least one inline clickable source.

## Expert signal-priority gate — BLOCKING

Before selecting 3–5 cards, rank eligible evidence by physical/economic impact, magnitude, China/Asia relevance, incremental information and actionability.

## Exact V4 machine composition — BLOCKING

The current `runtime/DAILY_TEMPLATE_PUBLIC.md` skeleton is normative, not illustrative. Required MODULE markers, KEY_SIGNAL_CARDS marker, signal-card heading grammar and NEXT_VERIFICATION marker must be preserved exactly.

## Single numerical depth authority — BLOCKING

The public runtime must load all Daily numerical depth thresholds from `runtime/DAILY_PUBLIC_DEPTH_POLICY_V4.json`.

That file is only a public-safe mirror of the machine Authority inside ReportOps:
`scripts/product/PRODUCT_FINAL_COMPOSITION_POLICY_V4.json`.

10:15 Chat must not maintain an independent governing threshold table in its prompt or prose. 12:30 Work must compute the public subset from the current Authority package and verify the mirror `public_contract_sha256`. Any mismatch is `RUNTIME_CONTRACT_VERSION_DRIFT` and is fail-closed until deterministically reconciled.

Qualitative blocking requirements remain: explicit falsifier/counterevidence, explicit next-verification/trigger set, governed DATA_GAP boundary, strong claims with evidence + boundary, exact structure, privacy, Evidence and fixed-window compliance.

## Public-safe boundary — BLOCKING

GitHub contains only public-safe generic operator/industry analysis. Public narrative must not include `JOVO` or `九丰` tokens or any specific-company non-public contract, margin, inventory, customer, vessel, financing or project information.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest must show Source Identity PASS, Inline Citation PASS, Expert Signal Priority PASS, exact V4 machine structure PASS, V4 Depth PASS, privacy PASS, Evidence/window/write/readback PASS and unsupported CORE claims = 0. It must also record the depth-policy mirror identity used for deterministic measurement.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites. Current live distribution is single-site public; Private Site is retired from live operation.
