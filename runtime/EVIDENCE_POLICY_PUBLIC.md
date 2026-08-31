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
