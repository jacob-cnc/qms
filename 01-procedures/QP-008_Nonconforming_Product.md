| Field | Value |
| --- | --- |
| Document No. | QP-008 |
| Title | Nonconforming Product Control |
| Revision | B |
| Effective Date | 2026-08-10 |
| Prepared By | Owner |
| Approved By | Jacob Honick, Owner |
| Revision Approval Date | 2026-11-05 |
| Next Review | 2027-08-10 |

---

# QP-008 Nonconforming Product Control

Standards and clause references are guidance only and do not claim certification or standard compliance. Applicable customer, contractual and legal requirements govern accepted work.

## 1. Purpose

Define the process for identifying, documenting, segregating, and dispositioning nonconforming product to prevent its unintended use or delivery.

## 2. Scope

Applies to all nonconforming material, in-process parts, and finished product discovered at any stage — receiving, in-process, final inspection, or after delivery (customer return).

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Identify, document, segregate, and disposition all nonconforming product. Determine customer notification requirements. Authorize rework to the original requirements; obtain prior written customer approval for repair or use-as-is. |
| External calibration provider, only when used | Report relevant out-of-tolerance conditions for the service supplied; no current laboratory engagement is implied |

## 4. References

- QF-011 — Nonconforming Material Report
- QF-012 — Corrective Action Report (8D)
- QP-009 — Corrective Action
- QP-007 — Final Inspection and Product Release
- QP-023 — Customer Communication and Complaints
- NCR/CAR Log (06-registers/)
- AS9100 Rev D Clause 8.7

## 5. Definitions

- **Nonconformance:** Any condition where product, material, or process output does not meet specified requirements (drawing, specification, purchase order, or procedure).
- **Disposition:** The decision on what to do with nonconforming product (rework, repair, use-as-is, scrap, or return to supplier).
- **Quarantine Area:** The designated, physically marked area in the shop where nonconforming material is segregated pending disposition.
- **Concession:** Written authorization from the customer to accept product that does not conform to specified requirements (use-as-is or repair disposition).

## 6. Procedure

### Identification

1. When a nonconformance is identified at any stage (receiving inspection, in-process, final inspection, or customer return), immediately stop work on the affected part(s).
2. Attach a red **REJECTED** hang tag under WI-008, showing the owner’s QC initials, inspection date and part number. Do not use marker dots or mix rejected parts with conforming product. A yellow **HOLD** tag is permitted for material awaiting verification or documentation; it does not authorize acceptance or shipment.
3. Move the nonconforming part(s) to the Quarantine Area.

### Documentation

4. Initiate QF-011 Nonconforming Material Report (NCR). Assign the next sequential NCR number from the NCR/CAR Log.
5. Record the following on QF-011:
   - Job number, part number, drawing revision, quantity affected
   - Description of the nonconformance (what is wrong and what the requirement is)
   - Discovery point (receiving / in-process / final inspection / customer return)
   - Date discovered

### Disposition

6. Evaluate the nonconformance and select one disposition:
   - **Rework:** Part can be brought into conformance by additional machining or processing within the original drawing requirements.
   - **Repair:** Part can be brought to usable condition but will not fully meet original drawing requirements. Requires customer approval before proceeding.
   - **Use-As-Is:** Part does not meet drawing requirements but is acceptable for the intended function. Requires customer approval (written) before release.
   - **Scrap:** Part cannot be reworked or repaired. Keep the red REJECTED hang tag attached, record the scrap disposition on QF-011 and render the part unusable before disposal. Do not use marker identification.
   - **Return to Supplier:** Nonconformance is attributable to incoming material or outside processing. Initiate supplier notification and return per QP-003 Purchasing and Supplier Management.

7. Record the selected disposition on QF-011. Sign and date as Disposition Authority.

### Customer Notification

8. Notify the customer when ANY of the following apply:
   - Disposition is "Repair" or "Use-As-Is" (requires customer concession/waiver before proceeding)
   - Nonconforming product has already been shipped to the customer
   - The nonconformance involves a safety-critical characteristic
   - Customer purchase order requires notification of nonconformances
   - The nonconformance affects product provided to or received from an external provider (e.g., outsourced special processing) — notify the external provider of the nonconforming condition
9. Record customer notification details on QF-011 (date, method, person contacted, decision received).

### Re-Inspection After Disposition

10. After rework or repair is complete, re-inspect the affected characteristic(s) and any characteristics that could have been affected by the rework/repair operation.
11. Record re-inspection results on the original QF-011 or on a new QF-005 In-Process Inspection Record referencing the NCR number.
12. Only release the part for further processing or shipment after re-inspection confirms conformance (or customer concession is documented for use-as-is/repair).

### Closure

13. When disposition is complete and verified, sign and date the closure section of QF-011.
14. Enter the closure date in the NCR/CAR Log.

### Corrective Action Escalation

15. Initiate a Corrective Action Request (QF-012) per QP-009 Corrective Action when ANY of the following apply:
    - The same or similar nonconformance has occurred more than once (repeat)
    - Nonconforming product escaped to the customer
    - The nonconformance involves a safety-critical characteristic
    - The nonconformance results in significant scrap cost or delivery impact
16. Record the related CAR number on QF-011.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-011 | Nonconforming Material Report | When any nonconformance is identified |
| QF-012 | Corrective Action Request | When escalation criteria in Step 15 are met |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-06 | Initial release | Shop Owner |

## Revision B Approval

Approved 2026-11-05 by Jacob Honick, Owner. Standardize control metadata and annual review, remove fixed page counts and align applicable references and wording.
