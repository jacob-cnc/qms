# KMS-001 — Proposed Karman machining quality scope and controls

> **Superseded 2026-11-05 by QSM-001 Basic Quality System Manual (07-basic-qms/).** Its content is folded into QSM-001. Kept for history only; do not issue.

| Field | Value |
| --- | --- |
| Revision | Draft 0 |
| Prepared | 2026-11-05 |
| Status | Draft for owner review; not effective, not a certification claim |
| Owner approval / effective date | Pending / not established |

## 1. Scope and status

Proposed scope: customer-designed machined parts supporting weld development, described by the owner as non-flight and non-ITAR. Welding, design authority, explosives work, and flight-product approval are not included in this proposed scope. No AS9100, ISO 9001, NADCAP or ISO 17025 certification is held. Certification is a future goal with no formal process or completion date established. Existing AS9100-oriented documents are a development foundation; full compliance and operational implementation have not been demonstrated.

This draft supplements the existing QMS for review. It does not silently replace QM-001, waive existing requirements, change a customer PO, or establish Karman Tier 3 qualification. Conflicts must be resolved in controlled revisions before release. Contract requirements take precedence over this proposed baseline.

## 2. Acceptance and responsibilities

The Shop Owner reviews each RFQ/PO and revision using QF-001 before acceptance: part/drawing revision; material and source; tolerances and inspection capability; quantity/delivery; weld-development use; certs; traceability; packaging; record retention; outside processing; source inspection/FAI; and all referenced quality, cybersecurity and data-handling clauses. Obtain missing documents and resolve conflicting requirements in writing before accepting or performing affected work. Do not assume non-flight or non-ITAR means non-DoD or non-CUI.

The owner may perform production and inspection if the contract permits. No independent inspector, accredited laboratory, outside auditor, IT provider or special-process source is represented as engaged without evidence. Do not accept special processes, welding, regulated data or new scope without a separate capability and requirement review.

## 3. Ethics and product conformity awareness

All persons performing work, including the owner, must record actual results honestly; never falsify measurements, certificates, training or approvals; disclose defects and conflicts of interest; protect customer property and information; and stop work when conformity or safety is uncertain. Prototype or development status does not authorize deviations from the drawing or PO. Each person's contribution to product conformity and safety includes preserving identification, using the correct revision and suitable instruments, reporting errors, and preventing suspect product from being shipped. Record review and understanding on QF-016 before work and after relevant changes. No acknowledgment is pre-completed.

## 4. Purchasing, material and configuration

Use QP-003/004 for source evaluation, approved scope and incoming verification. Before ordering, review the material specification, condition, dimensions, heat/lot traceability, certificates and flowed-down requirements. Customer-furnished material must be identified and checked against supplied evidence; missing required certs are resolved before use. Do not invent traceability or substitute material without authorization.

Maintain job ID, PO and drawing revision, lot/heat and quantity linkage from stock/cut pieces through WIP and shipment. Use identified storage for raw material, WIP, finished and held material and protect parts from damage, corrosion and contamination per QP-020/021. Record revisions and withdraw obsolete job copies per QP-001/015.

## 5. Inspection and release

Proposed low-volume default is 100% verification of applicable drawing/PO acceptance characteristics on every part, using suitable methods. This is not MIL-STD-1916 or another statistical sampling standard. If a characteristic cannot be verified with available equipment, arrange a qualified inspection service or resolve the inspection method with the customer before acceptance. Destructive or special tests require their specified method and frequency; do not promise destructive testing of every delivered part.

Plan characteristic IDs, requirements/tolerances, method, instrument IDs, and actual results by part or traceable lot on QF-005/006. Verify the first piece before continuing, inspect at process hold points and after relevant setup/tool changes, and complete final verification before release. First-piece inspection is not automatically an AS9102 FAI. Follow an AS9102/customer FAI requirement if actually flowed down.

Only acceptance instruments with documented suitability and current calibration under QP-010 may be used. Maintain QF-028/030 and certificates. Quarantine overdue/damaged/OOT instruments and assess affected product per QF-033.

For failed characteristics, stop and identify/segregate suspect parts under QP-008. The owner may authorize rework to the original requirements and reinspect. Repair or use-as-is requires written customer/design-authority authorization before proceeding or release; the owner has no delegated customer MRB authority. Preserve the authorization in the job file. Notify the customer of discovered delivered nonconformance.

Review the traveler, inspections, material/processing certs and resolved NCRs before signing QF-006 release and QF-010 CoC. State only verified conformity and document any authorized deviation. Preserve the job packet; do not sign blank records.

## 6. Tooling records, preservation and tracking

Assign an ID to each job-specific or customer-owned fixture, gauge or production tool affecting conformity. Maintain a tooling register with ID, description, owner, applicable job/part/revision, location, condition, inspection/maintenance requirements, last check, restrictions and return/disposition. Link setup information and CNC program revision in the job packet. General consumable cutters may be controlled through setup/tool lists rather than individual asset records.

Before use, check identity/revision, condition, cleanliness and suitability; record the check in the traveler. Protect stored tooling against corrosion, damage and mix-up. Tag and isolate damaged or suspect tooling, assess affected work, and obtain customer direction before modifying, disposing of, or repairing customer-owned items. Record issue, return, maintenance and disposition. Measuring tooling also falls under QP-010.

## 7. Records and preventive/corrective action

Resolve existing retention conflicts before release. Pending resolution, do not destroy records; preserve the longest applicable existing, contractual or legal period. Keep job and tooling records indexed by job/asset and customer, with controlled access and backups. Record actual storage location, backup method, owner and recovery check; Git alone is not evidence that signed records or certificates are backed up. Provide authorized customer/customer-representative/government access as contractually required, protecting unrelated customer data.

Use QP-014/QF-023 to review risks before the first job and significant changes. Record preventive actions, owner, target date and verification. Use QP-009/QF-012 when actual issues warrant corrective action: containment, cause, corrective action, similar-work impact and effectiveness. A blank form is not a completed CAR; a simulation must be labeled as a simulation.

## 8. Adoption gate

Before this draft is issued as effective: confirm customer scope/flowdowns; resolve baseline conflicts; revise impacted documents under QP-001/QF-025; obtain actual owner approval and effective date; update the Master Document List; issue matching DOCX copies; and complete readiness evidence in Readiness-records.md. Any customer-requested deviation or alternate baseline needs explicit customer acceptance.


### Calibration development update — 2026-11-05

QP-010 revision B and QF-039 revision A have now been drafted for limited-scope in-house external-length calibration. They are not effective or evidence of completed calibration. See DCR-2026-11-05-Calibration.md and Job-measurement-register.md. The previous external-only policy is the baseline pending actual release; reconcile any earlier wording here during release. Calipers remain unverified and pins remain planned.
