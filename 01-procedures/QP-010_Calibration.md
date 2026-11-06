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
- **Known-good reference:** A reference with an established size/value and a reasonable basis for trusting it for the intended check, such as a protected master, a previously verified gauge or a part independently measured with suitable equipment. Record its identification, value and basis of confidence. A nominal size, appearance, agreement between two unverified tools or the instrument checking itself is not sufficient.
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

7. Review the customer drawing, purchase order and applicable specifications before choosing the calibration method. Meet all specified requirements, including any certified/traceable standards, accredited laboratory, method, interval, uncertainty or reporting requirements. Obtain written customer approval before departing from a customer requirement. A shop check does not waive these requirements.
7a. Where the customer does not require a more rigorous method, the owner may perform a simple, limited-scope in-house calibration by comparing the instrument with a known-good reference suitable for the actual function, range and product tolerance. Certification or national-standard traceability is not a blanket shop requirement for this route. Do not describe it as accredited, certified or traceable calibration unless that claim is supported.
7b. Identify the instrument and reference; record the reference value and why it is considered known good. Clean both, inspect for damage and allow them to stabilize in the same shop conditions. Check zero where applicable, then compare at representative values near the intended working size. Repeat enough readings to identify inconsistent results; three readings per point are the normal shop minimum. A small, single-range job does not require a full-range calibration.
7c. Set an allowable error before the check based on the instrument specification, the job tolerance and customer requirements. Record actual readings, differences from the reference and pass/fail. Consider reference reliability, resolution, repeatability, contact/alignment and temperature when deciding suitability. A formal uncertainty budget is required only when specified by the customer or needed to substantiate a close measurement decision. Do not use an uncertain result to accept a borderline part; hold it for better measurement.
7d. Use QF-039 for a brief external-jaw caliper check. A short record is sufficient when it identifies the instrument, intended use, reference and basis of confidence, check date, allowable error, actual results, operator, outcome and next due date. Keep as-found results before zero adjustment; record adjustments and repeat checks afterward. Do not invent calibration certificates or results.
7e. Release only the functions and range actually supported by the checks. An outside-jaw check does not qualify inside jaws or depth functions. Check before initial acceptance use and assign a recall interval based on use, condition and history; six months is the starting interval for a new in-house method unless a shorter requirement applies. Review after damage, wear, unstable results or a failed check.
8. Use an appropriate external calibration service when the customer requires it or the shop cannot establish suitable measurement capability. Use an ISO/IEC 17025 accredited laboratory with relevant scope when accreditation is required. Retain the reports and any required certificates. For in-house work, retain the brief check record and any supporting reference evidence; a certificate number is not required if no certificate exists.
8a. Before each inspection session, check condition, zero where applicable and agreement with an appropriate known-good reference. These checks do not extend the due date or qualify untested functions.
9. Reference-only tools used solely for layout may be designated "Reference Only - Not for Acceptance."


### 6.4 Calibration Status Identification

10. Each calibrated instrument receives a calibration sticker showing: instrument ID, date calibrated, date due, and calibration provider or in-house operator.
10a. Label limited-scope instruments with the authorized function/range and record ID as well as calibration/due dates. Use “UNVERIFIED — NOT FOR ACCEPTANCE” until release; “Planned” equipment is not available capability. Register entries marked as examples in blank forms do not establish actual equipment or calibration status.
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

18. File in-house check records, reference evidence and any external certificates by instrument ID.
18a. Apply the same customer-first approach to acceptance pins and other gauges. Record ID, working size/value, reference basis, intended use and recall date. A caliper length check does not qualify a pin or tight-bore decision. When limits are close, establish that actual gauge size, accuracy and the acceptance rule are suitable; obtain dimensional calibration or a more capable method if the shop check cannot establish this. Visual inspection alone does not verify gauge size. Keep certificates and uncertainty data whenever required or supplied.
19. Record each calibration/check event on QF-020 Calibration Log (date, instrument ID, result and check-record reference; certificate number when applicable).
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
| B — draft | 2026-11-05 | Proposed limited-scope in-house checks using suitable known-good references; simple records and customer-required rigor; not effective until owner approval | Pending |

