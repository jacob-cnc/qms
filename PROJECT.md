# Torchworx LLC Quality Management System

**Started:** 2025-07-14  
**Owner:** Jacob Honick (Torchworx LLC)  
**Repo:** https://github.com/jacob-cnc/qms  
**Status:** Active Development

## Purpose

Maintain a practical quality system for Torchworx LLC, a single-member LLC providing precision machining to customers in a variety of industries. QM-001 is the sole quality manual; standards provide guidance and best practice, without any certification or quality-standard compliance claim. Certification remains a separate future goal.

## Scope

### In Scope
- Quality Manual (QM-001 through QM-003)
- 25 Quality Procedures (QP-001 through QP-025)
- 9 Work Instructions (WI-001 through WI-009)
- 38 Quality Forms (QF-001 through QF-038)
- Supporting documents, implementation guides, and registers
- DOCX generation from markdown source
- Cross-reference integrity between all documents

### Out of Scope
- Actual implementation records (job travelers, filled forms, calibration certs)
- Customer-specific flowdown requirements
- NADCAP accreditation documentation
- ITAR/EAR compliance documentation (handled separately)

## Architecture Overview

```
qms/
├── 00-manual/          ← Quality Manual, Policy, Objectives
├── 01-procedures/      ← 25 Quality Procedures (QP-001–QP-025)
├── 02-work-instructions/ ← 9 Work Instructions (WI-001–WI-009)
├── 03-forms/           ← 38 Blank Forms/Templates (QF-001–QF-038)
├── 04-supporting/      ← PO clauses, retention schedule, risk matrix
├── 05-implementation/  ← Guides for implementing the QMS
├── 06-registers/       ← Master Doc List, Drawing Register, NCR/CAR Log
├── completion-reports/ ← Kiro agent build reports + review issues
├── convert_md_to_docx.py  ← DOCX generator
└── PROJECT.md          ← This file
```

Each document exists as `.md` (source of truth) and `.docx` (generated output for shop/audit use).

## Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Source format | Markdown (.md) | Editable, diffable, version-controlled |
| Output format | Word (.docx) | Generated via `convert_md_to_docx.py` |
| Converter | Python + python-docx | `python convert_md_to_docx.py --all` |
| Version control | Git | `main` = approved baseline |
| Standard | AS9100 Rev D (2016) | Incorporates ISO 9001:2015 |
| Standard | AS9102 Rev B | First Article Inspection |

## Key Constraints

- All documents must satisfy AS9100 Rev D clauses 4–10
- Single-person shop: all role assignments to Shop Owner
- Owner self-checks are not independent AS9100 audits; arrange independent reviews when actual requirements call for them
- Apply QM-001 retention rules and the longest applicable contractual/legal period
- DOCX outputs must stay synchronized with markdown source

## Milestones

| # | Milestone | Target Date | Status |
|---|-----------|-------------|--------|
| 1 | Document generation (all 86 docs) | 2026-08-07 | ✅ Complete |
| 2 | PM review + corrections (17 issues) | 2026-08-10 | ✅ Complete |
| 3 | Cross-reference integrity audit | 2026-08-10 | ✅ Complete |
| 4 | DOCX regeneration | 2026-08-10 | ✅ Complete |
| 5 | Git repo initialization | 2026-08-10 | ✅ Complete |
| 6 | Remaining document review (WIs, forms) | TBD | ⬜ Not started |
| 7 | QMS implementation (run processes, generate records) | TBD | ⬜ Not started |
| 8 | Internal audit | TBD | ⬜ Not started |
| 9 | Management review | TBD | ⬜ Not started |
| 10 | Stage 1 audit (registrar) | TBD | ⬜ Not started |
| 11 | Stage 2 audit (certification) | TBD | ⬜ Not started |

## Branching Strategy

- `main` — approved baseline (audit-ready documents)
- `review/*` — review round branches (e.g., `review/round-1-pm-fixes`)
- PRs with change descriptions when review branches merge to main

## Agent Operating Rules

Per the Kiro PM handoff:
- Quick CAN dispatch single-file edits and cross-reference checks autonomously
- Quick SHOULD flag bulk rewrites (>5 files) or structural changes
- Quick MUST NOT modify the constitution without owner approval
- Quick CAN create and merge review branches

## References

- AS9100 Rev D (SAE International, 2016)
- ISO 9001:2015
- AS9102 Rev B (First Article Inspection)
- Kiro PM Handoff: `~/.kiro/steering/qms-pm-handoff-quick.md`
- QMS Constitution: `~/.kiro/steering/qms-constitution.md`
- Project Management Templates: `github.com/jacob-cnc/project-management`

## Single-manual convention

Maintain only `00-manual/QM-001_Quality_Manual.md` as the quality-manual source and its generated DOCX. Supporting policy/objectives, procedures and the courtesy survey cross-reference are not alternate manuals. Do not recreate copies in basic-QMS or customer folders. Prior manual/addendum versions remain in Git history. Consolidated revision C is approved and effective 2026-11-05; other approved documents retain their recorded status.


