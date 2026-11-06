# Handoff — supplier self-survey and single quality manual

Updated 2026-11-05. Internal document; do not send this handoff to the customer.

## Single source of truth

The only maintained quality manual is `00-manual/QM-001_Quality_Manual.md`, with a generated DOCX at the same location. Revision C is approved and effective 2026-11-05 by explicit owner instruction. It retains the approved scope, policy, guidance-only standards language and external-service wording, and incorporates the practical controls previously maintained in a separate basic manual. The separate basic-manual and superseded scope-addendum files are removed; prior versions remain in Git history.

There is no manual in a customer-specific folder. QM-002 is the companion policy and QM-003 is the objectives document, not competing manuals.

## Preserved owner decisions

- Metallic or non-metallic machining for customers in a variety of industries.
- Only explosives and flight-hardware scope limits retained; no §1.3 design exclusion.
- No certification or quality-standard compliance claim; standards provide guidance and best practice.
- No specific customer names or We/Our language in the general manual.
- Customer-approved sources where required by the reviewed wording.
- General in-house calibration/verification using known-good standards, with customer requirements taking precedence; no dedicated caliper form or fixed reference values.
- Approved WI-008 hang tags: green INSPECTED/red REJECTED, each with QC initials, inspection date and part number.
- Ten-year minimum job retention, extended by any longer applicable requirement; existing backup/retrieval commitments retained.

## Manual navigation

Policy §3.1; ethics/conformity/acknowledgment §§3.4–3.6; competence §5.1; external services §5.3. Operating controls: data §6.1, document control §6.2, contract review §6.3, suppliers §6.4, material §6.5, calibration §6.6, production/inspection §6.7, NCR/MRB §6.8, corrective/preventive action §6.9, records §6.10, review §6.11, flowdown §6.12.

## Submission files

After actual release and readiness checks: completed QA-1003 survey, `00-manual/QM-001_Quality_Manual` PDF, and the separate unnumbered courtesy attachment `supplier-paperwork/karman/submission/QA-1003_QM-001_Cross_Reference`. Keep working assessments, readiness records, job plans and this handoff internal unless requested.

Survey working answers and courtesy references are remapped to the consolidated manual. Answers are drafts, not completed or verified activities.

## Outstanding work

Use STATUS.md as the task list. Consolidation approval is complete. QF-028 contains 22 actual owner-listed instruments/sets with thematic IDs. QF-030 is synchronized and QF-020 records owner-reported in-house calibration dated 2026-11-01. Annual calibration is assigned, next due 2027-11-01; pins are Class ZZ minus. Remaining priorities: confirm pending technical details and set contents, apply labels and verify job suitability/customer requirements. The provisional caliper identity is superseded for current planning. Confirm material certificates, profile and contract/DoD/CUI requirements. Do not invent a website, certification, score, instrument certificate, calibration or signature.

## Repository conventions

Keep `karman/basic-qms` separate; do not merge without owner direction. Present proposed wording in chat before further revisions. Update Markdown source and regenerate its Word counterpart; never regenerate over completed signed job records. Record actions in AGENT-LOG.md and status in STATUS.md.




