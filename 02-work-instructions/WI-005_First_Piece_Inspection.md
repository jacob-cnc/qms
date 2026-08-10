| Field | Value |
|-------|-------|
| Document No. | WI-005 |
| Title | First Piece Inspection |
| Revision | A |
| Effective Date | 2026-08-06 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# WI-005 First Piece Inspection

## 1. Purpose

Define the step-by-step process for inspecting the first part produced from any new setup, new program, or new material lot to verify that the machining process produces conforming product before running additional parts.

## 2. Scope

Applies to the first part produced in any of the following situations:
- New setup on CNC-MILL-001 (CNC Mill), CNC-LATHE-001 (CNC Lathe), or MAN-MILL-001 (Manual Mill)
- New or revised CNC program (first run after prove-out per WI-004)
- New material lot (different heat/lot number from previous run)
- Resumption of production after any machine adjustment that could affect dimensions

## 3. Required Tools and Equipment

- Calibrated micrometers appropriate to part size (0-1", 1-2", 2-3", etc.)
- Calibrated digital calipers (6" or 12" as needed)
- Calibrated height gauge (if applicable to part geometry)
- Calibrated bore gauge or telescoping gauges (for ID measurements)
- Calibrated indicators (for runout, concentricity as required)
- Gauge pins, thread gauges (as required by drawing)
- Surface plate (for height gauge and indicator work)
- Customer drawing (current revision — verify against Drawing Register)
- QF-005 In-Process Inspection Record (blank)
- Calculator

## 4. Safety Precautions

- Allow the part to reach ambient temperature before measuring (hot parts from machining will measure oversize). Minimum 15-minute cool-down for parts with tolerances tighter than ±0.001".
- Handle precision instruments by their frames, not measuring surfaces.
- Wipe chips, coolant, and burrs from part surfaces before measuring. Do not blow chips with compressed air toward measurement equipment.
- Verify instrument calibration is current before use (check sticker/label for due date).

## 5. Procedure

1. Remove the first completed part from the machine. Deburr as required per drawing.
2. Clean the part thoroughly — remove all coolant, chips, and residue from measured surfaces.
3. Allow the part to reach ambient temperature (minimum 15 minutes for tight-tolerance work, or verify part is at room temp with a non-contact thermometer).
4. Retrieve the current revision customer drawing. Verify the drawing revision matches the Job Traveler (QF-004) and the Drawing Register.
5. Select a blank QF-005 In-Process Inspection Record. Record job number, part number, operation, machine asset ID, and date in the header.
6. Identify all critical dimensions on the drawing (those with tolerances of ±0.001" or tighter, GD&T callouts, or any dimension flagged as critical/safety by the customer).
7. Measure ALL critical dimensions first. Record each measurement on QF-005 including:
   - Characteristic number (match balloon number if drawing is ballooned)
   - Nominal value and tolerance
   - Actual measured value
   - Instrument used (record asset ID, e.g., ME-003)
   - Pass/Fail determination
8. Measure a representative sample of non-critical dimensions (minimum 5 additional characteristics or 25% of remaining dimensions, whichever is greater).
9. Compare all measured values against drawing tolerances.
10. Make the accept/reject decision:
    - **ALL measurements within tolerance:** First piece ACCEPTED. Sign QF-005 and record "First Piece Approved" on the Job Traveler (QF-004) at the current operation. Proceed with production run.
    - **ANY measurement out of tolerance:** First piece REJECTED. Proceed to Nonconformance Response (Section 7).

## 6. Acceptance Criteria

- All critical dimensions within drawing tolerance
- All measured non-critical dimensions within drawing tolerance
- Surface finish within drawing requirement (visual comparison to roughness standards or measured with profilometer if specified)
- No visible defects: tool marks exceeding surface finish requirement, burrs on finished surfaces, scratches, dents, or damage
- Part matches drawing geometry (no missing features, extra holes, wrong thread)

## 7. Nonconformance Response

If any measurement exceeds tolerance or any acceptance criterion is not met:

1. **STOP** — do not run additional parts.
2. Tag the nonconforming part with a red tag. Move it to the Quarantine Area.
3. Determine if the condition is correctable:
   - **Correctable by adjustment:** Adjust the machine/program, produce a new first piece, and repeat this inspection from Step 1. Scrap or rework the failed part as appropriate.
   - **Not correctable (wrong material, wrong geometry, over-cut):** Initiate QF-011 Nonconforming Material Report per QP-008 Nonconforming Product Control.
4. Do not resume production until a conforming first piece is produced and documented.
5. If a CNC program offset was adjusted, record the adjustment on the Job Traveler (QF-004) for traceability.

## 8. References

- QP-006 — In-Process Inspection
- QP-008 — Nonconforming Product Control
- QP-010 — Calibration and Measurement Control
- QP-015 — Configuration Management
- QF-004 — Job Traveler / Route Sheet
- QF-005 — In-Process Inspection Record
- QF-011 — Nonconforming Material Report
- WI-004 — CNC Program Verification and Prove-Out

## 9. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-06 | Initial release | Shop Owner |
