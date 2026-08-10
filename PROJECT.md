# AS9100 Rev D Quality Management System

**Started:** 2025-07-14  
**Owner:** jacob-cnc  
**Repo:** (local — GitHub remote pending)  
**Status:** Active Development

## Purpose

Complete AS9100 Rev D / ISO 9001:2015 Quality Management System documentation package for a sole-proprietor aerospace CNC machine shop, supporting certification by an accredited registrar.

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
- Clause 8.3 (Design & Development) declared non-applicable
- Single-person shop: all role assignments to Shop Owner
- Internal audit requires contracted external auditor (independence)
- Minimum 7-year record retention for quality records
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
