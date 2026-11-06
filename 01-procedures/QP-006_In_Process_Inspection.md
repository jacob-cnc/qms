| Field | Value |
| --- | --- |
| Document No. | QP-006 |
| Title | In-Process Inspection |
| Revision | B |
| Effective Date | 2026-08-10 |
| Prepared By | Owner |
| Approved By | Jacob Honick, Owner |
| Revision Approval Date | 2026-11-05 |
| Next Review | 2027-08-10 |

---

# QP-006 In-Process Inspection

Standards and clause references are guidance only and do not claim certification or standard compliance. Applicable customer, contractual and legal requirements govern accepted work.

## 1. Purpose

Define the process for performing inspections during production operations to verify conformance at critical stages and detect nonconformances before further value is added to the part.

## 2. Scope

Applies to all in-process inspection activities including first piece inspection, intermediate dimensional checks, and inspection hold points identified on the job traveler.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Perform all in-process inspections. Record results on inspection records. Initiate nonconformance reports when out-of-tolerance conditions are found. Verify measurement equipment is current on calibration. |

## 4. References

- QF-005 — In-Process Inspection Record
- QF-011 — Nonconforming Material Report
- WI-005 — First Piece Inspection
- QP-005 — Production Planning and Control
- QP-008 — Nonconforming Product Control
- QP-010 — Calibration and Measurement Control
- AS9100 Rev D Clause 8.5.1, 8.6

## 5. Definitions

- **First Piece Inspection:** Inspection of the first part produced in a setup to verify the operation will produce conforming product before running the remainder of the batch.
- **Inspection Hold Point:** A mandatory stop in the operation sequence where production cannot continue until inspection is performed and signed off.
- **SPC (Statistical Process Control):** Use of measured data to monitor process stability. Applied when batch sizes and customer requirements warrant.

## 6. Procedure

### First Piece Inspection

1. After completing setup for any machining operation, produce the first piece.
2. Perform first piece inspection per WI-005, measuring all characteristics produced in that operation.
3. Record all measurements on QF-005 In-Process Inspection Record.
4. Compare measured values to drawing tolerances:
   - If all characteristics conform: sign off QF-005, release the setup for production run.
   - If any characteristic is out of tolerance: adjust the setup, produce a new first piece, and re-inspect. Do not run production until first piece passes.
5. For CNC operations: verify program offsets match the first piece measurements before continuing.

### In-Process Checkpoints

6. During production runs, perform dimensional checks at intervals appropriate to the operation:
   - Default: inspect every part for all characteristics produced at that operation.
   - Use a different inspection extent only when specified by the customer or expressly accepted by the customer in writing; record the requirement and plan on the traveler.
   - After any tool change or offset adjustment: re-verify the next piece before continuing.
7. Record checkpoint measurements on QF-005.

### Inspection Hold Points

8. At operations marked as inspection hold points on the job traveler (QF-004):
   - Stop production after completing the operation.
   - Perform full inspection of all characteristics produced up to that point.
   - Record results on QF-005.
   - Sign off the hold point on QF-004 before releasing to the next operation.
9. Do not proceed past a hold point without documented sign-off.

### Statistical Process Control

10. When batch sizes exceed 25 pieces and customer or internal requirements specify SPC:
    - Measure the specified characteristic(s) on each piece unless the customer specifies or approves a different plan in writing. SPC does not replace full acceptance inspection by default.
    - Plot data on X-bar/R chart or individual/moving range chart as appropriate.
    - Investigate any out-of-control condition (point beyond control limits, run of 7, trend of 7).
11. SPC data is recorded on QF-005 or an attached data sheet referenced by the QF-005 number.

### Nonconformance Discovery

12. When any in-process measurement reveals a nonconforming condition:
    - Immediately stop production on that operation.
    - Segregate the nonconforming part(s) and any suspect parts produced since the last good check.
    - Initiate QF-011 Nonconforming Material Report per QP-008.
    - Do not resume production until the cause is identified and corrected.
13. Record the NCR number on QF-005 for traceability.

### Equipment Verification

14. Before performing any in-process inspection, verify that the measurement equipment being used is within its calibration due date per QP-010.
15. If calibration is overdue, do not use the instrument. Select an alternative calibrated instrument or have the equipment calibrated before proceeding.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-005 | In-Process Inspection Record | At first piece, each checkpoint, and each hold point |
| QF-011 | Nonconforming Material Report | When any in-process nonconformance is discovered |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |

## Revision B Approval

Approved 2026-11-05 by Jacob Honick, Owner. Release approved Rev B; correct references and make full inspection the default unless the customer specifies or approves an alternative.
