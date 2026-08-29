# ReportOps Daily Public Runtime Contract v1.2

Status: `R3_1_DAILY_V4_PUBLIC_CORE_ACTIVE`
Editorial contract: `DAILY_V4_PUBLIC_CORE`
Language: `zh-CN` (source titles/identifiers may remain original language)

## Product role

Daily answers: **固定窗口内出现了哪些新的、可验证的能源市场信号，它们通过什么机制影响价格、供需、物流和产业链？** Role: `SIGNAL_RADAR`.

## Runtime role

10:15 Asia/Shanghai Scheduled Chat remains the sole Daily continuity controller. Priority: secure D → persist accepted public core/evidence/manifest → scan continuity → recover at most two oldest gaps. No evening task. 12:30 Work remains downstream formal reconciler/publisher and must not redo public-web research.

## Fixed window

`[D-1 10:00, D 10:00) Asia/Shanghai`. Delays never move the window.

## V4 public-core composition

The accepted `public_core.md` must be Chinese analytical prose and use these semantic markers:

1. `EXECUTIVE_SIGNAL_SUMMARY`
2. `KEY_SIGNAL_CARDS:3-5` with 3–5 `### 信号卡...` subsections
3. `MARKET_AND_EVENT_DELTA`
4. `PRICE_AND_SPREAD_DELTA`
5. `CHINA_CHAIN_DELTA`
6. `GLOBAL_ENERGY_DELTA`
7. `RESEARCH_TRIGGER_BOARD`
8. `INDUSTRY_CHAIN_AND_OPERATOR_EXPOSURE`
9. `EVIDENCE_AND_GAPS`
10. `NEXT_VERIFICATION`
11. conditional Proxy Matrix when material `DATA_GAP/PROXY_USED` exists.

Each signal card must contain: fact summary, why it matters, transmission, affected objects, evidence boundary, next verification and falsifier. Prefer `DATA_GAP / NEEDS_CONFIRMATION` over filler. Weekend mode may be shorter only when it explicitly reviews prior-week signals, next-week risk path, gaps and next-open verification.

## Public-safe boundary

GitHub contains no JOVO/九丰-specific operating, contract, margin, capital-allocation or opportunity judgment. `JOVO_DIRECTIONAL_EXPOSURE` is a private-only Work reconciliation layer and must never appear in `public_core.md`.

## Acceptance metadata

Before `PUBLIC_CORE_ACCEPTED`, manifest must record `editorial_contract=DAILY_V4_PUBLIC_CORE`, `language=zh-CN`, `public_composition_status=PASS`, `signal_card_count=3..5`, window/privacy/evidence/write/readback PASS and `unsupported_core_claims=0`.

GitHub is bridge durability, not Canonical Authority, and never publishes Sites.
