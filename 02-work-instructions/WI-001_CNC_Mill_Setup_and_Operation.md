| Field | Value |
|-------|-------|
| Document No. | WI-001 |
| Title | CNC Mill Setup and Operation |
| Revision | A |
| Effective Date | 2026-08-06 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# WI-001 CNC Mill Setup and Operation

## 1. Purpose

Define the step-by-step process for setting up and operating CNC-MILL-001 (CNC Mill) to produce conforming parts safely and efficiently, from pre-setup checks through production run to teardown.

## 2. Scope

Applies to all production and prototype work performed on CNC-MILL-001 including:
- New job setups
- Repeat job setups (reload from stored programs)
- Tool changes during a production run
- Any operation requiring workholding changes

## 3. Required Tools and Equipment

- Workholding: vise(s), clamps, fixtures, parallels, soft jaws as required by job
- Cutting tools per tool list on Job Traveler (QF-004) or setup sheet
- Edge finder or electronic touch probe
- Dial indicator and magnetic base (for tramming and part alignment)
- Torque wrench for vise and fixture bolts (where specified)
- Approved cutting fluid (verify correct type for material)
- Personal protective equipment: safety glasses, closed-toe shoes, no loose clothing or jewelry
- Current revision customer drawing and Job Traveler (QF-004)

## 4. Safety Precautions

- Verify machine PM is current before starting any setup (check PM log on machine).
- Never reach into the work envelope while the spindle is running or axes are in motion.
- Secure all workholding firmly — perform pull test on part before running program.
- Remove chuck keys, wrenches, and setup tools from the table before closing doors.
- Keep the machine enclosure door closed during any automatic cycle.
- Verify the correct tool is in each pocket — wrong tool can cause crash and injury.
- Long hair must be tied back. No gloves near rotating spindle.
- Know the location of the E-stop and how to use feed hold.

## 5. Procedure

### Pre-Setup

1. Review the Job Traveler (QF-004) and customer drawing. Confirm material, operation sequence, and required tools.
2. Verify machine PM is current (check log posted on machine). If PM is overdue, notify Shop Owner — do not proceed until PM is completed or authorized per QP-018.
3. Clean the machine table, T-slots, and work envelope of chips and coolant residue from prior job.
4. Verify coolant level and concentration are within range per maintenance schedule.

### Workholding Setup

5. Select workholding per setup sheet or job plan (vise, fixture, clamp arrangement).
6. Mount workholding to the table. Torque fasteners to specified value if documented, otherwise confirm tight with no rock.
7. Indicate/tram the vise or fixture to within 0.0005" of the machine axis (or tighter if specified on drawing).
8. Install soft jaws if required. Machine soft jaws to match part geometry if first use.

### Tool Loading

9. Retrieve tools per the tool list. Verify each tool is correct type, diameter, and length.
10. Load each tool into the appropriate spindle pocket per the tool list. Record tool pocket assignments if not already on setup sheet.
11. Measure tool length offsets using the tool setter or gauge block method. Enter offsets into the control.
12. Verify cutter compensation values (diameter offsets) are correct for each tool.

### Program Loading and Verification

13. Load the CNC program per WI-004. Verify program number matches Job Traveler.
14. Verify the program revision matches the drawing revision (check program header comments).
15. If this is the first run of a new or revised program, perform prove-out per WI-004 before proceeding.

### Datum / Work Coordinate System (WCS) Setting

16. Load a part (or material blank) into the workholding.
17. Pick up the X and Y datum using edge finder or probe. Set the G54 (or specified WCS) X and Y values in the control.
18. Pick up the Z datum on the top of the part (or specified reference surface). Set G54 Z value.
19. Double-check WCS values by jogging to known coordinates and verifying position visually.

### First Piece

20. Run the program to produce the first part. Use single block for the first few lines to verify clearance moves.
21. Upon completion, perform first piece inspection per WI-005. Do not proceed until first piece is accepted.

### Production Run

22. Once first piece is accepted, load the next part and run the program in full auto.
23. Monitor the machine during operation — listen for unusual sounds, check for excessive vibration, verify coolant is reaching the cut.
24. Perform in-process checks per QP-006 at the frequency specified on the Job Traveler (typically every 5th or 10th part, or per control plan).
25. Record in-process measurements on QF-005.

### Teardown and Cleanup

26. When the run is complete or the job is finished, remove the last part and perform final in-process inspection.
27. Remove workholding and return to storage. Wipe down vise/fixture with rust preventive if it will be stored.
28. Remove tools from the spindle pockets if not needed for the next job. Return to tool crib/storage.
29. Clean the machine table, T-slots, and work envelope. Remove chips from the chip tray.
30. Wipe down the machine exterior and verify coolant level for next user.

## 6. Acceptance Criteria

- First piece passes all inspections per WI-005 before production continues
- In-process checks remain within tolerance throughout the run
- No machine alarms or abnormal conditions during operation
- Workholding is secure with no part movement during cycle

## 7. Nonconformance Response

If any part fails inspection or an abnormal condition occurs during the run:

1. **STOP** production immediately.
2. Quarantine suspect parts (any produced since last known-good inspection).
3. If the issue is a dimensional drift that can be corrected by offset adjustment, adjust and produce a new first piece per WI-005 before resuming.
4. If the issue is not correctable (crash, wrong feature, material defect), initiate QF-011 Nonconforming Material Report per QP-008.
5. Record the nonconformance on the Job Traveler (QF-004).

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
