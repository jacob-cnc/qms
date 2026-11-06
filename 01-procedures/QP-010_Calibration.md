| Field | Value |
|-------|-------|
| Document No. | QP-010 |
| Title | Calibration and Measurement Control |
| Revision | B — draft, pending owner release |
| Effective Date | Pending owner release |
| Prepared By | Shop Owner |
| Approved By | Pending |

---

# QP-010 Calibration and Measurement Control

## 1. Purpose

Define the process for managing measurement equipment to ensure equipment used to accept product is suitable for the job and checked against known-good references. Customer-specified calibration, certification and traceability requirements take precedence.

## 2. Scope

Applies to all measurement and test equipment used to verify product conformance, including micrometers, calipers, gauges, indicators, gauge blocks, and any CMM or optical measurement systems. This includes personally-owned measurement equipment when used for product acceptance decisions, and customer-furnished measurement equipment used in production.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Maintain equipment inventory, schedule calibrations, verify calibration status before use, handle out-of-tolerance conditions, maintain records |
| External Calibration Provider (when used) | Meet applicable customer and job requirements, provide required reports/certificates and report out-of-tolerance conditions |

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
- **Traceability:** A documented chain of calibrations linking a measurement to recognized standards, with associated measurement uncertainty. Required when specified by the customer or other applicable requirements; not claimed for a shop check without supporting evidence.

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

7. Customer drawing, purchase order and specification requirements govern calibration and measurement control. Meet any required certification, traceability, accreditation, method, interval or reporting requirements. Obtain written customer approval before using an alternative to a customer requirement.
8. Where customer requirements permit, the owner may perform in-house calibration or verification using known-good standards considered suitable for the intended work. The owner selects a practical approach appropriate to the equipment and job; this procedure does not prescribe a dedicated form, fixed reference values, check points, repeat count or calculation method.
9. Record the activity, date, instrument, result and person performing the check in QF-020 or a linked equipment/job record. Set the next due date as appropriate to use, condition, history and customer requirements. Keep any evidence or reports required by the customer.
9a. Use an appropriate external service when required by the customer or when suitability cannot be established in-house. Do not claim certified, accredited or traceable calibration without supporting evidence.
9b. Check equipment condition before use. Remove damaged, unreliable or overdue equipment from acceptance use and assess affected product under QF-033. Do not accept product where measurement suitability is unresolved.
9c. Tools used solely for layout may be designated "Reference Only - Not for Acceptance."


### 6.4 Calibration Status Identification

10. Identify calibration status on the instrument or through its linked equipment record, including instrument ID, date checked, due date and provider or in-house operator.
10a. Identify any use restrictions in the equipment record or on the instrument. Planned or unverified equipment is not represented as available acceptance capability. Example register entries do not establish actual status.
11. Instruments past due or found out-of-tolerance are immediately marked with a red "DO NOT USE" tag and segregated from production use.
12. "Reference Only" instruments are labeled accordingly.

### 6.5 Calibration Scheduling

13. Maintain QF-030 Calibration Schedule showing all instruments with due dates.
14. Review the schedule monthly. Arrange in-house checks or send instruments for external calibration at least 2 weeks before the due date to avoid overdue gaps.
15. If an instrument is found overdue (missed its calibration date), quarantine it immediately and do not use it until recalibrated.

### 6.5a Calibration Recall Process

Maintain the following recall process:
16a. The calibration recall is triggered by:
    - QF-030 Calibration Schedule showing an instrument approaching its due date (2-week advance warning)
    - Discovery that an instrument has been damaged, dropped, or exposed to conditions that may affect accuracy
    - Notification from calibration lab of recall or advisory on a standard used
16b. Upon recall trigger, physically retrieve the instrument from use, tag with "AWAITING CALIBRATION" label, and either arrange the approved in-house check or send to the required calibration provider.
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

18. Keep calibration and verification records by instrument ID, including external reports or certificates when required or supplied.
18a. Apply the same customer requirements and suitability review to acceptance gauges and pins. Record their status and any restrictions in equipment or job records.
19. Record each calibration or verification event on QF-020 or a linked equipment/job record. Include certificate references only where applicable.
20. Retain calibration records for the life of the instrument plus 3 years after retirement, or longer when QP-001, the applicable job retention period or the contract requires it; apply the longest applicable period.

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
| B — draft | 2026-11-05 | Proposed general in-house calibration/verification using known-good standards and existing records; dedicated caliper form removed; customer requirements govern; approval pending | Pending |


