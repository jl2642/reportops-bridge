# ReportOps Public Evidence Policy v1.2

Status: `STRICT_NEW_PUBLIC_SOURCE_IDENTITY_RECEIPT_BLOCKING`

## Mode

New Daily bridge outputs use `STRICT_NEW_PUBLIC`.

## Atomicity

One claim ID = one independently testable proposition. One source may support several claims; one claim may use several independent sources.

## Exact source identity — BLOCKING

For every external CORE or MATERIAL evidence record, the URL must come from an actually observed search result, opened page, official document listing, or publisher-returned canonical URL. **Never construct, autocomplete, infer, or rewrite a publisher slug from the article title.**

Each external record must contain:
- `url`: exact accepted canonical document URL;
- `title`;
- `publisher`;
- `publication_time` when available;
- `url_identity_status`;
- `url_verified_date`;
- `source_identity_receipt` with:
  - `verification_method`: `SEARCH_RESULT_OBSERVED`, `OPENED_EXACT_DOCUMENT`, `CANONICAL_REDIRECT_CONFIRMED`, or `OFFICIAL_DOCUMENT_LISTING`;
  - `observed_url`;
  - `canonical_url`;
  - `observed_title`;
  - `observed_publisher`;
  - `title_match_status`: `EXACT` or `SAME_DOCUMENT_UPDATED_TITLE`;
  - `verified_at`.

The receipt is the auditable trace of what Chat actually observed during source acquisition. A self-declared `url_identity_status=PASS` without a receipt is not sufficient.

Blocking failures include:
- guessed/synthesized URL;
- no observed source identity;
- receipt missing/incomplete;
- receipt canonical URL != Evidence URL;
- title/document mismatch;
- publisher/domain mismatch;
- generic/search/home page used as CORE evidence.

Paywall, anti-bot behavior and transient reachability do not by themselves invalidate source identity if the exact document identity was observed.

Method/absence records may have `url=null` only when explicitly typed `METHOD_RESULT`.

## Source rules

- CORE claims require an exact document/data/methodology page.
- Reprints/aggregators may corroborate but do not replace a directly available primary/professional source.
- Publication time and data period are separate.
- Superseded evidence must not remain PRIMARY.

## Direct support

- CORE: `DIRECT` support required.
- MATERIAL: at least `PARTIAL` support.
- Analytical inference must be labelled and bound to underlying facts.

## Cross-check

CORE claims normally require an independent cross-check unless they are a single authoritative datum with no logical independent issuer. Independence is by publisher/ownership group, not merely different URLs.

## Price semantics

Any price record must disclose value, unit, currency, geography, basis and observation time. Live, settlement, assessed, average, indicative, proxy and model-estimated values must not be described interchangeably.

## Reader-facing citation

Evidence storage is not reader citation. External sources used in the narrative must also satisfy the separate Inline Citation gate; a bottom Sources appendix alone is insufficient.

## Public-safe restriction

Do not commit internal/private/JOVO-specific analysis to the public bridge.

## Minimum acceptance

A bridge Daily candidate is accepted only if:
1. Source Identity v2 receipt gate = PASS;
2. required evidence metadata is present;
3. no blocking unsupported CORE claim remains;
4. strong claims are supported or downgraded;
5. source times respect the fixed Daily window;
6. price semantics are complete where used;
7. prohibited/private content is absent.

`PUBLIC_CORE_ACCEPTED` is forbidden when any source URL is guessed, synthesized, not observed, or lacks a valid acquisition receipt.

## Strict V2 Ledger — existing Authority contract mirror (producer-readable, BLOCKING)

This section mirrors the **existing** canonical ReportOps Authority, not a new schema or a relaxation of any gate. It is the permitted public-safe reference for the frozen 10:15 Producer. Source Authority ZIP SHA-256 at synchronization: `b72ed50f71fbdf0b726ce151be7f53dfe89a4e78cfbb99ad60038fa3e7aaaaad` (2026-11-06). Exact normative paths within that ZIP:
- `runtime/contracts/EVIDENCE_GOVERNANCE_CORE_V2.md`
- `runtime/schemas/EVIDENCE_SCHEMA_V2_FIELDS.csv` (42 business/schema fields)
- `runtime/schemas/evidence_schema_v2.json`
- `runtime/config/evidence_governance_policy_v2.json`
- `scripts/evidence/evidence_governance_validator.py`

For new Daily, the **ledger** `schema_version=2.0`, `schema_mode=STRICT_NEW`; `STRICT_NEW_PUBLIC` is the distinct bridge acquisition-receipt policy mode for evidence.json, **not** a ledger `schema_mode` enum. Historical accepted products may use `LEGACY_COMPAT` for read-only diagnostics, not for new candidate acceptance.

### Exact 43-column serialized Daily CSV header

The first `index` field is a zero-based CSV serialization index (0..n-1) observed in the accepted canonical 2026-11-06 Daily ledger; the Authority's `EVIDENCE_SCHEMA_V2_FIELDS.csv` contains **42 normative claim/evidence fields**. Do not invent a 43rd business field or count the index as an Evidence claim.

```csv
index,schema_version,schema_mode,record_id,claim_id,claim_text,claim_type,claim_importance,report_cycle,report_period,report_cutoff,source_id,source_name,source_publisher,source_type,source_tier,source_url,canonical_url,url_surface,publication_time,data_period_start,data_period_end,retrieved_at,direct_support,support_excerpt,cross_check_required,cross_check_group,independence_group,series_id,version_id,superseded_status,superseded_by,usage_policy,confidence,price_value,price_unit,price_currency,price_geography,price_basis,price_observation_time,proxy_disclosure,data_boundary,notes
```

Use UTF-8 CSV with the header exactly in this order, one row per atomic claim-source relation. Preserve quoting for commas, quotes and line breaks. Each external `source_id`/canonical URL must bind to the **actually observed** Evidence JSON acquisition receipt; do not invent sources, timestamps or claim support.

### Existing Authority enum values — exact tokens, no near-synonyms

| Field | Allowed values |
|---|---|
| schema_mode | `STRICT_NEW`, `LEGACY_COMPAT` |
| claim_type | `PRICE`, `MARKET_DATA`, `EVENT`, `POLICY`, `FORECAST`, `PROJECT`, `COMPANY`, `ANALYSIS`, `METHODOLOGY`, `BACKGROUND`, `INTERNAL_LINEAGE` |
| claim_importance | `CORE`, `MATERIAL`, `NORMAL`, `CONTEXT` |
| report_cycle | `DAILY`, `WEEKLY`, `MONTHLY`, `QUARTERLY`, `ANNUAL` |
| source_type | `OFFICIAL`, `REGULATOR`, `EXCHANGE`, `INSTITUTIONAL`, `PROFESSIONAL_DATA`, `WIRE`, `ORIGINAL_MEDIA`, `REPRINT`, `AGGREGATOR`, `COMPANY`, `INTERNAL` |
| source_tier | `T1_PRIMARY`, `T2_PROFESSIONAL`, `T3_TRACEABLE_SECONDARY`, `T4_WEAK_SURFACE`, `INTERNAL` |
| url_surface | `EXACT_DOCUMENT`, `DATA_PAGE`, `METHODOLOGY_PAGE`, `HOMEPAGE`, `INDEX`, `SEARCH`, `AGGREGATION`, `INTERNAL_ARTIFACT` |
| direct_support | `DIRECT`, `PARTIAL`, `INDIRECT`, `UNVERIFIED` |
| superseded_status | `CURRENT`, `SUPERSEDED`, `UNKNOWN`, `NOT_APPLICABLE` |
| usage_policy | `PRIMARY`, `CORROBORATION`, `CONTEXT_ONLY`, `OBSERVATION_ONLY`, `DO_NOT_USE` |
| confidence | `HIGH`, `MEDIUM`, `LOW`, `UNVERIFIED` |
| price_basis | `LIVE`, `SETTLEMENT`, `ASSESSED`, `AVERAGE`, `INDICATIVE`, `PROXY`, `MODEL_ESTIMATE` |

### Existing field requirements and governance thresholds

- Required for every new claim row: `schema_version`, `schema_mode`, `record_id`, `claim_id`, `claim_text`, `claim_type`, `claim_importance`, `report_cycle`, `report_period`, `report_cutoff` (explicit timezone), `source_id`, `source_name`, `source_type`, `source_tier`, `url_surface`, `direct_support`, `cross_check_required` (boolean true/false), `superseded_status`, `usage_policy`, `confidence`.
- External strict rows additionally require `source_publisher`, `source_url`, `canonical_url`, `publication_time` (source publication, not retrieval), `retrieved_at` and `independence_group`. `data_period_start`/`data_period_end` are conditional; never substitute them for `publication_time`.
- CORE/MATERIAL strict rows require `support_excerpt` and `data_boundary`; CORE requires `direct_support=DIRECT` and an exact document/data/methodology page. MATERIAL requires `DIRECT` or `PARTIAL`. `cross_check_group` links corroboration rows where required; independent publisher/owner group matters.
- `series_id`, `version_id`, `superseded_by`, `cross_check_group`, `proxy_disclosure`, `notes` are conditional or optional as declared in the Authority schema; do not backfill nonexistent values.
- PRICE strict rows must supply `price_value`, `price_unit`, `price_currency`, `price_geography`, `price_basis`, `price_observation_time`; `price_basis=PROXY` additionally requires `proxy_disclosure`. No inferred numeric price or timestamp.
- Existing Authority freshness thresholds (days by claim_type): `PRICE=3`, `MARKET_DATA=45`, `EVENT=14`, `POLICY=120`, `FORECAST=180`, `PROJECT=180`, `COMPANY=180`, `ANALYSIS=365`, `METHODOLOGY=1095`, `BACKGROUND=1095`, `INTERNAL_LINEAGE=3650`. CORE stale data or superseded PRIMARY evidence fail closed subject to actual native validator results.
- New-product ledger mode is `STRICT_NEW`; there is no permission to downgrade a new candidate to `LEGACY_COMPAT` to pass. Source Identity v1.2 acquisition receipt and clickable inline citations remain **additional independent** gates.

### Producer bridge Manifest — current accepted identity (not a replacement validator)

Current accepted Daily bridge manifests (e.g. 2026-11-03) use `schema_version=REPORTOPS_DAILY_MANIFEST_V1_5_SINGLE_SITE` and record `target_date`, `window_start`, `window_end`, `scheduled_for`, `producer_status`, `product_status`, `formal_status`, `cjk_characters_actual`, `executive_cjk_actual`, `key_signal_cjk_actual`, `signal_card_cjk_actual`, `china_chain_cjk_actual`, `global_energy_cjk_actual`, `industry_operator_cjk_actual`, `signal_card_count`, `evidence_record_count`, `source_url_count_distinct`, `public_contract_sha256`, `authority_policy_sha256`, `source_identity_gate_status`, `inline_citation_gate_status`, `exact_v4_machine_structure_status`, `v4_public_depth_gate_status`, `privacy_status`, `window_status`, `evidence_status`, `strict_v2_ledger_status`, `producer_self_audit_status`, `consumer_status`, `canonical_mutation_performed=false`, `site_publication_performed=false`, `site_mutation_performed=false`, `work_may_rewrite=false`, `warnings` and `next_work_action`.

Record actual measurable gate results only; `source_identity_gate_status` and `strict_v2_ledger_status` cannot be self-declared PASS without evidence. For a Producer-accepted unpromoted candidate use the existing `PUBLIC_CORE_ACCEPTED_PENDING_WORK` product state and `PENDING_WORK_RECONCILIATION` formal state. Never set Formal Current, Reader, Lineage or Work P8G success in Chat.

The Authority ZIP and its SHA sidecar remain immutable. This section is a **public-safe deterministic mirror** of existing requirements; Work's native consumer gates continue to govern formal publication.
