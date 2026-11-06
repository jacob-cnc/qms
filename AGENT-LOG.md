# Agent Log

Significant actions taken by AI agents on this project.

---

## 2026-08-10 — Quick (Project Manager Handoff)

**Action:** Initial PM review and corrections

1. **Research phase** — Conducted deep research (10 parallel tracks, 305KB) on AS9100 Rev D requirements for a 1-person CNC machine shop. Produced consolidated reference guide.

2. **Document review** — Reviewed 10 highest-risk documents against AS9100D requirements:
   - QM-001 Quality Manual
   - QP-003 Purchasing & Supplier Management
   - QP-008 Nonconforming Product
   - QP-009 Corrective Action
   - QP-010 Calibration
   - QP-011 Internal Audit
   - QP-012 Management Review
   - QP-014 Risk Management
   - QP-015 Configuration Management
   - QP-022 First Article Inspection

3. **Issues found and fixed (17 total):**
   - 3 CRITICAL: "Excluded" terminology, duplicated sections, missing Clause 8.1.1 operational risk
   - 5 HIGH: Wrong clause references, missing ECN process, management review inputs, FAI standard revision, clause mapping error
   - 6 MEDIUM: Calibration recall, personally-owned equipment, GIDEP reporting, similar-process CA review, concession definition, FAI trigger
   - 3 LOW: Retention statement, audit criteria, date inconsistency

4. **Cross-reference audit** — Verified 360 document references, Master Document List alignment (75/75), and form title consistency. Fixed 7 title mismatches.

5. **DOCX regeneration** — Ran `convert_md_to_docx.py --all` (99 files converted).

6. **Git initialization** — Created repo with initial commit (200 files), `.gitignore`, `PROJECT.md`, and `AGENT-LOG.md`.

**Files modified:** QM-001, QP-003, QP-005, QP-008, QP-009, QP-010, QP-011, QP-012, QP-014, QP-015, QP-016, QP-018, QP-022, QP-023, QP-025 (15 markdown files + all DOCX regenerated)

**Issues tracker:** `completion-reports/review-issues.md`

---

## 2026-11-05 — Kiro Crew (Karman ASL self-survey)

**Action:** Built a standalone basic quality system for Tier 3 supply to Karman and drafted the self-survey answers.

1. Reviewed the `review/karman-supplier-paperwork` drafts against the survey PDF and the dev QMS; recorded gaps (QM-001 calibration/retention/"posted"/"audits contracted" claims; Rev B drafts overwrite approved revs).
2. Wrote `07-basic-qms/QSM-001_Basic_Quality_System_Manual` (supersedes draft KMS-001) and `supplier-paperwork/karman/working/Survey-answers-draft`; registered QSM-001 in the Master Document List.
3. Entered owner facts: LLC formed 2025-03-05, equipment, contact, US-person status, records/backup method.
4. Replaced erroneous "KB Objects LLC" with Torchworx LLC on QF-002, QF-007, QF-010 (also [PR #2](https://github.com/jacob-cnc/qms/pull/2) for master).
5. Fixed `convert_md_to_docx.py` footer title bug; regenerated affected DOCX.
6. Wrote `supplier-paperwork/karman/HANDOFF.md` for the next agent.

**PR:** [PR #1](https://github.com/jacob-cnc/qms/pull/1) (draft, kept separate at owner's request).

## 2026-11-05 — Codex (owner review revisions)

Applied all requested QSM-001 wording revisions; removed design/special-process exclusions, retained explosives/flight exclusions, broadened materials scope, revised supplier/customer approval wording and made the manual customer-neutral. Moved Appendix A into a separate QA-1003 submission cross-reference. Updated submission instructions, status and handoff; regenerated corresponding DOCX files and checked content parity. Owner signature and effective date remain pending. Changes committed to the existing basic-QMS feature branch at the owner's request.


## 2026-11-05 — Codex (review corrections)

Fixed the six reported review items, with the owner's exception that the survey cross-reference is an unnumbered courtesy attachment rather than a controlled QMS document. Aligned customer-approved inspection sources; removed We/Our from the survey narrative; corrected the extracted Q8 reference; split explosives and DoD questions, including Q40 and the Q44 explanation field. Removed the static manual page label; converter now adds actual Word page fields for controlled documents, uses the stated revision, and omits empty controlled-document footers on unnumbered documents. Regenerated affected Word copies and verified contents and footer fields.

## 2026-11-05 — Codex (actual part-marking practice)

Reworked WI-008 as draft revision B to use attached green INSPECTED and red REJECTED hang tags, each with QC initials, inspection date and part number. Added customer-specific review/approval and implementation, traceability, safe attachment, reinspection and release controls. Aligned QSM-001 §11 red-tag wording and recorded the pending WI revision in the Master Document List. No approval signature or effective date was invented. Regenerated Word copies and verified tag fields and status wording.


## 2026-11-05 — Codex (WI-008 revision B approval)

Recorded Jacob Honick's explicit instruction to approve WI-008 revision B. Set approval and effective date to 2026-11-05 (America/Los_Angeles), removed draft status, updated the effective Master Document List entry and next review date, removed the pending WI entry, and regenerated matching Word copies. Approval is recorded from the owner's conversation instruction; no handwritten signature was created. Other pending document approvals remain unchanged.


## 2026-11-05 — Codex (simplified in-house calibration draft)

Revised QP-010 revision B draft to allow simple limited-scope comparison with suitable known-good references; retained brief actual-results records, fitness decisions and customer-required certification/traceability/accreditation. Simplified QF-039 and aligned QSM-001 §9. No reference, instrument, calibration result or formal release is asserted by these edits. Regenerated and checked Word copies. Existing proposed tube-specific plans may retain stricter checks until reviewed for the actual job.


## 2026-11-05 — Codex (remove dedicated caliper method)

Removed QF-039 Markdown/Word and active references to it. Generalized in-house calibration/verification to known-good standards without defining values or a prescribed method. Retained customer requirement precedence, equipment suitability and existing QF-020/linked record use. Updated manual, calibration log, master register, related purchasing/training text, handoff, survey/readiness documents, DCR, job plan, measurement register and packet. Historical entries above describe superseded work, not current requirements. No calibration result, reference qualification or approval signature was invented. Regenerated all affected Word copies and audited the repository for active obsolete links.


## 2026-11-05 — Codex (QM-001 scope and standards language)

Applied owner revisions to QM-001: variety-of-industries context, metallic/non-metallic scope, removed §1.3 and the certification-required external-factor bullet. Added explicit no-certification/no-quality-standard-compliance status; standard and clause references are guidance/best-practice only, with actual customer/legal obligations retained. Reworked §§3.1 and 5.3 and related registrar/auditor/responsibility wording to avoid implying existing engagements or assessed conformity. Aligned linked QM-002 policy and the pending document register, and harmonized retention with QSM-001/QP-001. Regenerated and checked Word copies. Both manual/policy revisions remain draft pending release.


## 2026-11-05 — Codex (manual/policy revision B approval)

Recorded the owner's explicit approval of QM-001 and QM-002 revision B, effective 2026-11-05 (America/Los_Angeles). Removed draft status, updated register entries and next review dates, removed pending manual/policy entries, reconciled approval wording and regenerated Word copies. No handwritten signature or operational/certification claim was created. Other pending revisions remain unchanged. Owner requests that subsequent wording changes be presented in chat for approval/rework before application.


## 2026-11-05 — Codex (QF-028 in-house provider wording)

Updated QF-028 as revision B draft: example provider entries now read In-house (example); sample acceptance instruments are explicitly Example — unverified, not In-Cal; reference-only sample is also labeled as an example. Added customer-requirement precedence and a clear pending actual-inventory note. Updated pending register/status and regenerated matching Word copies. QF-030 intentionally unchanged until the owner supplies and confirms the actual QF-028 inventory; the dependency is recorded for follow-up. No actual equipment, calibration, dates or approval is asserted.


## 2026-11-05 — Codex (single-manual consolidation)

Owner requested one accurate quality manual. Consolidated approved QM-001 revision B wording with practical operating controls from the separate basic manual into `00-manual/QM-001_Quality_Manual.md`, revision C draft pending release. Kept approved policy/context/external-service wording, ethics, scope limits, customer-approved sources, hang-tag controls, simplified in-house calibration, records and reviews. Removed competing basic-manual and superseded scope-addendum Markdown/Word files and stale Word lock file; prior versions remain in history. Remapped the separate courtesy attachment (renamed to QA-1003_QM-001_Cross_Reference), survey answers, policy, master register, readiness/DCR/assessment and project/index/handoff/status. Historic entries above retain former names as history only. Generated matching Word copies and audited active references. QF-030 equipment schedule intentionally unchanged pending actual QF-028 inventory. No new operational results, signatures or certification claims were created.


## 2026-11-05 — Codex (consolidated manual revision C approved)

Recorded Jacob Honick's explicit approval of the consolidated single QM-001 revision C, effective 2026-11-05 (America/Los_Angeles). Removed current draft/pending status from the manual and active references; updated the effective register entry, index, project, status, handoff, courtesy attachment and survey working documents. Prior revisions remain historical. Regenerated Word copies and checked release consistency. No handwritten signature, completed implementation, customer approval or certification is asserted. Other pending documents and the QF-028 → QF-030 dependency are unchanged.


## 2026-11-05 — Codex (actual measuring equipment and calibration statement)

Imported all 22 instruments/sets from the owner's uploaded inventory. Applied the user's current instructions over embedded source guidance: assigned new thematic permanent IDs, retaining TW-ME-xxx source IDs as aliases. Recorded all as In-house calibrated — owner reported, dated 2026-11-01 from the owner's reply. Replaced QF-028 examples, synchronized QF-030, added QF-020 opening entries, and updated register/index/status/handoff and job references. Corrected current caliper planning to actual 500-752-20/500-753-20 entries without reassigning historical results. M-1 set details do not establish completion of the proposed certified-minus pin purchase. No readings, operator identity, intervals/due dates, certificates or signatures were invented. Document release remains pending where already pending. Regenerated and checked Word copies.


## 2026-11-05 — Owner interval and pin-class clarification

Recorded TW-PIN-001 as Class ZZ minus. Assigned all 22 assets an owner-directed annual (12-month) interval from 2026-11-01, next due 2027-11-01. Updated register, schedule, calibration log and related working references. Individual pin sizes, increments, numerical tolerances and job suitability are not inferred from class alone; customer requirements take precedence.

