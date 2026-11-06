| Field | Value |
| --- | --- |
| Document No. | QP-015 |
| Title | Configuration Management |
| Revision | B |
| Effective Date | 2026-08-10 |
| Prepared By | Owner |
| Approved By | Jacob Honick, Owner |
| Revision Approval Date | 2026-11-05 |
| Next Review | 2027-08-10 |

---

# QP-015 Configuration Management

Standards and clause references are guidance only and do not claim certification or standard compliance. Applicable customer, contractual and legal requirements govern accepted work.

## 1. Purpose

Define the process for controlling drawing revisions, CNC program versions, and configuration status to ensure the correct revision of technical data is used for every job.

## 2. Scope

Applies to all customer drawings, specifications, CNC programs, and related technical data used in the production of machined parts.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Maintain Drawing Register, control CNC program revisions, verify current revision before production, remove obsolete documents from use |

## 4. References

- Drawing Register (06-registers/)
- CNC Program Log (06-registers/)
- QP-025 — Control of Changes
- QP-022 — First Article Inspection
- AS9100 Rev D Clause 8.1.2 (Configuration Management)
- AS9100 Rev D Clause 8.5.2 (Identification and Traceability) — related requirement

## 5. Definitions

- **Configuration Item:** Any drawing, specification, or CNC program that defines product requirements.
- **Drawing Register:** Log that records all active drawings, their current revision, date received, and superseded revision disposition.
- **CNC Program Log:** Register that tracks program file names, revision levels, associated part numbers, and validation dates.

## 6. Procedure

### Drawing Receipt and Verification

1. Upon receipt of a new or revised customer drawing, record in the Drawing Register: part number, drawing revision, date received, source (customer/portal).
2. Compare the received revision against the Drawing Register. If a prior revision exists, mark the prior revision as "SUPERSEDED" with the date.
3. Remove or clearly mark (red "OBSOLETE" stamp) all superseded hard-copy drawings from the shop floor. Move electronic files to an "Archive" folder with read-only permissions.

### CNC Program Naming and Revision Control

4. Name CNC program files using the convention: `PartNumber_OpNumber_RevLetter` (e.g., `12345_OP10_A`).
5. When a program is revised, increment the revision letter and record in the CNC Program Log: part number, operation, old revision, new revision, date, reason for change.
6. Validate revised programs per the original prove-out procedure (first piece inspection at minimum) before production use.
7. Archive prior program revisions in a clearly labeled "Archive" directory. Do not delete prior revisions.

### Configuration Status Accounting

8. Before starting any production job, verify the drawing revision on the Work Order/Router matches the current revision in the Drawing Register.
9. Record the drawing revision and CNC program revision used on the Job Traveler for each operation.
10. If a discrepancy is found (shop floor revision does not match Drawing Register), STOP production and resolve before proceeding.

### Engineering Change Notice (ECN) Management

11. Upon receipt of a customer Engineering Change Notice (ECN) or drawing revision:
    a. Log the ECN in the Drawing Register with: ECN number, date received, affected part numbers, nature of change.
    b. Perform an impact assessment: Is any WIP currently in production to the superseded revision? Are there open purchase orders referencing the old revision? Does the change affect tooling, fixtures, or CNC programs?
    c. Document the impact assessment results and determine the cutover point (effective serial number, lot, or date).
    d. If WIP exists at the old revision, coordinate with the customer: complete to old revision (with customer authorization) or scrap/rework to new revision.
    e. Update CNC programs, fixtures, and inspection criteria as required by the change.
    f. Trigger FAI per QP-022 if the change affects form, fit, or function.
    g. Update the Drawing Register to reflect the new current revision and mark the prior revision as SUPERSEDED.
12. Retain records of all ECN impact assessments and cutover decisions.
13. Report ECN activity at Management Review as part of configuration status reporting.

### As-Built Configuration Verification

14. At final inspection, verify that the as-built configuration (drawing revision produced against, material lot, CNC program revision) matches the required configuration per the purchase order.
15. Record as-built configuration data on the Job Traveler and shipping documentation.

### Periodic Review

16. Quarterly, review the Drawing Register to confirm no obsolete drawings remain in active production areas.
17. Record the review date and findings in the Drawing Register.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| Drawing Register | Drawing Revision Log | On receipt of any new/revised drawing |
| CNC Program Log | Program Revision Log | On creation or revision of any CNC program |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |

## Revision B Approval

Approved 2026-11-05 by Jacob Honick, Owner. Standardize control metadata and annual review, remove fixed page counts and align applicable references and wording.
