| Field | Value |
| --- | --- |
| Document No. | QM-001 |
| Title | Quality Manual |
| Revision | B |
| Effective Date | 2026-11-05 |
| Prepared By | Shop Owner |
| Approved By | Jacob Honick, Owner |

---

# QM-001 Quality Manual

**Status and use of standards.** Torchworx LLC is not certified to AS9100, ISO 9001, ISO/IEC 17025, NADCAP or any other quality standard, and does not claim or imply compliance with those standards. References to standards and clause numbers provide guidance and best-practice context only; they are not evidence of certification, full implementation or assessed compliance. Actual customer, contractual and applicable legal requirements remain binding and are reviewed before work is accepted.

This manual and its procedure/form cross-references are a development framework. Their presence does not establish that an activity has occurred or a service provider has been engaged. QSM-001 Basic Quality System Manual defines the current basic operating system and governs where the development documents differ; customer requirements take precedence. Certification is a future goal with no formal process or completion date established.

## 1. QMS Scope and Company Information

### 1.1 Company Information

| Item | Detail |
| --- | --- |
| Company Name | Torchworx LLC |
| Address | 1721 63rd ST SE, Everett, WA 98203 |
| Phone | 614-670-3079 |
| Owner / Operator | Jacob Honick |
| Business Type | LLC - Precision CNC and Manual Machining |
| Equipment | 1x CNC Mill, 1x CNC Lathe, 1x Manual Mill |
| Certification status | None held; no quality-standard compliance claimed. AS9100 / ISO 9001 are future goals only |

### 1.2 Scope of the Quality Management System

This Quality Management System covers precision CNC and manual machining services for customers in a variety of industries. Torchworx LLC machines metallic or non-metallic parts using CNC milling, CNC turning and manual milling to customer-supplied drawings, specifications and purchase order requirements.

**Products and Services Covered:**

- CNC milled components (3-axis)
- CNC turned components (2-axis)
- Manually milled components
- Associated inspection, packaging, and shipping services

**Locations Covered:**

- Single facility at the address above - all operations performed on-site except where contracted services are noted

**Guidance and Best-Practice References:**

- AS9100 Rev D (EN/JISQ 9100:2016), for guidance only
- ISO 9001:2015, for guidance only

These references do not assert certification or compliance. Specific standard provisions become job requirements only when applicable through the customer order, contract or law; such requirements are reviewed and met for that work.

## 2. Context of the Organization

### 2.1 Understanding the Organization and Its Context

The organization operates as a single-member LLC providing precision machining services to customers in a variety of industries. The context analysis considering internal and external issues affecting the QMS is documented in QF-032 Context Analysis.

**Key Internal Factors:**

- Single-person operation - all roles consolidated
- Three-machine shop providing milling and turning capability
- Capacity limited by single-operator constraint
- Direct control over all processes (no delegation complexity)

**Key External Factors:**

- Customer flow-down requirements vary by contract
- Regulatory requirements (FAA, ITAR as applicable)
- Supply chain risks for raw materials and calibration services
- Industry trends toward tighter tolerances and shorter lead times

### 2.2 Understanding the Needs and Expectations of Interested Parties

| Interested Party | Needs and Expectations |
| --- | --- |
| Customers | Conforming product, on-time delivery, traceability, required product records (CoC, FAI when specified), communication |
| Regulatory Bodies | Identification and fulfillment of legal/regulatory requirements applicable to accepted work; no blanket regulatory-compliance claim |
| Suppliers | Clear requirements, timely payment, fair evaluation |
| Calibration Service Providers | Equipment access schedules, clear specifications |
| Potential future certification body | Requirements to be assessed if a formal certification project is undertaken; no registrar engagement or certification audit is claimed |

### 2.3 Determining the Scope of the QMS

The scope boundaries are defined in Section 1.2 above. The scope was determined by considering the internal and external issues (2.1), interested party requirements (2.2), and the products and services delivered.

## 3. Quality Policy

The development-set quality policy is documented in **QM-002 Quality Policy**. The current basic operating policy is in QSM-001 §3.1 and governs where the documents differ.

### 3.1 Quality Policy Statement (Summary)

Torchworx LLC commits to reviewing requirements before accepting work, delivering parts that meet the agreed drawing and purchase order requirements, and communicating problems honestly. This policy is a statement of intent and operating expectations, not a claim of certification, full implementation or compliance with a quality-management standard.

1. **Customer requirements** — Review quality, delivery and communication requirements before work is accepted.
2. **Product conformity** — Inspect against agreed drawings, specifications and job requirements; obtain written customer authorization before any permitted deviation.
3. **Ethics and product safety** — Keep honest records, report concerns and prevent unresolved suspect product from being shipped.
4. **Improvement** — Use feedback, inspection results and reviews to improve shop practices.
5. **Applicable obligations** — Identify and meet customer, contractual and legal requirements that apply to the work. Mention of a standard does not create or imply certification or full-standard compliance.

### 3.2 Communication and Availability

On adoption, the applicable quality policy is made available to persons performing work and communicated as appropriate. Record actual approval, distribution and reviews; this manual does not establish that the policy has been posted or reviewed. QM-002 is an approved development-set policy; QSM-001 defines the current basic operating policy.

### 3.3 Record Retention

Retain quality records for at least 10 years after shipment, or longer when QP-001, the applicable program, customer contract, purchase order or law requires it. Apply the longest applicable period. QSM-001 §13 governs the current basic operating system; do not destroy records while an applicable retention period remains open.

## 4. Process Interaction and Document Cross-Reference

### 4.1 Process Interaction Map

The QMS processes interact as a system. The following map shows the primary process groups and their relationships for this 3-machine shop (CNC Mill, CNC Lathe, Manual Mill):

```
CUSTOMER REQUIREMENTS
        |
        v
+-------------------+     +----------------------+
| CONTRACT REVIEW   |---->| PRODUCTION PLANNING  |
| (QP-002)          |     | (QP-005)             |
+-------------------+     +----------------------+
        |                          |
        v                          v
+-------------------+     +----------------------+     +-------------------+
| PURCHASING &      |---->| PRODUCTION           |---->| IN-PROCESS        |
| SUPPLIER MGMT     |     | (WI-001, WI-002,     |     | INSPECTION        |
| (QP-003)          |     |  WI-003, WI-004)     |     | (QP-006)          |
+-------------------+     +----------------------+     +-------------------+
        |                                                       |
        v                                                       v
+-------------------+                               +-------------------+
| RECEIVING         |                               | FINAL INSPECTION  |
| INSPECTION        |                               | & RELEASE         |
| (QP-004)          |                               | (QP-007)          |
+-------------------+                               +-------------------+
                                                            |
                                                            v
                                                    +-------------------+
                                                    | PACKAGING &       |
                                                    | SHIPPING          |
                                                    | (QP-020, WI-009)  |
                                                    +-------------------+
                                                            |
                                                            v
                                                    CUSTOMER DELIVERY

SUPPORT PROCESSES (feed into all operational processes):
+-------------------+  +-------------------+  +-------------------+
| DOCUMENT CONTROL  |  | CALIBRATION       |  | TRAINING &        |
| (QP-001)          |  | (QP-010)          |  | COMPETENCE        |
+-------------------+  +-------------------+  | (QP-013)          |
                                               +-------------------+
+-------------------+  +-------------------+  +-------------------+
| RISK MANAGEMENT   |  | PREVENTIVE        |  | FOD PREVENTION    |
| (QP-014)          |  | MAINTENANCE       |  | (QP-018)          |
+-------------------+  | (QP-019)          |  +-------------------+
                       +-------------------+

IMPROVEMENT PROCESSES (monitor and correct all processes):
+-------------------+  +-------------------+  +-------------------+
| NONCONFORMING     |  | CORRECTIVE ACTION |  | INTERNAL AUDIT    |
| PRODUCT (QP-008)  |  | (QP-009)          |  | (QP-011)          |
+-------------------+  +-------------------+  +-------------------+
+-------------------+  +-------------------+
| MANAGEMENT REVIEW |  | CUSTOMER          |
| (QP-012)          |  | COMMUNICATION     |
+-------------------+  | (QP-023)          |
                       +-------------------+

```

**Process Interactions Summary:**

- Customer requirements flow in through Contract Review and flow out through Final Inspection/Release
- Purchasing feeds into Receiving Inspection which feeds into Production
- All operational processes are supported by Document Control, Calibration, Training, Risk Management, PM, and FOD Prevention
- Nonconformances and corrective actions provide feedback loops to all processes
- Management Review and Internal Audit provide system-level oversight

### 4.2 Procedure Cross-Reference Table

The following development procedures are cross-referenced to AS9100 clauses for guidance and navigation only. This table does not establish conformity, implementation or compliance with any clause:

| Doc No. | Title | AS9100 Guidance Reference |
| --- | --- | --- |
| QP-001 | Document Control | 7.5 Documented Information |
| QP-002 | Contract Review | 8.2 Requirements for Products and Services |
| QP-003 | Purchasing and Supplier Management | 8.4 Control of Externally Provided Processes |
| QP-004 | Receiving Inspection | 8.4 Control of Externally Provided Processes |
| QP-005 | Production Planning and Control | 8.1 Operational Planning and Control |
| QP-006 | In-Process Inspection | 8.5.1 Control of Production and Service Provision |
| QP-007 | Final Inspection and Release | 8.6 Release of Products and Services |
| QP-008 | Nonconforming Product Control | 8.7 Control of Nonconforming Outputs |
| QP-009 | Corrective Action | 10.2 Nonconformity and Corrective Action |
| QP-010 | Calibration | 7.1.5 Monitoring and Measuring Resources |
| QP-011 | Internal Audit | 9.2 Internal Audit |
| QP-012 | Management Review | 9.3 Management Review |
| QP-013 | Training and Competence | 7.2 Competence |
| QP-014 | Risk Management | 6.1 Actions to Address Risks and Opportunities |
| QP-015 | Configuration Management | 8.1 Operational Planning and Control |
| QP-016 | Counterfeit Parts Prevention | 8.1.4 Counterfeit Part Prevention |
| QP-017 | Product Safety | 8.1.3 Product Safety |
| QP-018 | FOD Prevention | 7.1.4 Environment for the Operation of Processes |
| QP-019 | Preventive Maintenance | 7.1.3 Infrastructure |
| QP-020 | Handling, Storage, Packaging, and Shipping | 8.5.4 Preservation |
| QP-021 | Customer Property | 8.5.3 Property Belonging to Customers or External Providers |
| QP-022 | First Article Inspection | 8.5.1 Control of Production and Service Provision |
| QP-023 | Customer Communication | 8.2.1 Customer Communication |
| QP-024 | Work Transfer | 8.1 Operational Planning and Control |
| QP-025 | Control of Changes | 6.3 Planning of Changes |

### 4.3 Form Cross-Reference Table

The following blank forms/templates are available for development and use as applicable. A listed form is not evidence of a completed activity:

| Doc No. | Title | Associated Procedure |
| --- | --- | --- |
| QF-001 | Contract Review Checklist | QP-002 |
| QF-002 | Purchase Order | QP-003 |
| QF-003 | Receiving Inspection Record | QP-004 |
| QF-004 | Job Traveler | QP-005 |
| QF-005 | In-Process Inspection Record | QP-006 |
| QF-006 | Final Inspection Report | QP-007 |
| QF-007 | FAI Form 1 - Part Number Accountability | QP-022 |
| QF-008 | FAI Form 2 - Product Accountability | QP-022 |
| QF-009 | FAI Form 3 - Characteristic Accountability | QP-022 |
| QF-010 | Certificate of Conformance | QP-007 |
| QF-011 | Nonconforming Material Report | QP-008 |
| QF-012 | Corrective Action Request | QP-009 |
| QF-013 | Internal Audit Checklist | QP-011 |
| QF-014 | Internal Audit Report | QP-011 |
| QF-015 | Management Review Minutes | QP-012 |
| QF-016 | Training Record | QP-013 |
| QF-017 | Supplier Evaluation | QP-003 |
| QF-018 | Supplier Scorecard | QP-003 |
| QF-019 | Approved Supplier List | QP-003 |
| QF-020 | Calibration Log | QP-010 |
| QF-021 | Preventive Maintenance Record | QP-019 |
| QF-022 | Customer Complaint | QP-023 |
| QF-023 | Risk Register | QP-014 |
| QF-024 | Customer Property Log | QP-021 |
| QF-025 | Document Change Request | QP-001 |
| QF-026 | FOD Checklist | QP-018 |
| QF-027 | Equipment List | QP-019 |
| QF-028 | Measurement Equipment List | QP-010 |
| QF-029 | Change Notification | QP-025 |
| QF-030 | Calibration Schedule | QP-010 |
| QF-031 | Suspect/Counterfeit Part Report | QP-016 |
| QF-032 | Context Analysis | QM-001 |
| QF-033 | Out-of-Tolerance Impact Assessment | QP-010 |
| QF-034 | Supplier Audit Checklist | QP-003 |
| QF-035 | Supplier Corrective Action Request | QP-003 |
| QF-036 | Training Matrix | QP-013 |
| QF-037 | Quality Objectives Tracker | QM-003 |
| QF-038 | Improvement Log | QP-012 |

## 5. Organizational Structure and Responsibilities

### 5.1 Organization Overview

This is a single-member LLC. The Owner fulfills all management and operational roles. There is no delegation of authority to employees because there are no employees. External services may be arranged where needed for the accepted work; no provider engagement is established by this manual.

### 5.2 Roles Fulfilled by Shop Owner

| Role | QMS Responsibilities |
| --- | --- |
| Top Management | Establish quality policy and objectives, ensure QMS integration with business processes, ensure resources are available, promote improvement and risk-based thinking |
| Quality Manager | Maintain the QMS, ensure process conformance, report QMS performance, ensure customer focus throughout the organization |
| Management Representative | Interface with customers and any actually engaged external parties on quality matters |
| Production Operator | Set up and operate CNC Mill, CNC Lathe, and Manual Mill per work instructions and job travelers |
| Inspector | Perform receiving, in-process, and final inspection per procedures; make accept/reject decisions |
| Internal Auditor | Coordinate reviews and any independent audits actually required or arranged under 5.3; an owner self-check is not represented as an independent AS9100 audit |
| Purchasing / Buyer | Select and evaluate suppliers, issue purchase orders with quality requirements, manage ASL |
| Document Controller | Control document creation, revision, distribution, and obsolescence |
| Calibration Coordinator | Schedule calibration, maintain calibration records, manage OOT conditions |
| Shipping / Receiving | Receive incoming material, verify against PO; package and ship finished product |

### 5.3 External Services and Reviews

External services are selected for the actual job or business need. This section describes possible arrangements, not existing contracts, completed audits, accreditation or compliance with a quality standard.

| Activity | Approach | Customer and capability considerations |
| --- | --- | --- |
| Calibration / verification | In-house checks using known-good standards where permitted, or an appropriate external service under QP-010 | Meet customer-required methods, traceability, certification and accreditation; no accredited calibration is claimed without evidence |
| Quality reviews / audits | Owner reviews under QSM-001; an independent reviewer or auditor may be engaged when required or specifically arranged | Owner self-checks are not independent audits. No annual auditor contract, AS9100 audit or completed assessment is claimed |
| Special processes | Review capability and any external source before accepting the work | Obtain customer approval where required; use NADCAP-accredited or otherwise qualified sources when the actual contract/specification requires them. No process approval or accreditation is implied |
| IT / backup | Owner-managed storage and backup, with external support if actually arranged | Follow documented practices and customer data requirements; retain evidence of actual backup/retrieval checks. No IT service contract is asserted |

AS9100, ISO 9001 and other standard references are guidance and best-practice resources. If a customer imposes specific requirements, review and satisfy those requirements for the affected work; this does not establish organization-wide standard compliance or certification.

### 5.4 Authority and Communication

**Authority Structure:**

- The Shop Owner manages shop quality decisions within contractual and legal limits, including product release and nonconformance control. Repair, use-as-is or deviations require prior written customer authorization; no customer MRB authority is implied.
- Supplier approval and removal
- Corrective action approval and effectiveness verification
- Process changes and document revisions
- Stop-work authority for quality or safety concerns

**Internal Communication:**

- As a single-person operation, internal communication is inherent
- Documented decisions (NCR dispositions, CARs, management review minutes) serve as the formal record
- QMS changes are effective immediately upon document revision approval

**External Communication:**

- Customer communication per QP-023
- Supplier communication per QP-003
- Communication with a registrar only if a certification project is actually initiated

### 5.5 Responsibility Matrix

| QMS Process | Shop Owner | External Calibration Provider, if used | Independent Auditor, if engaged | Special Process Suppliers, if used |
| --- | --- | --- | --- | --- |
| Document Control (QP-001) | R, A | - | - | - |
| Contract Review (QP-002) | R, A | - | - | - |
| Purchasing (QP-003) | R, A | - | - | - |
| Receiving Inspection (QP-004) | R, A | - | - | - |
| Production Planning (QP-005) | R, A | - | - | - |
| In-Process Inspection (QP-006) | R, A | - | - | - |
| Final Inspection (QP-007) | R, A | - | - | - |
| Nonconforming Product (QP-008) | R, A | I | - | I |
| Corrective Action (QP-009) | R, A | I | - | I |
| Calibration (QP-010) | R, A | R when used | - | - |
| Reviews / audits (QP-011 development reference; QSM-001 current controls) | Coordinate; R, A for owner self-checks | - | R if engaged for an independent audit | - |
| Management Review (QP-012) | R, A | - | - | - |
| Training (QP-013) | R, A | - | - | - |
| Risk Management (QP-014) | R, A | - | - | - |
| Configuration Mgmt (QP-015) | R, A | - | - | - |
| Counterfeit Prevention (QP-016) | R, A | - | - | - |
| Product Safety (QP-017) | R, A | - | - | - |
| FOD Prevention (QP-018) | R, A | - | - | - |
| Preventive Maintenance (QP-019) | R, A | - | - | - |
| Handling/Storage/Shipping (QP-020) | R, A | - | - | - |
| Customer Property (QP-021) | R, A | - | - | - |
| First Article Inspection (QP-022) | R, A | - | - | - |
| Customer Communication (QP-023) | R, A | - | - | - |
| Work Transfer (QP-024) | R, A | - | - | - |
| Control of Changes (QP-025) | R, A | - | - | - |

**Legend:** R = Responsible (does the work), A = Accountable (approves/owns), I = Informed. External assignments apply only when a provider is actually engaged; this matrix is not evidence of a contract or standard compliance.

## 6. References

Quality-standard references below are guidance and best-practice resources only. They do not claim certification or compliance; customer-imposed requirements are reviewed for the applicable job.

- QSM-001 Basic Quality System Manual — current basic operating controls

- QM-002 Quality Policy
- QM-003 Quality Objectives
- QF-032 Context Analysis
- QF-037 Quality Objectives Tracker
- AS9100 Rev D (EN/JISQ 9100:2016)
- ISO 9001:2015

## 7. Revision History

| Rev | Date | Description | Approved By |
| --- | --- | --- | --- |
| - | 2025-07-14 | Initial draft | Shop Owner |
| A | 2026-08-10 | Revised: updated Clause 8.3 non-applicability terminology, added record retention statement, corrected procedure cross-reference table (QP-017 clause mapping), removed duplicate sections, incorporated full procedure and form cross-reference tables | Shop Owner |


Revision B, approved and effective 2026-11-05: broaden industry/material scope; remove §1.3; make guidance-only status explicit; revise policy, external-service and responsibility wording; align calibration and retention with current basic controls. Approved by Jacob Honick, Owner, by explicit instruction in the project conversation. Earlier revision-history entries describe superseded wording.


