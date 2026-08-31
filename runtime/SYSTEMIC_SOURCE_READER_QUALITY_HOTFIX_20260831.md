# ReportOps｜Systemic Source & Reader Quality Hotfix｜2026-08-31

Status: `CHAT_SYSTEM_AUDIT_COMPLETE__PENDING_WORK_FORMALIZATION`

## Why this hotfix exists

The defect is not a single bad link. Full Authority audit found a multi-layer quality-control gap:

1. `2026-08-29` contains one synthesized Reuters slug in the formal source list.
2. Reader V1 cutover on 2026-08-29 removed the legacy Reader's clickable Source-reference behavior: legacy 8/28 rendered `Source:Sx` as clickable source references/cards; V1 rendered them as plain text.
3. `reader_design_regression_gate_v1.py` validates DOM/CSS structure but not citation functionality.
4. `READER_DESIGN_SYSTEM_V1` requires renderer screenshot regression, but Authority contains no executable screenshot-regression gate.
5. Existing Source Acquisition audit can PASS on structurally plausible URLs without proving the URL was actually observed from the publisher/search result.
6. Formal V4 Gate Registry lacks Source Identity, Inline Citation, Reader Citation Functionality, Expert Signal Priority, Bridge/Canonical Identity and Runtime Version Drift gates.
7. GitHub's pre-formal 8/29 body diverges from the formal Chinese V4 Canonical body; same-date correction must patch Canonical in place, never overwrite it from the old bridge body.
8. GitHub runtime policy files are v1.5 candidate while formal Authority remains v1.4; the state must declare this distinction until Work formalizes it.

## Chat-produced controlled assets

- `runtime/source_identity_gate_v1.py`
- `runtime/inline_citation_gate_v2.py`
- `runtime/render_daily_reader_v1_1.py`
- `runtime/QUALITY_GATE_REGISTRY_PATCH_SOURCE_READER_V1.csv`
- `daily/2026/08/2026-08-29/canonical_source_map.json`
- `daily/2026/08/2026-08-29/source_identity_correction.json`
- `daily/2026/08/2026-08-29/inline_citation_correction.json`
- `runtime/DAILY_RUNTIME_CONTRACT_PUBLIC.md` v1.5 candidate
- `runtime/BRIDGE_PROTOCOL.md` v1.5 candidate
- `runtime/EVIDENCE_POLICY_PUBLIC.md` v1.1
- `runtime/DAILY_TEMPLATE_PUBLIC.md`

## 8/29 correction rule

The prose authority is the current formal Library Authority body:
`ReportOps/outputs/energy/daily/2026-08-29/energy_daily_2026-08-29.md`.

The GitHub `public_core.md` for 8/29 is archival pre-formal Scheduled Chat input and MUST NOT replace the formal Chinese V4 Canonical prose.

Allowed same-date changes:
- replace S2 synthesized Reuters slug with the exact canonical Reuters URL from `canonical_source_map.json`;
- turn existing `[Source: Sx]` references into clickable links to the exact accepted source URL;
- preserve Private/Public content separation;
- render with citation-preserving Reader V1.1;
- no claim/prose/fixed-window research rewrite.

## Reader functionality acceptance

For the corrected 8/29 and all new V1 Dailies:
- source links must be clickable in the narrative, not only in a bottom Sources appendix;
- every Signal Card must expose at least one inline source link;
- final Reader article must contain all unique accepted external source URLs;
- no external `[Source:Sx]` marker may remain plain text;
- external links must preserve exact accepted canonical hrefs;
- Reader renderer release must have functional regression evidence in addition to DOM/CSS regression.

## Formal Work transaction

Work should perform one bounded transaction:
1. verify current Authority base and Current Daily;
2. copy the Chat-produced runtime assets into formal Authority and merge the Gate Registry patch;
3. patch the formal 8/29 Canonical body in place from `canonical_source_map.json`;
4. render 8/29 with Reader V1.1 and run Source Identity + Inline Citation v2 + Reader/V4/Evidence/Lineage/State/Freshness gates;
5. process 8/30 and any ready 8/31 oldest-first using the same formalized gates;
6. publish Private → authenticated readback → Public → remote readback → Download → SHA/ZIP;
7. update Current/derived views and GitHub deployment state to formal v1.5 only after successful formalization;
8. rebuild Authority ZIP and prove the new runtime assets/gates survive rebuild.

No public re-research. No higher-cycle authoring. No new project phase.

## Stability rule

Do not re-sign `REPORTOPS_STABILIZED_BASELINE_V4=PASS` merely because this hotfix transaction succeeds.
Require at least two consecutive natural Daily cycles that pass:
- Source Identity;
- Inline Citation;
- Expert Signal Priority;
- V4 Depth;
- Work first-pass reconciliation;
- Reader functionality;
- Private/Public/Download publication;
without manual editorial repair.
