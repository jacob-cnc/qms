# QMS Review Issues Log

## Summary

| Priority | Count | Status |
| --- | --- | --- |
| CRITICAL | 3 | DONE |
| HIGH | 5 | DONE |
| MEDIUM | 6 | DONE |
| LOW | 3 | DONE |

---

## Issue 001: QM-001 uses "Excluded" instead of "Not Applicable"

- **Document:** QM-001 Quality Manual
- **Section:** 1.3 "Exclusion of Clause 8.3"
- **Problem:** Section heading says "Exclusion of Clause 8.3" and uses the word "Excluded Clause" in the body. AS9100 Rev D (based on ISO 9001:2015) replaced the "exclusion" concept with "not applicable" under Clause 4.3. Using "excluded" is outdated Rev C terminology and will be flagged by auditors immediately.
- **Fix:** Change heading to "Non-Applicable Requirement: Clause 8.3" and replace all instances of "excluded/exclusion" with "not applicable/non-applicable." Update justification wording to match current standard terminology.
- **Priority:** CRITICAL
- **Status:** DONE

## Issue 002: QM-001 has duplicated Section 5

- **Document:** QM-001 Quality Manual
- **Section:** Sections 5.1-5.5 + 6 + 7
- **Problem:** The entire Section 5 (Organizational Structure and Responsibilities), Section 6 (References), and Section 7 (Revision History) are duplicated verbatim — they appear twice in the document. This is a generation artifact from the Kiro agent.
- **Fix:** Remove the duplicated content (second instance of Sections 5, 6, and 7).
- **Priority:** CRITICAL
- **Status:** DONE

## Issue 003: QP-014 Risk Management only addresses Clause 6.1, not 8.1.1

- **Document:** QP-014 Risk Management
- **Section:** Entire document
- **Problem:** The procedure references AS9100 Rev D Clause 6.1 only. AS9100D has TWO distinct risk requirements: Clause 6.1 (strategic/enterprise risk) and Clause 8.1.1 (operational risk). The current procedure blends both concepts without clear separation. The title says "Risk Management" and the scope mentions "operational risks" but it only references Clause 6.1. A separate operational risk process per 8.1.1 (or a clear two-part structure within this document) is needed — auditors specifically look for this distinction.
- **Fix:** Restructured QP-014 with clearly labeled Part A (Strategic Risk, Clause 6.1) and Part B (Operational Risk, Clause 8.1.1). Added Clause 8.1.1 to references. Added job-level risk assessment as a distinct activity.
- **Priority:** CRITICAL
- **Status:** DONE

## Issue 004: QP-015 Configuration Management references wrong AS9100 clause

- **Document:** QP-015 Configuration Management
- **Section:** 4. References
- **Problem:** References "AS9100 Rev D Clause 8.5.2 (Identification and Traceability)" but configuration management is Clause 8.1.2. Clause 8.5.2 is related but is a different requirement. The procedure should reference 8.1.2 as its primary clause mapping.
- **Fix:** Changed reference to "AS9100 Rev D Clause 8.1.2 (Configuration Management)" and added 8.5.2 as a secondary reference.
- **Priority:** HIGH
- **Status:** DONE

## Issue 005: QP-015 Configuration Management missing ECN impact assessment

- **Document:** QP-015 Configuration Management
- **Section:** 6. Procedure
- **Problem:** The procedure covers drawing receipt and CNC program versioning but does NOT address customer Engineering Change Notice (ECN) management. Per AS9100D 8.1.2, the configuration management process must ensure "requirements (including changes) are accounted for in the product configuration."
- **Fix:** Added "Engineering Change Notice (ECN) Management" section and "As-Built Configuration Verification" section.
- **Priority:** HIGH
- **Status:** DONE

## Issue 006: QP-012 Management Review missing mandatory inputs per 9.3.2

- **Document:** QP-012 Management Review
- **Section:** 6.2 Required Inputs
- **Problem:** Missing "feedback from relevant interested parties" as explicit input. Inputs list did not use AS9100D 9.3.2 numbering.
- **Fix:** Re-organized inputs to explicitly match AS9100D 9.3.2 sub-clauses with clause references. Added "feedback from relevant interested parties."
- **Priority:** HIGH
- **Status:** DONE

## Issue 007: QP-022 FAI references "AS9102 Rev C" — verify currency

- **Document:** QP-022 First Article Inspection
- **Section:** 4. References
- **Problem:** References "AS9102 Rev C" which may not be universally adopted. AS9102 Rev B is the more widely recognized current standard.
- **Fix:** Changed to "AS9102 Rev B" with note that customer-specified revision takes precedence (including Rev C per DS/EN 9102:2024 if specified).
- **Priority:** HIGH
- **Status:** DONE

## Issue 008: QP-017 Product Safety clause mapping incorrect in QM-001

- **Document:** QM-001 Quality Manual
- **Section:** 4.2 Procedure Cross-Reference Table
- **Problem:** QP-017 Product Safety mapped to "8.1.1 Operational Risk Management" — should be Clause 8.1.3.
- **Fix:** Corrected to "8.1.3 Product Safety."
- **Priority:** HIGH
- **Status:** DONE

## Issue 009: QP-010 Calibration missing "recall process" requirement

- **Document:** QP-010 Calibration
- **Section:** 6. Procedure
- **Problem:** AS9100D Clause 7.1.5 specifically requires a "process for recall of monitoring and measuring equipment requiring calibration or verification." Not explicitly defined.
- **Fix:** Added Section 6.5a "Calibration Recall Process" defining triggers, physical retrieval, and substitute equipment protocol.
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 010: QP-010 Calibration missing personally-owned equipment

- **Document:** QP-010 Calibration
- **Section:** 2. Scope
- **Problem:** AS9100D explicitly requires personally-owned measuring equipment used for acceptance be in the calibration program.
- **Fix:** Added explicit statement to scope covering personally-owned and customer-furnished equipment.
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 011: QP-003 Purchasing missing GIDEP reporting reference

- **Document:** QP-003 Purchasing and Supplier Management
- **Section:** 6. Procedure, Counterfeit Parts Prevention
- **Problem:** No mention of GIDEP reporting obligation for defense contracts.
- **Fix:** Added Step 11 referencing GIDEP reporting per DFARS 252.246-7007.
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 012: QP-009 Corrective Action missing "similar process" review

- **Document:** QP-009 Corrective Action
- **Section:** 6.5 Effectiveness Verification
- **Problem:** AS9100D 10.2.1 requires determining if similar nonconformities exist or could occur elsewhere. Missing from procedure.
- **Fix:** Added Section 6.4a "Similar Process/Product Review" per AS9100D 10.2.1.
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 013: QP-008 NC procedure missing external provider notification + concession definition

- **Document:** QP-008 Nonconforming Product
- **Section:** 6. Procedure, Customer Notification (Step 8) and Definitions
- **Problem:** Missing external provider notification requirement and "concession" term.
- **Fix:** Added external provider notification to Step 8. Added "Concession" definition to Section 5.
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 014: QP-022 FAI missing "natural or man-made event" trigger

- **Document:** QP-022 First Article Inspection
- **Section:** 6. Procedure, FAI Triggers (Step 1)
- **Problem:** AS9102 trigger for natural/man-made events adversely affecting the manufacturing process was missing.
- **Fix:** Added trigger: "Natural or man-made event that may have adversely affected the manufacturing process."
- **Priority:** MEDIUM
- **Status:** DONE

## Issue 015: QM-001 Quality Manual missing record retention statement

- **Document:** QM-001 Quality Manual
- **Section:** General
- **Problem:** No top-level retention policy stated.
- **Fix:** Added Section 3.3 "Record Retention" with 7-year minimum and defense contract provisions.
- **Priority:** LOW
- **Status:** DONE

## Issue 016: QP-011 Internal Audit does not reference audit criteria

- **Document:** QP-011 Internal Audit
- **Section:** 6.4 Audit Execution
- **Problem:** Per AS9100D 9.2.2, audit criteria must be defined. Not explicitly listed.
- **Fix:** Added explicit audit criteria list (AS9100D requirements, documented procedures, customer/regulatory requirements, quality objectives).
- **Priority:** LOW
- **Status:** DONE

## Issue 017: Multiple documents have inconsistent effective dates

- **Document:** QM-001 (was 2025-07-14, other docs 2026-08-07)
- **Section:** Header metadata
- **Problem:** QM-001 effective date predates all procedures it references.
- **Fix:** Updated QM-001 effective date to 2026-08-10, added revision history entry documenting the review and corrections made.
- **Priority:** LOW
- **Status:** DONE

