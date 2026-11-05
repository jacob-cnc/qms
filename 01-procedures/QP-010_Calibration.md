| Field | Value |
|-------|-------|
| Document No. | QP-010 |
| Title | Calibration and Measurement Control |
| Revision | B — draft, pending owner release |
| Effective Date | Pending owner release |
| Prepared By | Shop Owner |
| Approved By | Pending |
| Page | 1 of 1 |

---

# QP-010 Calibration and Measurement Control

## 1. Purpose

Define the process for managing measurement equipment to ensure all inspections and measurements are performed with calibrated instruments traceable to national standards.

## 2. Scope

Applies to all measurement and test equipment used to verify product conformance, including micrometers, calipers, gauges, indicators, gauge blocks, and any CMM or optical measurement systems. This includes personally-owned measurement equipment when used for product acceptance decisions, and customer-furnished measurement equipment used in production.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Maintain equipment inventory, schedule calibrations, verify calibration status before use, handle out-of-tolerance conditions, maintain records |
| Contracted Calibration Lab | Perform calibrations per ISO/IEC 17025 accreditation, issue calibration certificates, report out-of-tolerance conditions |

## 4. References

- QF-020 - Calibration Log
- QF-028 - Measurement Equipment List
- QF-030 - Calibration Schedule
- QF-033 - Out-of-Tolerance Impact Assessment
- QP-008 - Nonconforming Product Control
- AS9100 Rev D Clause 7.1.5

## 5. Definitions

- **Calibration:** Comparison of a measurement instrument against a known standard of higher accuracy, with adjustment if necessary, and documentation of results.
- **Calibration Interval:** The time period between scheduled calibrations for a specific instrument.
- **Out-of-Tolerance (OOT):** Condition where an instrument is found to read outside its specified accuracy during calibration.
- **Traceability:** An unbroken chain of comparisons linking an instrument's calibration to national or international standards (NIST).

## 6. Procedure

### 6.1 Equipment Inventory

1. Maintain QF-028 Measurement Equipment List. Each instrument is assigned a unique ID number (engraved or label).
2. Record for each instrument: ID number, description, manufacturer, model, serial number, range, resolution, accuracy, calibration interval, calibration provider, and location.
3. Update QF-028 when equipment is added, retired, or transferred.

### 6.2 Calibration Interval Assignment

4. Assign initial calibration intervals based on:
   - Manufacturer recommendation
   - Frequency of use
   - Criticality of measurements
   - Historical stability
5. Typical intervals: Micrometers and calipers - 12 months; Gauge blocks - 24 months; Indicators - 12 months; Thread gauges - 12 months.
6. Intervals may be adjusted based on calibration history (extend if consistently in-tolerance, reduce if OOT found).

### 6.3 Calibration Requirements

7. Use an ISO/IEC 17025 accredited laboratory with scope covering the instrument type and range when required by the customer/contract, when no approved in-house method exists, or when capability cannot be demonstrated. Otherwise, the owner may authorize a documented, limited-scope in-house calibration using certified traceable standards, a competent operator, appropriate conditions and an evaluated measurement uncertainty. In-house calibration is not accredited calibration. Customer requirements take precedence; obtain written acceptance if an alternate method departs from a customer requirement.
7a. Before authorizing an in-house method, record intended use/range/function, instrument specification, standards and their actual values/uncertainties, method and check points, environmental limits, permissible error, uncertainty/fitness criteria, operator competence and approval. Use QF-039 for the limited external-length caliper method. Blank fields, unknown specifications or missing certificates prevent instrument release.
7b. Reference standards must have certificates identifying the standard, calibration date, measured values, uncertainty with coverage factor, traceability and applicable conditions. Confirm the certificate covers the intended use and assign a justified recall date. A distributor CoC or the word “traceable” alone is insufficient evidence of calibration capability.
7c. A pre-use verification detects changes; it does not extend a calibration due date or establish calibration of untested functions. A passing external-jaw check does not release internal jaws, depth measurement or the entire 0–6 inch range.
7d. For a new in-house method, require initial calibration before acceptance use, pre-use checks each inspection session, and a conservative initial full-method recall no later than 6 months. Shorten for wear, damage, failed checks or heavy use. Review monthly and justify later interval changes using actual history; apply a shorter customer-required interval.
8. Obtain external calibration reports with instrument ID, calibration date, results, uncertainty/traceability, method and provider identification. Record the shop-assigned due date separately if not on the report. For in-house records, include as-found/as-left results, all reference IDs/certificates, environmental conditions, repeat readings, errors, uncertainty/decision rule, authorized scope, result and actual operator/release approval. Record observations before adjustment or zero changes; retain failed results.
9. Reference-only tools (e.g., steel rules, combination squares used for layout only) may be designated "Reference Only - Not Calibrated" if not used for acceptance decisions.

### 6.4 Calibration Status Identification

10. Each calibrated instrument receives a calibration sticker showing: instrument ID, date calibrated, date due, and calibration lab name.
10a. Label limited-scope instruments with the authorized function/range and record ID as well as calibration/due dates. Use “UNVERIFIED — NOT FOR ACCEPTANCE” until release; “Planned” equipment is not available capability. Register entries marked as examples in blank forms do not establish actual equipment or calibration status.
11. Instruments past due or found out-of-tolerance are immediately marked with a red "DO NOT USE" tag and segregated from production use.
12. "Reference Only" instruments are labeled accordingly.

### 6.5 Calibration Scheduling

13. Maintain QF-030 Calibration Schedule showing all instruments with due dates.
14. Review the schedule monthly. Send instruments for calibration at least 2 weeks before the due date to avoid overdue gaps.
15. If an instrument is found overdue (missed its calibration date), quarantine it immediately and do not use it until recalibrated.

### 6.5a Calibration Recall Process

Per AS9100D Clause 7.1.5, a documented recall process is maintained:
16a. The calibration recall is triggered by:
    - QF-030 Calibration Schedule showing an instrument approaching its due date (2-week advance warning)
    - Discovery that an instrument has been damaged, dropped, or exposed to conditions that may affect accuracy
    - Notification from calibration lab of recall or advisory on a standard used
16b. Upon recall trigger, physically retrieve the instrument from use, tag with "AWAITING CALIBRATION" label, and either send to the calibration lab or place in the designated awaiting-calibration area.
16c. If no substitute instrument is available and production requires measurement, halt affected production until calibration is restored or a qualified substitute is sourced.

### 6.6 Out-of-Tolerance Response

16. When calibration, a pre-use check, damage or other evidence indicates an out-of-tolerance or unreliable instrument:
    a. Quarantine the instrument.
    b. Initiate QF-033 Out-of-Tolerance Impact Assessment.
    c. Identify all product inspected with that instrument since the last known good calibration.
    d. Determine if the OOT condition could have caused acceptance of nonconforming product.
    e. If product may be affected, initiate QF-011 NCR per QP-008 and notify affected customers if product was shipped.
    f. Record the assessment results and any actions taken on QF-033.
17. After adjustment or repair, recalibrate and verify the instrument is within tolerance before returning to service.

### 6.7 Records

18. File calibration certificates in the equipment record file, organized by instrument ID.
18a. For certified acceptance pins, record each pin ID, nominal/actual size, class/tolerance, certificate uncertainty, calibration/recall dates and intended GO/NO-GO use. Evaluate actual size and uncertainty against the decision rule; nominal increment is not accuracy. Inspect for wear, damage, contamination and corrosion before each session. Cleanliness/visual checks alone do not recalibrate a pin. Use qualified external calibration unless a separately approved capable in-house method is established.
19. Record each calibration event on QF-020 Calibration Log (date, instrument ID, result, certificate number).
20. Retain calibration records for the life of the instrument plus 3 years after retirement, or longer when QP-001, the applicable job retention period or the contract requires it; apply the longest applicable period.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-020 | Calibration Log | Each calibration event |
| QF-028 | Measurement Equipment List | Equipment added, retired, or changed |
| QF-030 | Calibration Schedule | Updated monthly and after each calibration |
| QF-033 | Out-of-Tolerance Impact Assessment | When instrument found OOT |
| QF-039 | Limited-Scope Caliper Calibration and Verification Record | Initial/recall calibration and linked session checks |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |
| B — draft | 2026-11-05 | Proposed limited-scope in-house calibration, reference/uncertainty criteria, pin control and actual release records; not effective until owner approval | Pending |
