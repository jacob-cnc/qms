# Titanium tube — provisional job quality plan

Status: working draft, 2026-11-05. Owner-provided requirements; not a released drawing, completed contract review or inspection record.

## Requirements reported by owner

| Characteristic | Reported requirement | Proposed verification / open issue |
| --- | --- | --- |
| Material | McMaster-Carr 89055K53 (owner-confirmed); material cert and lot traceability expected | Titanium grade/specification and actual cert/lot linkage pending |
| Length | 3.000 ±0.050 in (2.950–3.050 in) | 100% measurement with identified 6 in Mitutoyo calipers; calibration status unresolved |
| OD | 0.250 in stock OD (STK) | Confirm purchased stock tolerance and whether OD is reference/as-supplied; do not invent a ± tolerance |
| Controlled ID | 0.194 ±0.001 in (0.193–0.195 in), extending at least 1 in from the designated end | 100% inspection using certified minus pins under the conservative rule below |
| Remaining ID | Produced with 3/16 in drill; not to exceed 0.195 in | Check upper size bound from the opposite end using the conservative pin rule below; drill size alone is not an acceptance result |
| Other geometry | Owner reports no additional cylindricity, TIR or other requirements | Confirm against agreed customer drawing/order; do not create additional geometric tolerances |

All dimensions in inches. Owner clarified customer wording: “only 1” minimum of ID depth must be tightly controlled to +-.001””. Both ends are accessible. Identify the controlled entry end on the traveler. Confirm stock OD acceptance basis and preserve the actual agreed customer requirements in the job packet.

## Traceability plan — intended practice, not yet demonstrated

Receive the agreed stock against the order and supplier documentation. Preserve McMaster part number, manufacturer/mill lot or heat identifier as provided, certificate identifier, quantity and receiving check. Do not assume the distributor order number alone identifies a material heat.

Assign an internal material-lot ID linked to that evidence. Maintain identification on remaining stock, cut blanks and work containers through machining. Give each part a traceable piece ID (or segregated tray position linked to its inspection record) mapping it to the actual material batch. Record split lots, scrap, quantities and shipments. Avoid permanent part marking unless permitted by the customer. Do not mix unidentified pieces or infer a missing lot. Retain the material cert, traveler, inspection results and shipment/CoC linkage.

## 100% inspection plan

Inspect every part, recording piece ID, material lot, requirement/revision, actual length, ID gauge results and insertion depths, instrument/gauge IDs, date and inspector. Verify clean, deburred and temperature-stable parts and gauges. Do not force pins or use a reading rounded to the acceptance limit without considering measurement capability. Isolate failures and suspect pieces under QP-008.

### Planned pin set and conservative acceptance rule

Owner plans to purchase certified, traceable minus pins at nominal diameters 0.193, 0.194, 0.195 and 0.196 in. Purchase, receipt, certificate review and instrument release are not yet completed. Record each pin ID, actual certified diameter, tolerance/class, working length, certificate and calibration status before use.

- Controlled section lower-bound check: the 0.194 in minus pin must pass freely at least 1 in from the designated end. Verify its certified size and measurement uncertainty support a lower bound above 0.193 in. The 0.193 in minus pin alone cannot establish the minimum bore size.
- Upper-bound check: the 0.195 in minus pin must not enter the functional bore from either end. Exclude only an explicitly permitted entrance chamfer/edge break when defining engagement. Verify certified size and uncertainty support the 0.195 in upper bound. Never force a pin.
- The 0.193 and 0.196 in pins are diagnostic; passing the former or rejecting the latter alone is insufficient acceptance evidence.
- This rule intentionally accepts a narrower range than the drawing permits. A failed conservative screen puts the part on hold for further measurement; it does not automatically establish drawing nonconformance. Do not change drawing limits or sign off an unresolved result.

Pin checks establish bounds over their engagement paths. Use the documented drilling process and checks from both accessible ends as the proposed practical method; do not claim continuous bore mapping or verification of unrequired cylindricity/TIR. Resolve any contradictory results or evidence of process instability before release.

Owner plans to acquire Deltronic pins in 0.0001 in increments for upper/lower limit checks if the customer requires finer gauge increments. Finer increments may also be needed to resolve otherwise conforming parts held by the conservative screen. Gauge increments are not themselves measurement accuracy or uncertainty; select actual certified sizes, tolerances, working length and decision rules for the requirement. This future purchase is not represented as current capability.

## Instrument status and verification proposal

Owner reports Mitutoyo model 509-712-20, 0–150 mm, IP67 calipers without a current external calibration certificate. Model marking, serial number, display resolution, inch-mode capability and manufacturer accuracy are not yet verified. Proposed purchase of certified reference pins or blocks is not yet completed. Gauge-pin supplier traceability and individual calibration evidence must be checked on the actual purchase; a generic CoC does not establish dimensional calibration uncertainty or full traceability.

QP-010 currently requires acceptance instruments to be calibrated by an ISO/IEC 17025 accredited laboratory with suitable scope. Shop reference checks do not satisfy that existing policy. Either obtain suitable external calibration before acceptance use, or develop and approve a controlled revision permitting technically supported in-house calibration where the customer contract allows it. No revision, calibration result or supplier acceptance is implied by this draft.

For this loose length tolerance, a documented external-jaw verification near 3 in is a useful capability check. Zero plus several certified lengths can support an in-house method, but does not alone calibrate all caliper functions/ranges or establish measurement uncertainty. Prefer suitable certified gauge blocks for external length checks; cylindrical pins require attention to alignment/contact. Any future in-house method must define instrument ID and restricted scope, standard IDs/certificates, environmental conditions, cleaning/zeroing, check points/repeats, permissible error, uncertainty/fitness decision, as-found/as-left results, due date and OOT response. Do not claim calibration of inside/depth functions from outside-jaw checks.

## Open before release

- Exact customer drawing/order and material specification/certificate requirements; stock part number 89055K53 confirmed by owner.
- Designated controlled end, stock OD acceptance basis and confirmation of the recorded customer requirements.
- Actual caliper model/resolution/condition and external calibration or approved alternate method.
- Receipt and review of planned pin certificates/classes/working lengths; documented inspection decision rule and any customer-required changes.
- Approved job traveler/inspection sheet, material-lot mapping and actual completed measurements.

The full shop instrument inventory can wait; qualify the instruments actually used on this job first. No physical inspection, calibration, material receipt or supplier submission has been performed by creating this plan.


### Calibration development update — 2026-11-05

QP-010 revision B and QF-039 revision A have now been drafted for limited-scope in-house external-length calibration. They are not effective or evidence of completed calibration. See DCR-2026-11-05-Calibration.md and Job-measurement-register.md. The previous external-only policy is the baseline pending actual release; reconcile any earlier wording here during release. Calipers remain unverified and pins remain planned.
