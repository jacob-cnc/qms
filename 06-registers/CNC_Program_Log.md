# CNC Program Log

## Instructions

This register tracks all CNC programs created for production use. Update when new programs are created, modified, or superseded. Maintain backup copies per storage requirements below.

**Naming Convention (per QP-015):**
- Format: `[PartNumber]_[Op#]_[Machine]_[Rev]`
- Example: `12345_OP10_MILL_A` = Part 12345, Operation 10, CNC Mill, Revision A
- Example: `67890_OP20_LATHE_B` = Part 67890, Operation 20, CNC Lathe, Revision B

**Revision Control:**
- Increment revision letter (A, B, C...) for any program change
- Mark previous version as "Superseded" in this log
- Do NOT delete superseded programs - move to archive folder
- Always validate (prove-out) new or modified programs before production use per WI-004

---

## Program Register

| Program Name | Part No. | Drawing Rev | Machine | Date Created | Date Modified | Modification Desc | Author | Validation Status | Primary Storage | Backup Location | Notes |
|-------------|----------|-------------|---------|--------------|---------------|-------------------|--------|-------------------|-----------------|-----------------|-------|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |

**Machine codes:** CNC-MILL-001, CNC-LATHE-001

**Validation Status values:**
- Proved-out: First article run successfully, approved for production
- Approved: Released for repeat production use
- Superseded: Replaced by newer revision (retain in archive)
- Draft: Not yet validated, do NOT use for production

---

## Storage Requirements

**Primary storage:** CNC machine controller memory or dedicated shop computer in `CNC_Programs/[Machine]/[Part Number]/` folder structure.

**Backup location:** External USB drive or network backup, updated minimum monthly. Label backup media with date of last update.

**Archive (superseded programs):** Move to `CNC_Programs/Archive/[Part Number]/` with original filename. Do not delete - may be needed for reference or if drawing reverts.

---

## Program Change Process

1. Identify need for change (new drawing revision, optimization, error correction)
2. Create new program file with incremented revision letter
3. Update this register: new entry with current date, mark old as Superseded
4. Validate new program per WI-004 CNC Program Verification (first piece inspection)
5. Upon successful validation, update status to "Proved-out" then "Approved"
6. Archive superseded version
7. If drawing revision drove the change, update Drawing Register simultaneously

---

*Reference: QP-015 Configuration Management, WI-004 CNC Program Verification*