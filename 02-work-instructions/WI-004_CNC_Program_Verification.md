| Field | Value |
|-------|-------|
| Document No. | WI-004 |
| Title | CNC Program Verification and Prove-Out |
| Revision | A |
| Effective Date | 2026-08-06 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# WI-004 CNC Program Verification and Prove-Out

## 1. Purpose

Define the step-by-step process for verifying a new or revised CNC program before it is approved for production use, ensuring the program produces conforming parts without machine crashes, tool collisions, or other hazards.

## 2. Scope

Applies to all CNC programs before first production use on CNC-MILL-001 and CNC-LATHE-001 including:
- Newly written programs (in-house or customer-supplied)
- Revised programs (geometry changes, tooling changes, or process improvements)
- Programs ported from another machine
- Any program that has not been previously proven on the specific machine it will run on

## 3. Required Tools and Equipment

- CNC control with graphics/simulation mode (if available)
- Program listing (printed or on screen for line-by-line review)
- Current revision customer drawing
- Job Traveler (QF-004) with operation details
- Material blank (for first-run prove-out)
- Workholding and tools per setup sheet (same as production setup)
- Feed rate override knob (set to 0% for air cut approach)
- Single block mode capability on the control
- Dial indicator (to verify positions during dry run if needed)
- Measuring instruments for first piece verification per WI-005

## 4. Safety Precautions

- Never prove out a program at full rapid speed on first run. Use reduced rapid override (25% or lower).
- Keep hand on feed hold at all times during first run.
- Verify tool clearance heights are adequate before running — review Z-clearance moves in the program.
- If a crash occurs, immediately press E-stop. Do not attempt to jog away until damage is assessed.
- Never override safety interlocks or door switches during prove-out.
- Remove any unnecessary personnel from the immediate machine area during first run.

## 5. Procedure

### Program Receipt and Review

1. Obtain the program from the approved source (CAM system, customer, or manual programming). Record the source on the Job Traveler.
2. Verify the program filename follows the shop naming convention: `PN-REV-OP-MACHINE` (e.g., `12345-A-OP10-MILL01`).
3. Review the program header comments. Verify they include: part number, revision, operation number, machine, date, programmer name.
4. Perform a line-by-line review of the program looking for:
   - Correct tool numbers matching the tool list
   - Appropriate spindle speeds and feed rates for the material/tool combination
   - Proper coolant on/off commands
   - Safe Z-clearance moves between operations (minimum 0.100" above highest point of workholding)
   - Correct work offset (G54, G55, etc.) matching setup documentation
   - Proper program end (M30 or M02, spindle stop, coolant off)

### Dry Run (Graphics / Air Cut)

5. If the control has graphics simulation mode, run the program in graphics first. Verify tool paths visually match the drawing geometry.
6. Load the program into the control. Set up workholding and tools per the production setup.
7. With NO workpiece in the machine (or with the Z-offset raised 2" above actual), run the program with:
   - Feed rate override at 100%
   - Rapid override at 25%
   - Single block mode ON for the first 10-20 lines to verify initial positioning
8. Observe the tool paths during the air cut. Verify:
   - Tool changes occur without collision
   - Clearance moves provide adequate room above the workholding
   - The program visits features in the expected order
   - No unexpected axis movements occur

### First Run (Single Block)

9. Load the workpiece material (production material or equivalent test blank).
10. Set WCS datum per the production setup procedure (WI-001 or WI-002 as applicable).
11. Set rapid override to 25%. Set feed rate override to 50%.
12. Run the program in single block mode. Press cycle start for each block.
13. Monitor each move carefully. Verify:
    - Each tool approaches the workpiece correctly
    - Cutting depths match program intent
    - No unexpected tool-to-fixture contact
    - Chip load appears reasonable (not excessive deflection or chatter)
14. After verifying initial moves are safe (first tool, first feature), switch to continuous mode with:
    - Rapid override at 50%
    - Feed rate override increasing from 50% toward 100% as confidence builds
    - Hand on feed hold at all times
15. Complete the first part.

### First Piece Inspection

16. Remove the first part. Perform complete first piece inspection per WI-005.
17. Evaluate results:
    - **ALL dimensions in tolerance:** Program APPROVED. Proceed to Step 18.
    - **Minor offset adjustments needed:** Make tool offset corrections, produce a second first piece, inspect again per WI-005. If acceptable, program APPROVED.
    - **Geometry errors (wrong feature location, wrong profile shape):** Program REJECTED. Return to programmer for correction. Do not attempt to fix geometry issues with offsets alone.

### Approval and Storage

18. Record "Program Proved — Approved for Production" on the Job Traveler (QF-004). Include date and operator initials.
19. Save the approved program to the designated storage location (network drive or USB backup per shop policy).
20. Record the program in the Program Register (log of all active programs) with: filename, part number, revision, date proved, machine.
21. If a previous revision of the program exists, archive it (do not delete). Mark archived version clearly with date superseded.

### Revision Control

22. Any change to an approved program (geometry, speeds/feeds, tool paths) requires a new revision letter and re-prove-out per this procedure.
23. Minor offset adjustments during production (tool wear compensation) do NOT require re-prove-out, but must be documented on the Job Traveler.
24. If a program is moved to a different machine, it must be proved out on the new machine per this procedure even if previously approved on another machine.

## 6. Acceptance Criteria

- Program produces a part that passes first piece inspection per WI-005
- No collisions, crashes, or near-misses during prove-out
- All tool paths match drawing geometry and intent
- Cycle time is reasonable for the operation (no excessive air cutting)
- Program header comments are complete and accurate

## 7. Nonconformance Response

If the program cannot produce a conforming part or causes a safety concern:

1. **STOP** — do not attempt additional prove-out runs until the issue is resolved.
2. Tag the program as "UNAPPROVED — DO NOT USE" in the control and storage.
3. Document the issue: what failed, what was observed, what correction is needed.
4. Return the program to the programmer (or CAM source) for correction.
5. If a crash occurred, inspect the machine, tooling, and workholding for damage before any further operation. Report machine damage to Shop Owner per QP-018.
6. Re-start this procedure from Step 1 when the corrected program is received.

## 8. References

- QP-005 — Production Planning and Control
- QP-008 — Nonconforming Product Control
- QP-015 — Configuration Management
- QP-018 — Equipment Maintenance
- QF-004 — Job Traveler / Route Sheet
- QF-005 — In-Process Inspection Record
- WI-001 — CNC Mill Setup and Operation
- WI-002 — CNC Lathe Setup and Operation
- WI-005 — First Piece Inspection

## 9. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-06 | Initial release | Shop Owner |
