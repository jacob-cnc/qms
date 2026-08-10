| Field | Value |
|-------|-------|
| Document No. | QP-010 |
| Title | Calibration and Measurement Control |
| Revision | A |
| Effective Date | 2026-08-07 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
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

7. All calibrations shall be performed by an ISO/IEC 17025 accredited laboratory with scope covering the instrument type and range.
8. Calibration certificates must state: instrument ID, date calibrated, date due, as-found readings, as-left readings, standards used (with traceability), pass/fail determination, and technician signature.
9. Reference-only tools (e.g., steel rules, combination squares used for layout only) may be designated "Reference Only - Not Calibrated" if not used for acceptance decisions.

### 6.4 Calibration Status Identification

10. Each calibrated instrument receives a calibration sticker showing: instrument ID, date calibrated, date due, and calibration lab name.
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

16. When a calibration certificate reports an instrument as out-of-tolerance (as-found condition):
    a. Quarantine the instrument.
    b. Initiate QF-033 Out-of-Tolerance Impact Assessment.
    c. Identify all product inspected with that instrument since the last known good calibration.
    d. Determine if the OOT condition could have caused acceptance of nonconforming product.
    e. If product may be affected, initiate QF-011 NCR per QP-008 and notify affected customers if product was shipped.
    f. Record the assessment results and any actions taken on QF-033.
17. After adjustment or repair, recalibrate and verify the instrument is within tolerance before returning to service.

### 6.7 Records

18. File calibration certificates in the equipment record file, organized by instrument ID.
19. Record each calibration event on QF-020 Calibration Log (date, instrument ID, result, certificate number).
20. Retain calibration records for the life of the instrument plus 3 years after retirement.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-020 | Calibration Log | Each calibration event |
| QF-028 | Measurement Equipment List | Equipment added, retired, or changed |
| QF-030 | Calibration Schedule | Updated monthly and after each calibration |
| QF-033 | Out-of-Tolerance Impact Assessment | When instrument found OOT |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |