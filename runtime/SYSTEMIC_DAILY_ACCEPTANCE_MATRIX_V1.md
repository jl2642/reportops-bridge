# ReportOps Daily Systemic Acceptance Matrix v1

Status: `CHAT_CANDIDATE__PENDING_FORMAL_AUTHORITY`

A Daily system may be called healthy only when every applicable row below is explicitly evaluated. A PASS in one layer may not stand in for another layer.

| Layer | Acceptance question | Blocking evidence | Owner |
|---|---|---|---|
| 1. Authority | Is CURRENT_POINTER the unique machine Current and is base Authority SHA known? | pointer/SHA readback | Work |
| 2. Automation trigger | Did the scheduled Chat actually run and persist target-date artifacts? | task run + GitHub readback | Chat |
| 3. Fixed window | Are accepted sources inside the half-open Daily window, with event time separated from publish time? | window gate | Chat |
| 4. Source identity | Is every external CORE/MATERIAL URL an actually observed exact/canonical document rather than a guessed slug? | Source Identity v2 | Chat |
| 5. Acquisition trace | Does every external source carry observed URL/title/publisher/method/time receipt matching Evidence? | source_identity_receipt | Chat→Work |
| 6. Claim support | Are CORE claims directly supported and inference/boundary explicit? | Evidence gate | Chat→Work |
| 7. Price semantics | Are live/settlement/assessment/proxy values correctly typed with unit/basis/time/geography? | price semantics gate | Chat |
| 8. Expert signal selection | Are 3–5 cards the highest-value same-window energy signals, not filler or merely fresh structural data? | signal-selection rationale/matrix | Chat |
| 9. Product depth | Does the Daily meet V4 section/card depth and falsifier/next-verification requirements? | V4 depth validator | Chat→Work |
| 10. Reader-facing citation | Can the reader click the source next to the material fact, not only at the bottom? | Inline Citation v2 | Chat→Work |
| 11. Reader citation functionality | Does final Reader HTML preserve exact accepted hrefs and eliminate plain Source markers? | Reader citation functional gate | Work |
| 12. Reader DOM/CSS | Does final Reader satisfy READER_DOM_V1 / DS V1 static design contract? | Reader design gate | Work |
| 13. Renderer release regression | If renderer changed, did functional + desktop/mobile/print regression pass? | release regression evidence | Work |
| 14. Public/Private composition | Is public core identical/equivalent across surfaces, JOVO private-only, and private layer present? | composition/privacy/parity gates | Work |
| 15. Bridge ↔ Canonical identity | For same-date corrections, is formal Canonical prose protected from divergent pre-formal bridge bodies? | body authority/hash/provenance | Work |
| 16. Runtime version consistency | Do Authority, GitHub runtime state and scheduled tasks agree on formal active vs pending versions? | version-state gate | Work |
| 17. Current metadata freshness | Are all derived Current views regenerated from the final committed pointer with provenance? | freshness validator | Work |
| 18. Publication ordering | Did Private pass authenticated readback before Public advanced? | transaction checkpoint | Work |
| 19. Remote reader acceptance | Do Private/Public live pages preserve body, citations, navigation and current date? | remote readback | Work |
| 20. Download integrity | Does downloadable HTML/ZIP match formal product and SHA? | remote SHA/ZIP | Work |
| 21. Authority rebuild survival | Did new runtime/gates survive final ReportOps.zip rebuild? | post-rebuild asset assertion | Work |
| 22. Natural-cycle stability | Did consecutive natural Dailies pass first try without manual editorial correction? | >=2 natural-cycle checkpoints | Chat independent acceptance |

## Current 2026-08-31 audit status

- Rows 1/14/17/18/19/20/21: last formal state is 2026-08-29; new systemic hotfix pending Work.
- Rows 2/3/6/7/8/9/10: 2026-08-31 Scheduled Chat produced a first-pass V1.5 candidate; Source Identity was subsequently upgraded to v2 receipts before Work.
- Rows 4/5: 8/29 defect exposed the old gap; v2 receipt mechanism now exists in Chat candidate runtime.
- Row 11: FAIL on formal 2026-08-29 Reader V1; citation-preserving Reader V1.1 candidate prepared.
- Row 12: prior static Reader gate passed but was insufficient to prove row 11.
- Row 13: formal contract requires screenshot regression, but no executable regression gate existed in Authority at audit time.
- Row 15: risk confirmed for 8/29; Canonical authority rule/source map now frozen.
- Row 16: drift confirmed; state now explicitly distinguishes formal Authority v1.4 from pending Chat v1.5.
- Row 22: NOT YET PASS. Do not re-sign stabilized baseline until two consecutive natural cycles pass the full applicable matrix without manual editorial repair.
