| Field | Value |
|-------|-------|
| Document No. | QP-005 |
| Title | Production Planning and Control |
| Revision | A |
| Effective Date | 2026-08-07 |
| Prepared By | Shop Owner |
| Approved By | Shop Owner |
| Page | 1 of 1 |

---

# QP-005 Production Planning and Control

## 1. Purpose

Define the process for planning, scheduling, and controlling production operations to ensure parts are manufactured in a controlled sequence with full traceability.

## 2. Scope

Applies to all machining operations performed on the three CNC machines in the shop, including operation sequencing, job traveler preparation, scheduling, and in-process traceability.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| Shop Owner | Plan operations, create job travelers, schedule work across machines, maintain traceability records, and ensure production proceeds per the approved plan. |

## 4. References

- QF-004 — Job Traveler / Route Sheet
- QF-005 — In-Process Inspection Record
- QP-002 — Contract Review
- QP-006 — In-Process Inspection
- QP-015 — Configuration Management
- QP-014 — Risk Management (operational risk assessment per AS9100D Clause 8.1.1)
- WI-004 — CNC Program Verification and Prove-Out
- AS9100 Rev D Clause 8.5.1

## 5. Definitions

- **Job Traveler:** The controlled document that accompanies the part through all production operations, recording what was done, by whom, and when.
- **Operation Sequence:** The planned order of manufacturing steps required to produce a conforming part from raw material to finished product.

## 6. Procedure

### Job Planning

1. After contract review acceptance (QP-002), create a production plan for the job.
1a. Perform a job-level operational risk assessment per QP-014 Part B. Document risk factors on the Job Traveler (new part, new material, tight tolerances, compressed timeline, unfamiliar special processes). Apply additional controls for elevated-risk jobs.
2. Review the drawing and identify:
   - Raw material requirements (type, size, condition)
   - Machining operations required and their logical sequence
   - Special process requirements (heat treat, plating, NDT) and where they occur in the sequence
   - Inspection points (first piece, in-process, final)
   - Tooling and fixture requirements
   - CNC program requirements (existing or new program needed)

### Job Traveler Creation

3. Prepare QF-004 Job Traveler for the job. Include:
   - Job number, customer name, part number, drawing number and revision
   - Material specification and lot/heat traceability reference
   - Operation sequence (numbered steps) with description of each operation
   - Machine assignment for each operation
   - Inspection hold points (operations requiring sign-off before proceeding)
   - Special process send-out points with supplier identification
   - Space for operator sign-off (initials, date) at each operation
4. Verify the traveler matches the drawing requirements and contract review notes.

### Operation Sequencing

5. Sequence operations considering:
   - Geometric precedence (rough before finish, OD before ID where required)
   - Heat treatment timing (if required between machining operations)
   - Inspection points after critical dimensions are established
   - Outside processing send-out points (minimize handling and WIP time)
6. Identify which of the three machines each operation is assigned to based on capability and availability.

### Scheduling

7. Schedule jobs considering:
   - Customer-required delivery date (from contract review)
   - Material availability (lead time for procurement)
   - Outside processing lead times
   - Current machine loading and job priorities
   - First Article Inspection time (if FAI is required)
8. Communicate delivery concerns to the customer as early as possible if scheduling conflicts arise.

### Production Execution and Control

9. Release the job traveler and material to the shop floor only after:
   - Material has passed receiving inspection (QP-004)
   - CNC programs are verified per WI-004 (for new or revised programs)
   - Required tooling and fixtures are available
10. Perform each operation in the sequence documented on QF-004. Sign off each operation upon completion.
11. Do not skip or reorder operations without documented engineering authorization and updated traveler.

### Traceability

12. Maintain lot/heat traceability from raw material through finished part:
    - Record material heat/lot number on the job traveler at the first operation.
    - If multiple lots are used in a batch, maintain lot segregation or document all lot numbers on each traveler.
13. For serialized parts (customer requirement), assign serial numbers at the first machining operation and record on the traveler.

### Changes During Production

14. If a drawing change or process change is required during production, stop work and re-evaluate per QP-025 Control of Changes.
15. Update the job traveler to reflect any authorized changes. Note the change authorization reference on the traveler.

## 7. Records Generated

| Form No. | Title | When Completed |
|----------|-------|----------------|
| QF-004 | Job Traveler | Created at job planning, completed through production |
| QF-005 | In-Process Inspection Record | At each designated inspection hold point |

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| A | 2026-08-07 | Initial release | Shop Owner |