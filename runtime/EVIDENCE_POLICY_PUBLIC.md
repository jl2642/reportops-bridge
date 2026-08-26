# ReportOps Public Evidence Policy v1

Derived from the internal Evidence Governance Core, with private/internal fields removed.

## Mode

New Daily bridge outputs use `STRICT_NEW_PUBLIC`.

## Atomicity

One claim ID = one independently testable proposition. One source may support several claims; one claim may use several independent sources.

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

Do not commit internal ReportOps lineage identifiers, internal research-object state, user/private inputs or JOVO-specific private analysis. Public bridge IDs are local to this repository and do not claim Canonical lineage authority.

## Minimum acceptance

A bridge Daily candidate is accepted only if:

1. required public evidence metadata is present;
2. no blocking unsupported CORE claim remains;
3. strong claims are supported or downgraded;
4. source times respect the fixed Daily window;
5. price semantics are complete where prices are used;
6. prohibited/private content is absent.
