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

