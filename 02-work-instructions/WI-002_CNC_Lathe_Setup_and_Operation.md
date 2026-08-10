| Field | Value |
|-------|-------|
| Document No. | WI-002 |
| Title | CNC Lathe Setup and Operation |
| Revision | A |
| Effective Date | 2026-08-06 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# WI-002 CNC Lathe Setup and Operation

## 1. Purpose

Define the step-by-step process for setting up and operating CNC-LATHE-001 (CNC Lathe) to produce conforming turned parts safely and efficiently, from pre-setup checks through production run to teardown.

## 2. Scope

Applies to all production and prototype turning operations performed on CNC-LATHE-001 including:
- New job setups (chuck work and collet work)
- Repeat job setups from stored programs
- Operations requiring jaw changes, collet changes, or soft jaw boring
- Bar work and chucking work

## 3. Required Tools and Equipment

- Workholding: 3-jaw chuck with hard jaws, soft jaws, collets, or collet chuck as required
- Cutting tools per tool list on Job Traveler (QF-004) or setup sheet
- Tool touch-off gauge or reference surface for tool offsets
- Dial indicator and magnetic base (for indicating stock and checking runout)
- Chuck key (if manual-tightening chuck)
- Jaw boring bar (if boring soft jaws)
- Approved cutting fluid (verify correct type for material)
- Chip hooks and brushes (never remove chips by hand)
- Personal protective equipment: safety glasses, closed-toe shoes, no loose clothing or jewelry
- Current revision customer drawing and Job Traveler (QF-004)

## 4. Safety Precautions

- Verify machine PM is current before starting setup (check PM log on machine).
- Never reach toward rotating workpiece or chuck — entanglement injuries are severe.
- Remove chuck key immediately after use. Never leave it in the chuck.
- Verify workpiece is secure before spinning — do a low-RPM test spin and check for wobble.
- Keep hands away from chip stream. Use chip hooks to remove stringy chips only when spindle is stopped.
- Ensure tailstock or steady rest is locked if in use — part ejection risk if loose.
- Long hair must be tied back. No gloves when working near rotating spindle. No loose sleeves.
- Know the location of the E-stop and feed hold.
- Verify the correct tool is in each turret station before running.

## 5. Procedure

### Pre-Setup

1. Review the Job Traveler (QF-004) and customer drawing. Confirm material, operation sequence, and required tools.
2. Verify machine PM is current. If overdue, notify Shop Owner — do not proceed until completed or authorized per QP-018.
3. Clean the chuck face, bore, and turret of chips and debris from prior job.
4. Verify coolant level and concentration are within range.

### Workholding Setup

5. Select workholding per setup sheet (hard jaws, soft jaws, collet, or fixture).
6. If soft jaws are required, mount soft jaw blanks and bore to the part OD or ID dimension plus appropriate clearance. Verify grip diameter with a test piece or ring gauge.
7. If using a collet chuck, install correct collet size for the bar/part diameter.
8. Indicate stock runout: mount a piece of stock and indicate OD with a dial indicator. Runout must be within 0.001" TIR (or tighter if drawing requires).
9. Set chuck pressure to appropriate value for the part (avoid over-clamping thin-wall parts, avoid under-clamping heavy cuts).

### Tool Loading

10. Retrieve tools per the tool list. Verify each tool type, insert grade, and orientation.
11. Load each tool into the correct turret station per the tool list.
12. Touch off each tool to the reference surface (face for Z, OD for X). Enter geometry offsets into the control.
13. Verify tool nose radius compensation values are correct for each finishing tool.

### Program Loading and Verification

14. Load the CNC program per WI-004. Verify program number matches Job Traveler.
15. Verify program revision matches drawing revision (check program header comments).
16. If first run of a new or revised program, perform prove-out per WI-004.

### Datum Setting (Face and X)

17. Load the workpiece into the chuck. Verify proper seating and grip.
18. Face the part to establish Z-zero reference. Set G54 Z offset.
19. Turn a test diameter, measure, and set G54 X offset based on the measured value vs. programmed value (diameter mode).
20. Verify datum by jogging to a known position and checking with an indicator or caliper.

### First Piece

21. Run the program to produce the first part. Use single block for initial moves to verify clearance and tool paths.
22. Perform first piece inspection per WI-005. Do not continue until first piece is accepted.

### Production Run

23. Once first piece is accepted, load the next workpiece and run in full auto.
24. Monitor the machine — listen for chatter, verify chip evacuation, check coolant delivery.
25. Perform in-process checks per QP-006 at the frequency specified on the Job Traveler.
26. Record measurements on QF-005. Watch for trends (e.g., diameter growing as insert wears — adjust offset as needed).

### Teardown and Cleanup

27. When the run is complete, remove the last part and perform final in-process inspection.
28. Remove tools from the turret if not needed for the next job. Return to tool storage.
29. Remove workholding if changing setup. Wipe chuck face and bore with rust preventive if storing.
30. Clean the machine — clear chip pan, wipe slides, verify coolant level for next user.

## 6. Acceptance Criteria

- First piece passes all inspections per WI-005 before production continues
- In-process checks remain within tolerance throughout the run
- Chuck runout verified within specification before first cut
- No machine alarms, chatter, or abnormal conditions during operation

## 7. Nonconformance Response

If any part fails inspection or an abnormal condition occurs:

1. **STOP** production immediately.
2. Quarantine suspect parts produced since last known-good inspection.
3. If correctable by offset adjustment (wear, tool pressure), adjust and produce a new first piece per WI-005.
4. If not correctable (crash, wrong feature, material defect, chuck slip), initiate QF-011 per QP-008.
5. Record the nonconformance on the Job Traveler (QF-004).
6. If a chuck slip occurred, re-indicate runout and verify workholding before resuming any operation.

## 8. References

- QP-005 — Production Planning and Control
- QP-006 — In-Process Inspection
- QP-008 — Nonconforming Product Control
- QP-018 — Equipment Maintenance
- QF-004 — Job Traveler / Route Sheet
- QF-005 — In-Process Inspection Record
- QF-011 — Nonconforming Material Report
- WI-004 — CNC Program Verification and Prove-Out
- WI-005 — First Piece Inspection

## 9. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-06 | Initial release | Shop Owner |
