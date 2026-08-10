| Field | Value |
| --- | --- |
| Document No. | QM-001 |
| Title | Quality Manual |
| Revision | A |
| Effective Date | 2026-08-10 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# QM-001 Quality Manual

## 1. QMS Scope and Company Information

### 1.1 Company Information

| Item | Detail |
| --- | --- |
| Company Name | Torchworx LLC |
| Address | 1721 63rd ST SE, Everett, WA 98203 |
| Phone | 614-670-3079 |
| Owner / Operator | Jacob Honick |
| Business Type | Sole Proprietorship - Precision CNC and Manual Machining |
| Equipment | 1x CNC Mill, 1x CNC Lathe, 1x Manual Mill |
| Certifications Sought | AS9100 Rev D / ISO 9001:2015 |

### 1.2 Scope of the Quality Management System

This Quality Management System applies to the **precision CNC and manual machining of aerospace components to customer drawings**. The shop manufactures metallic parts using CNC milling, CNC turning, and manual milling processes per customer-supplied drawings, specifications, and purchase order requirements.

**Products and Services Covered:**

- CNC milled components (3-axis)
- CNC turned components (2-axis)
- Manually milled components
- Associated inspection, packaging, and shipping services

**Locations Covered:**

- Single facility at the address above - all operations performed on-site except where contracted services are noted

**Applicable Standards:**

- AS9100 Rev D (EN/JISQ 9100:2016)
- ISO 9001:2015
- Customer-specific requirements as flowed down via purchase orders

### 1.3 Non-Applicable Requirement: Clause 8.3 — Design and Development

**Non-Applicable Requirement:** AS9100 Rev D / ISO 9001:2015 Clause 8.3 (Design and Development of Products and Services)

**Justification:** This organization does not perform design or development activities. All products are manufactured to customer-provided drawings, models, and specifications. The shop has no responsibility for product design, design validation, or design changes. All design authority resides with the customer or their designated design organization.

This determination of non-applicability does not affect the organization's ability or responsibility to provide products that meet customer and applicable statutory/regulatory requirements.

## 2. Context of the Organization

### 2.1 Understanding the Organization and Its Context

The organization operates as a sole proprietorship providing precision machining services to aerospace and defense customers. The context analysis considering internal and external issues affecting the QMS is documented in QF-032 Context Analysis.

**Key Internal Factors:**

- Single-person operation - all roles consolidated
- Three-machine shop providing milling and turning capability
- Capacity limited by single-operator constraint
- Direct control over all processes (no delegation complexity)

**Key External Factors:**

- AS9100 certification required by aerospace customers
- Customer flow-down requirements vary by contract
- Regulatory requirements (FAA, ITAR as applicable)
- Supply chain risks for raw materials and calibration services
- Industry trends toward tighter tolerances and shorter lead times

### 2.2 Understanding the Needs and Expectations of Interested Parties

| Interested Party | Needs and Expectations |
| --- | --- |
| Customers | Conforming product, on-time delivery, traceability, certifications (CoC, FAI), communication |
| Regulatory Bodies | Compliance with applicable airworthiness and export control regulations |
| Suppliers | Clear requirements, timely payment, fair evaluation |
| Calibration Service Providers | Equipment access schedules, clear specifications |
| Certification Body (Registrar) | Maintained QMS, corrective actions closed, management review conducted |

### 2.3 Determining the Scope of the QMS

The scope boundaries are defined in Section 1.2 above. The scope was determined by considering the internal and external issues (2.1), interested party requirements (2.2), and the products and services delivered.

## 3. Quality Policy

The full quality policy is maintained as a standalone controlled document: **QM-002 Quality Policy**.

### 3.1 Quality Policy Statement (Summary)

The Shop Owner is committed to:

1. **Customer Satisfaction** - Meeting or exceeding customer requirements and expectations for quality, delivery, and communication
2. **Conformity to Requirements** - Delivering products that conform to drawings, specifications, and applicable standards
3. **Product Safety** - Ensuring awareness of product safety contribution and maintaining ethical behavior
4. **Continual Improvement** - Continuously improving QMS effectiveness and process capability
5. **Statutory and Regulatory Compliance** - Meeting all applicable legal, regulatory, and certification requirements

### 3.2 Communication and Availability

The Quality Policy is:

- Displayed in the shop (printed and posted)
- Available as a controlled document (QM-002)
- Communicated to all interested parties as appropriate
- Reviewed for continuing suitability during Management Review (QP-012)

### 3.3 Record Retention

Quality records shall be retained for a minimum of 7 years unless customer contract, purchase order, or regulatory requirements specify a longer retention period. Record retention requirements are detailed in QP-001 Document Control. For defense contracts, retain records for the life of the contract plus 3 years or as specified by the contracting authority.

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

All quality procedures referenced by this QMS, organized by AS9100 clause:

| Doc No. | Title | Primary AS9100 Clause |
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

All quality forms/templates used within this QMS:

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

This is a sole proprietorship. The Shop Owner fulfills all management and operational roles. There is no delegation of authority to employees because there are no employees. Certain specialized activities are contracted to qualified external providers.

### 5.2 Roles Fulfilled by Shop Owner

| Role | QMS Responsibilities |
| --- | --- |
| Top Management | Establish quality policy and objectives, ensure QMS integration with business processes, ensure resources are available, promote improvement and risk-based thinking |
| Quality Manager | Maintain the QMS, ensure process conformance, report QMS performance, ensure customer focus throughout the organization |
| Management Representative | Interface with external parties (registrar, customers) on QMS matters, ensure QMS requirements are met |
| Production Operator | Set up and operate CNC Mill, CNC Lathe, and Manual Mill per work instructions and job travelers |
| Inspector | Perform receiving, in-process, and final inspection per procedures; make accept/reject decisions |
| Internal Auditor | Plan and conduct internal audits (NOTE: contracted to external auditor per 5.3 to maintain objectivity) |
| Purchasing / Buyer | Select and evaluate suppliers, issue purchase orders with quality requirements, manage ASL |
| Document Controller | Control document creation, revision, distribution, and obsolescence |
| Calibration Coordinator | Schedule calibration, maintain calibration records, manage OOT conditions |
| Shipping / Receiving | Receive incoming material, verify against PO; package and ship finished product |

### 5.3 Contracted Services

The following activities are contracted to qualified external providers to supplement the Shop Owner's capabilities or to satisfy objectivity requirements:

| Service | Provider Type | Reason for Contracting |
| --- | --- | --- |
| Calibration | Accredited calibration laboratory (ISO/IEC 17025) | Required accreditation; specialized equipment and standards |
| Internal Audit | Qualified AS9100 auditor (contracted annually) | AS9100 Clause 9.2 requires auditor objectivity - cannot self-audit |
| Special Processes | NADCAP-accredited processors (heat treat, plating, NDT) | Specialized processes not performed in-house; customer/spec requirements |
| IT / Backup | IT service provider | System maintenance, data backup verification |

### 5.4 Authority and Communication

**Authority Structure:**

- The Shop Owner has full authority for all QMS decisions including:- Product release and nonconformance disposition
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
- Registrar communication through Management Representative role

### 5.5 Responsibility Matrix

| QMS Process | Shop Owner | Contracted Calibration Lab | Contracted Auditor | Special Process Suppliers |
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
| Calibration (QP-010) | A | R | - | - |
| Internal Audit (QP-011) | A | - | R | - |
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

**Legend:** R = Responsible (does the work), A = Accountable (approves/owns), I = Informed

## 6. References

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

