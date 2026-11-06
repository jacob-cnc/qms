# Handoff — Karman ASL Self-Survey / Basic QMS (QSM-001)

**Last updated:** 2026-11-05
**Owner:** Jacob Honick, Torchworx LLC (sole owner/employee)
**Working branch:** `karman/basic-qms` — keep SEPARATE; do not merge without the owner's say-so.
**Internal doc — do not send to Karman.**

## 1. Goal

Get Torchworx LLC onto Karman Aerospace & Defense's Approved Supplier List (ASL) as a **Tier 3, uncertified** supplier so a formal PO/contract can be issued for non-ITAR, non-flight, development weld-test titanium tubes. Karman knows Torchworx is not AS9100/ISO 9001 certified and has said that is acceptable for Tier 3.

Deliverables:
1. A short, honest, presentable quality manual Karman can be referred to → **QSM-001**.
2. Accurate answers to Karman's self-survey (form `QA-1003 Supplier Self-Survey_9-15-2025.pdf`, a Systima Technologies form, 7 pages), each pointing to a QSM-001 section.

Guiding rule from the owner: **accurate and honest, best practice, bare minimum.** Never claim certification, compliance, signatures, calibration results, job history or anything not true today. Mark unconfirmed items open rather than guessing.

## 2. Branches and PRs

| Branch | Purpose | State |
|---|---|---|
| `master` | Full 86-doc AS9100 development QMS (draft, Aug 2026) | Unchanged |
| `review/karman-supplier-paperwork` | Survey PDF, assessment, job packet, KMS-001 draft, QP-006/QP-010/QF-020 Rev B drafts, new QF-039 (commit `a677ecd`, made in an earlier cloud session) | Base of PR #1 |
| `karman/basic-qms` | QSM-001 + survey answers + company-name fix + this handoff | **[PR #1](https://github.com/jacob-cnc/qms/pull/1)** (draft, into the review branch). Owner wants it kept separate for now. |
| `fix/torchworx-company-name` | Same KB Objects → Torchworx fix applied to `master`'s QF-002/007/010 | **[PR #2](https://github.com/jacob-cnc/qms/pull/2)** into `master`, open, not merged |

## 3. What to send Karman vs. keep internal

**Send:** `07-basic-qms/QSM-001_Basic_Quality_System_Manual` (signed, exported to PDF by the owner from Word), plus the completed survey PDF and separate `supplier-paperwork/karman/submission/QA-1003_QSM-001_Cross_Reference` attachment.

**Keep internal:** everything under `supplier-paperwork/karman/working/` (Survey-answers-draft, Survey-assessment, Readiness-records, DCR, job plan), this HANDOFF.md, and the 86-doc development set. The development set makes claims that are not yet true (accredited calibration, annually contracted audits, policy posted), which is why QSM-001 exists as a standalone document.

## 4. Key files

- `07-basic-qms/QSM-001_Basic_Quality_System_Manual.md` (+ .docx) — the manual. The separate submission cross-reference maps each survey question → QSM-001 section; Appendix A has been removed from the general manual. QSM-001 governs where it differs from the larger draft QMS, reuses existing QF forms as records, and supersedes draft KMS-001.
- `supplier-paperwork/karman/working/Survey-answers-draft.md` (+ .docx) — every survey field/question with a drafted answer, page-5 "additional information" text, and a pre-send checklist. ⚠ marks = owner must confirm.
- `supplier-paperwork/karman/working/Survey-assessment.md` — question-by-question mapping and evidence needed (accurate vs. the PDF).
- `supplier-paperwork/karman/working/job-packet/` — blank contract review, material lot, traveler, inspection, release/CoC forms for the tube job.
- `supplier-paperwork/karman/working/Titanium-tube-job-plan.md`, `Job-measurement-register.md` — 3.000 ±0.050 in length (calipers); ID 0.194 ±0.001 in for 1 in deep from one end, checked with 0.194 GO / 0.195 NO-GO minus pins (deliberately tighter than drawing, stated as such).
- `03-forms/QF-002`, `QF-007`, `QF-010` — corrected to Torchworx LLC (QF-010 is the CoC Karman will receive).
- `convert_md_to_docx.py` (repo root) — Markdown → DOCX converter. Fixed on this branch: footer showed the wrong title when a table had a "Title" column. Needs `python-docx` (install into a scratch venv, pin the version; don't touch global Python).

## 5. Decisions made in QSM-001 (owner may change)

- **Inspection:** 100% inspection of every characteristic, actual values recorded; no sampling → survey Q16a answered "No" with explanation.
- **Material review:** rework-to-drawing or scrap only. Use-as-is, repair or any deviation requires Karman's written approval.
- **Calibration:** accredited lab, or the limited in-house method recorded on QF-039.
- **Record retention:** 10 years minimum or longer if the contract requires (strictest of the conflicting values in the dev set).
- **ITAR/DFARS:** not ITAR-registered, no ITAR work accepted; NIST SP 800-171 not assessed, so no CUI orders accepted. Page-1 ITAR questions drafted "No" with that explanation — ask the Karman contact whether they prefer "NA".

## 6. Confirmed owner facts (already entered)

- Company: **Torchworx LLC**, 1721 63rd ST SE, Everett, WA 98203. "KB Objects LLC" was an erroneous leftover. The owner doesn't know where it came from. It has been removed everywhere (text and inside DOCX XML) on this branch and on PR #2.
- LLC formed **2025-03-05** (owner wrote "3/05/25"; read as March 5). Owner has run the shop 10+ years.
- Contact: torchworxjacob@gmail.com, 614-670-3079.
- US citizen by birth, no other citizenship ever → "All employees US persons?" = Yes.
- Equipment: CTMACH CQ6133 CNC lathe; MACH3 3040 3-axis CNC mill; Grizzly G0704 manual mill.
- Records: on the shop's local admin computer, backed up to an external HD weekly and at each document change/addition (QSM-001 §13.2). Manual adds an annual test restore. Suggested (not adopted) an offsite/cloud copy.

## 7. Open items — next agent picks up here

Owner input needed:
1. **Website** on the survey: the owner's URL, or "none".
2. **Survey Q7b material certs:** confirm the supplier provides a material cert per order (e.g. McMaster 89055K53).
3. **Address** marked ⚠ confirm on the answer sheet (already used on QF-002/QF-010).
4. **ITAR "No" vs "NA"** wording on the page-1 ITAR questions: ask the Karman contact.
5. Whether this is DoD/CUI work (owner says non-ITAR, non-flight, development).

Owner actions before sending:
6. Sign QSM-001 §17; set **Effective Date** (= signature date, do not backdate; also the Rev A history row).
7. Sign the Code of Conduct acknowledgment on QF-016 (Q8/Q9 only truthfully "Yes" after QSM-001 is signed/adopted).
8. Do one backup test restore so §13.2 is already true.
9. Export signed QSM-001 to PDF from Word (agent can't generate PDF without Word).

Before measuring parts for acceptance (not before sending the survey):
10. Calibrate calipers (lab or QF-039 in-house method); buy certified 0.194/0.195 minus pins and reference length standards. Q10 "calibration system" is honest once adopted, but instruments must be calibrated before use.

Repo housekeeping / known gaps (not fixed, by design or pending owner):
11. Review-branch drafts (QP-006, QP-010, QF-020 Rev B "draft, approval pending") **replace the approved versions** — merging to master before approval loses the approved revs.
12. QM-001 (dev set) still says all calibration goes to an accredited lab, retention 7 yrs, policy posted, audits contracted. Revise alongside QP-010 if the dev set is ever used externally. Not needed for Karman since QSM-001 governs.
13. Committed junk on master: `tmp/` folder and Word lock file `00-manual/~$-001_Quality_Manual.docx`. Remove + `.gitignore` when owner approves.
14. "KB Objects" still exists in old git history; owner was told purging needs a history rewrite + force-push (irreversible). Not requested.
15. Open decision from STATUS.md: keep DOCX in git vs. generate on demand.

## 8. Conventions to follow

- Commit as `jacob-cnc <jacob-cnc@users.noreply.github.com>` (use `git -c user.name=... -c user.email=...`; don't change git config).
- Never push to `master`; feature branch + PR. Run commit and `git push origin <branch>` as **separate** commands (a chained `...; git push` line is blocked by the Kiro Crew safety policy).
- After editing any `.md` that has a `.docx` twin, regenerate the DOCX with `convert_md_to_docx.py` (repo root) and verify the new text is in it.
- Log agent actions in `AGENT-LOG.md`; keep `STATUS.md` as the single source of truth.

## Owner review revisions — 2026-11-05

Applied the owner's review: metallic or non-metallic scope; retain only explosives and flight exclusions; require customer approval for suppliers receiving data and sources for work outside demonstrated competence; use customer-neutral wording and Torchworx LLC throughout QSM-001; revise policy, potential conflicts of interest, product conformity contributions and suitable-equipment wording. Extracted Appendix A to `supplier-paperwork/karman/submission/QA-1003_QSM-001_Cross_Reference.md` (+ DOCX), to attach with the survey. Signature and effective date remain pending. Scope changes do not establish unverified design or special-process capabilities; review actual work before acceptance.


## Review corrections — 2026-11-05

Inspection services now require customer approval; survey narrative uses Torchworx LLC; courtesy attachment Q8 explicitly points to QSM-001. Q40 requires separate DoD applicability and actual DCMA site-survey confirmation; Q41–47 need applicability review, with Q44 answered as an explanation. The cross-reference is a courtesy attachment only: no document number, revision or Master Document List entry is required. Manual pagination uses Word PAGE/NUMPAGES fields; unnumbered documents have no controlled footer. Owner adoption/signature and other factual confirmations remain pending.
