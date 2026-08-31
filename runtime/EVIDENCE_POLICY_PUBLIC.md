# ReportOps Public Evidence Policy v1.1

Status: `STRICT_NEW_PUBLIC_SOURCE_IDENTITY_BLOCKING`

## Mode

New Daily bridge outputs use `STRICT_NEW_PUBLIC`.

## Atomicity

One claim ID = one independently testable proposition. One source may support several claims; one claim may use several independent sources.

## Exact source identity — BLOCKING

For every external CORE or MATERIAL evidence record, the URL must come from an actually observed search result, opened page, official document listing, or publisher-returned canonical URL. **Never construct, autocomplete, infer, or rewrite a publisher slug from the article title.**

Each external record must carry:

- `url`: observed/canonical exact-document URL;
- `title`: observed publisher/search-result title;
- `publisher`;
- `publication_time` when available;
- `url_identity_status`: one of `EXACT_SEARCH_RESULT_CONFIRMED`, `OPENED_EXACT_DOCUMENT`, `CANONICAL_REDIRECT_CONFIRMED`;
- `url_verified_date`;
- optional `resolved_url` when canonicalization/redirect changes the submitted URL.

Blocking failures:
- `SYNTHESIZED_OR_GUESSED_URL`;
- `URL_NOT_OBSERVED_FROM_SOURCE_RESULT`;
- `TITLE_URL_IDENTITY_MISMATCH`;
- `PUBLISHER_DOMAIN_MISMATCH`;
- `GENERIC_OR_SEARCH_PAGE_USED_AS_CORE`;
- any external CORE/MATERIAL record lacking source-identity verification.

Paywalls, anti-bot controls and transient publisher availability do **not** by themselves fail identity when the exact publisher result is observed. Reachability and identity are separate concepts.

Method/absence records may have `url=null` only when explicitly typed `METHOD_RESULT`.

## Source rules

- CORE claims require an exact document/data/methodology page, not a homepage, search page or generic aggregation page.
- Reprints/aggregators may corroborate but do not replace a directly available primary/professional source.
- Publication time and data period are separate fields.
- Superseded evidence must not remain PRIMARY.

## Direct support

- CORE: `DIRECT` support required.
- MATERIAL: at least `PARTIAL` support.
- Analytical inference must be labelled as analysis and bind to underlying facts.

## Cross-check

CORE claims normally require an independent cross-check unless they are a single authoritative datum with no logical independent issuer. Independence is by publisher/ownership group, not merely different URLs.

## Price semantics

Any price record must disclose value, unit, currency, geography, basis and observation time. Live, settlement, assessed, average, indicative, proxy and model-estimated values must not be described interchangeably.

## Public-safe restriction

Do not commit internal ReportOps lineage identifiers, internal research-object state, user/private inputs or JOVO-specific private analysis.

## Minimum acceptance

A bridge Daily candidate is accepted only if:

1. source identity gate = PASS for every external CORE/MATERIAL record;
2. required evidence metadata is present;
3. no blocking unsupported CORE claim remains;
4. strong claims are supported or downgraded;
5. source times respect the fixed Daily window;
6. price semantics are complete where prices are used;
7. prohibited/private content is absent.

`PUBLIC_CORE_ACCEPTED` is forbidden when any source URL was guessed, synthesized or not source-identity verified.
