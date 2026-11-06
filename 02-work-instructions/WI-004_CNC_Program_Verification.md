| Field | Value |
| --- | --- |
| Document No. | WI-004 |
| Title | CNC Program Verification and Prove-Out |
| Revision | B |
| Effective Date | 2026-08-10 |
| Prepared By | Owner |
| Approved By | Jacob Honick, Owner |
| Revision Approval Date | 2026-11-05 |
| Next Review | 2027-08-10 |

---

# WI-004 CNC Program Verification

## 1. Purpose and Scope

Verify new, revised or transferred CNC programs before production on CNC-MILL-001 or CNC-LATHE-001. The owner performs programming, review, prove-out and release. Control functions and machine capabilities must be confirmed by the owner; optional simulation or automated hardware is not assumed. Tool changes and tool setting are manual.

## 2. Review

1. Verify the current drawing, purchase order, traveler, machine and program revision. Use the program naming convention in REG-004 CNC Program Log and record the program reference on QF-004.
2. Review the program and setup together for geometry, datums, units, offsets, tool identity, compensation, speeds/feeds, clearances and safe start/end conditions.
3. Confirm programmed tool-change stops match manual changes. Stop motion and spindle before changing tools, secure the correct tool, verify its offset and clearance, and remove setup tools before resuming.
4. Check that program commands match actual machine/control functions. Do not rely on unsupported cycles or automated equipment.

## 3. Prove-Out and First Piece

5. Use suitable available preview, controlled dry-run or stepwise prove-out methods selected by the owner. Verify the complete path against actual stock, fixtures, travel limits and clearances. Do not apply an arbitrary datum shift as a substitute for checking the entire path.
6. Use conservative motion settings and available control functions. Stay ready to stop motion; keep clear of moving axes and rotating tools and do not bypass safeguards.
7. Produce a first piece and inspect all characteristics produced by the operation under WI-005. Correct and repeat verification when needed. Production is not released until the program/setup produces an acceptable first piece.

## 4. Release, Changes and Records

8. Record program prove-out approval, date and owner initials on QF-004 and update REG-004. Keep the program associated with the correct drawing revision and machine.
9. Archive superseded programs and back up approved programs under QP-001 and SUP-003: weekly and whenever programs or records are added or changed; test retrieval at least annually.
10. Re-verify program changes and programs moved to another machine before production. Record routine wear-offset adjustments on the traveler and verify their effect before continuing.
11. If a program cannot produce conforming product or creates a safety concern, stop, mark the program unapproved, correct it and repeat verification. Control affected parts under QP-008 and machine damage under QP-019.

## 5. References

- QP-001 Document Control; QP-005 Production Planning and Control; QP-008 Nonconforming Product Control
- QP-015 Configuration Management; QP-019 Preventive Maintenance; QP-025 Control of Changes
- QF-004 Job Traveler; WI-001 CNC Mill Setup and Operation; WI-002 CNC Lathe Setup and Operation; WI-005 First Piece Inspection
- REG-004 CNC Program Log; SUP-003 Record Retention Schedule

## 6. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-06 | Initial release | Shop Owner |

## Revision B Approval

Approved 2026-11-05 by Jacob Honick, Owner. Align program prove-out with actual controls, manual tool changes and current program/backup records.
