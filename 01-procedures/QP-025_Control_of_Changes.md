| Field | Value |
|-------|-------|
| Document No. | QP-025 |
| Title | Control of Changes |
| Revision | A |
| Effective Date | 2026-08-07 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# QP-025 Control of Changes

## 1. Purpose

Define the process for evaluating, approving, implementing, and verifying changes to product, processes, or suppliers to ensure continued conformity and to meet customer notification requirements.

## 2. Scope

Applies to all changes that could affect product conformity, including customer-initiated drawing revisions, internal process changes, supplier changes, tooling changes, and equipment changes.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Evaluate proposed changes for risk and impact, obtain customer approval when required, implement changes in a controlled manner, trigger re-validation (FAI) when applicable, maintain change records |

## 4. References

- QF-029 — Change Notification Form
- QP-015 — Configuration Management
- QP-022 — First Article Inspection
- QP-024 — Work Transfer Control
- QP-003 — Purchasing and Supplier Management
- AS9100 Rev D Clause 8.5.6 (Control of Changes)

## 5. Definitions

- **Change Trigger:** An event or condition that initiates the change control process (new drawing revision, process improvement, supplier change, equipment replacement, etc.).
- **Risk Assessment:** Evaluation of the potential impact of a change on product conformity, customer requirements, and downstream processes.
- **Re-validation:** Verification (typically via FAI) that the changed process still produces conforming product.

## 6. Procedure

### Change Triggers

1. Initiate the change control process when ANY of the following occur:
   - Customer issues a revised drawing or specification
   - Internal process change is proposed (different machining strategy, new tooling, new fixture, programming change)
   - Change of supplier for raw material or outside processing
   - Change of equipment used for a production operation
   - Change of inspection method or equipment for a critical characteristic
   - Corrective action requires a process change

### Risk Assessment

2. Initiate QF-029 Change Evaluation Record. Document:
   - Description of the proposed change
   - Reason/trigger for the change
   - Affected part numbers, operations, and specifications
3. Assess the risk of the change:
   - Could the change affect product form, fit, or function?
   - Does it affect safety-critical characteristics?
   - Does it require customer notification or approval?
   - Does it trigger FAI per QP-022?
4. Record risk assessment findings on QF-029.

### Approval Authority

5. Changes that do NOT affect product conformity (e.g., fixture material upgrade with same clamping, coolant brand change with same specification): Shop Owner approves internally. Document on QF-029.
6. Changes that COULD affect product conformity: require verification (FAI or documented first-piece) before full production release.
7. Changes that the customer contract requires notification of: obtain customer approval BEFORE implementing the change. Document approval on QF-029.

### Implementation

8. Once approved, update affected documents:
   - Drawing Register (per QP-015) for customer drawing revisions
   - CNC Program Log (per QP-015) for program changes
   - Process plans, routers, or work instructions as applicable
9. Communicate the change to all personnel involved in the affected operations before production resumes.

### Re-Validation / FAI Trigger Assessment

10. Determine if the change triggers FAI per QP-022 criteria:
    - Design change affecting form, fit, or function — FULL FAI
    - Process change that could affect conformity — FAI or documented first-piece
    - Supplier change for material or outside processing — verify material conformity at minimum
11. Perform required re-validation before releasing production quantities.
12. Record re-validation results on QF-029 (reference FAI number if applicable).

### Customer Notification

13. Notify the customer before implementing changes when:
    - Contract or PO requires notification of process/source changes
    - The change affects a special process or customer-approved process plan
    - The change affects safety-critical characteristics
14. Document customer notification and response on QF-029.

### Closure

15. Close QF-029 when: change is implemented, re-validation is complete (if required), and customer approval is documented (if required). Sign and date.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-029 | Change Evaluation Record | At initiation of each change through closure |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |