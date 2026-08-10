| Field | Value |
|-------|-------|
| Document No. | QP-014 |
| Title | Risk Management (Strategic and Operational) |
| Revision | A |
| Effective Date | 2026-08-07 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# QP-014 Risk Management (Strategic and Operational)

## 1. Purpose

Define the process for identifying, assessing, mitigating, and monitoring risks at both the strategic/enterprise level (AS9100D Clause 6.1) and the operational/job level (AS9100D Clause 8.1.1) to ensure product quality, on-time delivery, and business continuity.

## 2. Scope

Applies to:
- **Part A — Strategic Risks (Clause 6.1):** Organization-wide risks and opportunities affecting the QMS's ability to achieve its intended results.
- **Part B — Operational Risks (Clause 8.1.1):** Process-specific and job-specific risks that could affect product conformity, delivery performance, or customer satisfaction.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Identify risks, perform assessments, implement mitigations, review risk register quarterly, update after triggering events |

## 4. References

- QF-023 - Risk Register
- Risk_Matrix_5x5 (04-supporting/)
- QP-012 - Management Review
- QP-009 - Corrective Action
- AS9100 Rev D Clause 6.1 (Actions to Address Risks and Opportunities)
- AS9100 Rev D Clause 8.1.1 (Operational Risk Management)

## 5. Definitions

- **Risk:** The effect of uncertainty on objectives, expressed as a combination of likelihood of occurrence and severity of consequence.
- **Likelihood:** The probability that a risk event will occur (rated 1-5).
- **Severity:** The magnitude of impact if the risk event occurs (rated 1-5).
- **Risk Priority Number (RPN):** Likelihood x Severity (range 1-25). Used to prioritize mitigation efforts.
- **Mitigation:** Actions taken to reduce either the likelihood or severity of a risk to an acceptable level.

## 6. Procedure

### PART A — Strategic Risk Management (Clause 6.1)

### 6.1 Strategic Risk Identification

1. Identify operational risks by considering:
   - Process risks (machine failure, programming errors, setup errors)
   - Supply chain risks (single-source suppliers, material availability, long lead times)
   - Equipment risks (calibration drift, machine breakdown, tooling failure)
   - Personnel risks (single-operator illness/injury, skill gaps)
   - Customer risks (requirement changes, unclear specifications, payment)
   - External risks (regulatory changes, material cost increases, utility disruption)
2. Document each identified risk on QF-023 Risk Register with: risk ID, description, category, affected process/objective.

### 6.2 Strategic Risk Assessment

3. For each identified risk, assess using the 5x5 matrix (reference Risk_Matrix_5x5 in 04-supporting/):
   - **Likelihood** (1=Rare, 2=Unlikely, 3=Possible, 4=Likely, 5=Almost Certain)
   - **Severity** (1=Negligible, 2=Minor, 3=Moderate, 4=Major, 5=Critical)
4. Calculate Risk Priority Number: RPN = Likelihood x Severity.
5. Categorize risk level:
   - Low (RPN 1-4): Accept, monitor at quarterly review
   - Medium (RPN 5-9): Implement mitigation within 60 days
   - High (RPN 10-15): Implement mitigation within 30 days
   - Critical (RPN 16-25): Immediate action required, do not proceed with affected process until mitigated

### 6.3 Strategic Risk Mitigation

6. For each risk requiring mitigation (Medium and above), define:
   - Mitigation action(s) to reduce likelihood, severity, or both
   - Target completion date
   - Responsible person (Shop Owner)
7. Common mitigation strategies:
   - Elimination: Remove the source of risk
   - Substitution: Replace with lower-risk alternative
   - Engineering controls: Add process controls, fixtures, verification steps
   - Administrative controls: Procedures, training, checklists
   - Contingency planning: Define response if risk event occurs
8. Record mitigation actions on QF-023 Risk Register.

### 6.4 Strategic Risk Mitigation Implementation and Verification

9. Implement planned mitigations by target date.
10. After implementation, re-assess the residual risk (new Likelihood x Severity) and record on QF-023.
11. If residual risk remains Medium or above, define additional mitigations or formally accept the residual risk with documented justification.

### 6.5 Review and Monitoring

12. Review the full Strategic Risk Register quarterly at minimum.
13. Conduct ad-hoc risk assessments when any of the following occur:
    - New customer or new product type
    - New material or process introduced
    - New or changed supplier
    - Nonconformance trend identified (3 or more related NCRs)
    - Significant equipment change or addition
    - External event affecting operations
14. Update risk ratings based on current data (nonconformance trends, delivery performance, supplier performance).
15. Report risk status as a required input at Management Review (QP-012).

### PART B — Operational Risk Management (Clause 8.1.1)

### 6.6 Job-Level Operational Risk Assessment

16. When a new purchase order or job is received, perform an operational risk assessment considering:
    - Is this a new part number or repeat production?
    - Does the job involve material the shop has not previously processed?
    - Are there tight tolerances at or near machine capability limits?
    - Is the delivery timeline compressed, requiring overtime or expedited material?
    - Are special processes required from unfamiliar suppliers?
    - Does the drawing revision differ from the last production run?
    - Are there customer-identified critical/safety characteristics?
17. Document the job risk assessment on the Job Traveler (QF-004) risk field or on a separate job risk assessment note attached to the traveler.
18. For jobs assessed as elevated risk, define additional controls:
    - Increased inspection frequency (100% vs. sampling)
    - First-piece verification hold points
    - Additional setup verification steps
    - Supervisor/peer review of CNC program (if available)
    - Contingency material procurement

### 6.7 Operational Risk Criteria and Acceptance

19. Define acceptable and unacceptable operational risk levels:
    - **Acceptable:** Repeat job, proven material, tolerances within demonstrated capability, standard delivery timeline
    - **Elevated:** New part, new material, tight tolerances, compressed timeline — proceed with additional controls per Step 18
    - **Unacceptable:** Tolerances beyond machine capability, material shop cannot source from approved suppliers, process requirements shop cannot meet — decline the order or negotiate requirements with customer before acceptance
20. Formally accept residual operational risk for each elevated-risk job by sign-off on the traveler.

### 6.8 Communication of Operational Risks

21. Communicate identified operational risks that could affect product conformity to relevant parties:
    - To customer: when risk assessment reveals potential inability to meet requirements
    - To supplier: when incoming material or process quality is critical to risk mitigation
22. Record risk communications on the Job Traveler or in customer/supplier communication logs.

### 6.9 Records

23. Maintain QF-023 Risk Register as a living document, updated at each review (Part A).
24. Maintain job-level risk assessments on travelers or attached notes (Part B).
25. Retain superseded Risk Register versions for audit trail (minimum 3 years).

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-023 | Risk Register | Initial assessment and each quarterly review |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |