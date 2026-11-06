# Carry-over manifest

**Source branch:** `karman/basic-qms`
**Source commit:** `591d208213f79272e24b8fb3b9fd37af64dc6f96`
**Destination branch:** `active-working-qms`

## Selection and verification

- 83 QMS Markdown documents plus one unnumbered courtesy cross-reference.
- PDF_EXPORT.md, convert_md_to_pdf.py, its non-rendering test file and .gitignore retained.
- README.md and this manifest added for branch navigation and review.
- Every carried-over file is byte-identical to its source blob except Master_Document_List.md (branch scope/counts and navigation notes) and QMS_Recurring_Tasks.md (PDF workflow navigation). No quality policy, procedure, form, equipment entry or release state was rewritten.
- Recurring-task workflow: replace the removed Word-converter instruction with an on-request PDF export review task.
- Master register scope: implementation-guide rows removed, recurring-task register accounted for, total set to 83, and historical Word/project notes replaced by a current source/release summary.
- Draft procedure status preserved. Existing Markdown sources retain their recorded revision and approval fields.
- Source and generated Word versions are not maintained side by side on this branch.
- No conversion engine, export command or PDF generation was run.

## Source blob manifest

These are the original source blob IDs; the master register is the documented exception above. The destination tree is checked against this selection before completion.

| Path | Source Git blob SHA | Treatment |
| --- | --- | --- |
| `.gitignore` | `52aff1ab0619ba86273f25735cc5672ee5f4936a` | Unchanged |
| `00-manual/QM-001_Quality_Manual.md` | `a03e9224666e86102acd3a5ad0162b1c42939a7b` | Unchanged |
| `00-manual/QM-002_Quality_Policy.md` | `4f5f38115df14c2ac31069af5c2ce380c3da07cd` | Unchanged |
| `00-manual/QM-003_Quality_Objectives.md` | `c4a3d562cd7f86982cf6b9e2a08f11fc9acc2ba3` | Unchanged |
| `01-procedures/QP-001_Document_Control.md` | `8c75e43a9196d37bae6be94cb8cbe0df577796f2` | Unchanged |
| `01-procedures/QP-002_Contract_Review.md` | `2daaac5ac54dc96b1c78e056a6c9d72caccb0bcd` | Unchanged |
| `01-procedures/QP-003_Purchasing_and_Supplier_Management.md` | `dac910c91cb53c0fa1bf5bbdba7f050936ed2e36` | Unchanged |
| `01-procedures/QP-004_Receiving_Inspection.md` | `ef4732a055f616f2b9bf2ef75c8438cb10b07a9f` | Unchanged |
| `01-procedures/QP-005_Production_Planning_and_Control.md` | `ca58830eb5ec59a454d72c7032bb5479707e6f47` | Unchanged |
| `01-procedures/QP-006_In_Process_Inspection.md` | `7c33dedc73be5b4a0be7ad1413d93316dabacc7f` | Unchanged |
| `01-procedures/QP-007_Final_Inspection_and_Release.md` | `d4b082a2536c98f2709fdfe56a7753866e1d5857` | Unchanged |
| `01-procedures/QP-008_Nonconforming_Product.md` | `566187bd9db4c272b37ca9b63bbcf1e3680756fd` | Unchanged |
| `01-procedures/QP-009_Corrective_Action.md` | `1f543a6782e5cfb70d292885c81629ef5a01c166` | Unchanged |
| `01-procedures/QP-010_Calibration.md` | `07682a7f697f42ef48b305c3cb40bfe08c907318` | Unchanged |
| `01-procedures/QP-011_Internal_Audit.md` | `1074b0d2b4fce99bae61843a1f7f768b78e837c9` | Unchanged |
| `01-procedures/QP-012_Management_Review.md` | `1c40b0c1d5b6437f7dc6cd3034680dccc32ed5a3` | Unchanged |
| `01-procedures/QP-013_Training_and_Competence.md` | `4086e9a205c663969b897d975ec24a148a1edf4b` | Unchanged |
| `01-procedures/QP-014_Risk_Management.md` | `77e57d54bbc8a1493eb7767fdf5cce3e541581f2` | Unchanged |
| `01-procedures/QP-015_Configuration_Management.md` | `aed4b1d87a65de1fda97b76560636845e30acf93` | Unchanged |
| `01-procedures/QP-016_Counterfeit_Parts_Prevention.md` | `ce99d8f465f3be45286c14a4821ffefc1e3a12bf` | Unchanged |
| `01-procedures/QP-017_Product_Safety.md` | `c556caafc4b972b0f5aee459b6d99b441c0e04b6` | Unchanged |
| `01-procedures/QP-018_FOD_Prevention.md` | `ddd25540e3a8330ff7a2ea948f530b69f0145218` | Unchanged |
| `01-procedures/QP-019_Preventive_Maintenance.md` | `ae85a501cee4858414b0d49cb5f6095a7bad4a22` | Unchanged |
| `01-procedures/QP-020_Handling_Storage_Packaging_Shipping.md` | `17b7b974b487ec96353e1ed29076bcba89b855c7` | Unchanged |
| `01-procedures/QP-021_Customer_Property.md` | `ba3432aa6ceb3ee527c9e8323d624a367ee88114` | Unchanged |
| `01-procedures/QP-022_First_Article_Inspection.md` | `70478efaabccbc8167ee21823981ace477104436` | Unchanged |
| `01-procedures/QP-023_Customer_Communication.md` | `5888f0a5763cc93e7058e4eaf495bebe20c257bd` | Unchanged |
| `01-procedures/QP-024_Work_Transfer.md` | `b846b9501c124b69995fd21a563cc42035aa9554` | Unchanged |
| `01-procedures/QP-025_Control_of_Changes.md` | `212401af33f8c01790e1a6ed4d3c40ca20336468` | Unchanged |
| `02-work-instructions/WI-001_CNC_Mill_Setup_and_Operation.md` | `5fbef7f694060cdb545e8a3edd5aa7b2ce5bd245` | Unchanged |
| `02-work-instructions/WI-002_CNC_Lathe_Setup_and_Operation.md` | `7ca7e3a8ded8a177286e7b5845832328c5131de6` | Unchanged |
| `02-work-instructions/WI-003_Manual_Mill_Setup_and_Operation.md` | `b010911d1d29e4b59773121837e6693cc16bafb2` | Unchanged |
| `02-work-instructions/WI-004_CNC_Program_Verification.md` | `30170ac4c4972da2c1079a3175f05b03407140a9` | Unchanged |
| `02-work-instructions/WI-005_First_Piece_Inspection.md` | `4463199fc05ccafa62c74c36be4bb5fd95e51856` | Unchanged |
| `02-work-instructions/WI-006_Final_Part_Inspection.md` | `4845f3d72fad8d4a7f709bb4af7db4bedb3b868e` | Unchanged |
| `02-work-instructions/WI-007_Incoming_Material_Verification.md` | `68ff6177182e541d78e9bb68ab7c1f175837d619` | Unchanged |
| `02-work-instructions/WI-008_Part_Marking.md` | `10573baa21471579673a9540ede15219c05bcb21` | Unchanged |
| `02-work-instructions/WI-009_Packaging_and_Shipping.md` | `f9ce3afb97e6818875c2f02ef2576e29863c4921` | Unchanged |
| `03-forms/QF-001_Contract_Review_Checklist.md` | `89c9dc1ca251f889fed9b20d8069a62251792fe4` | Unchanged |
| `03-forms/QF-002_Purchase_Order.md` | `5c5de1a129f33796f2e128089b517859273fa76c` | Unchanged |
| `03-forms/QF-003_Receiving_Inspection_Record.md` | `5482d11267d4d489402e40fa4bdebe2626a5573d` | Unchanged |
| `03-forms/QF-004_Job_Traveler.md` | `c71df29a6aa9bc4e6768566980cc7eb73554f886` | Unchanged |
| `03-forms/QF-005_In_Process_Inspection_Record.md` | `44189f820863e623e51364550ff58bc9b83be6a7` | Unchanged |
| `03-forms/QF-006_Final_Inspection_Report.md` | `e0a48664fd09203b1e60337352c019e854cb7a7c` | Unchanged |
| `03-forms/QF-007_FAI_Form1_Part_Accountability.md` | `22e9741962b9a27ccdcb8966bf669b62f5b9888a` | Unchanged |
| `03-forms/QF-008_FAI_Form2_Product_Accountability.md` | `1a54bf26158b4261ac533b753fbb69e79cd0d270` | Unchanged |
| `03-forms/QF-009_FAI_Form3_Characteristic_Accountability.md` | `bb1daeafa8c6caf8b1d02b367d252425f34611cd` | Unchanged |
| `03-forms/QF-010_Certificate_of_Conformance.md` | `f4fc90329c5743ae8703a151f0cd357e81d634ca` | Unchanged |
| `03-forms/QF-011_NCR.md` | `a07ebc4e0ead9ab0f25b0c37fc8bbc40e5e4cc07` | Unchanged |
| `03-forms/QF-012_CAR.md` | `d161f4c6e2f97b09b7e74981987c1607253dd8ec` | Unchanged |
| `03-forms/QF-013_Internal_Audit_Checklist.md` | `0ea405ccb2c3fe74d7954bca0972826cc59d1844` | Unchanged |
| `03-forms/QF-014_Internal_Audit_Report.md` | `83164111ea9e63c8511fb813ae7a07a62038b433` | Unchanged |
| `03-forms/QF-015_Management_Review_Minutes.md` | `e11d6f77b69d7cae5a2ed313f89530105795538c` | Unchanged |
| `03-forms/QF-016_Training_Record.md` | `d9c889f128412a86504babbecce2dd62fe3514ac` | Unchanged |
| `03-forms/QF-017_Supplier_Evaluation.md` | `304f7c24f33da7e06b27744d04d931f2dc28ed1e` | Unchanged |
| `03-forms/QF-018_Supplier_Scorecard.md` | `85dc06bc913567b5715b269b4b8fbd88134a4ca9` | Unchanged |
| `03-forms/QF-019_Approved_Supplier_List.md` | `4520d0e510fe827823a0a1f4c00dc8f423f62760` | Unchanged |
| `03-forms/QF-020_Calibration_Log.md` | `dbc5491cfd7f8f226057ba68cc5f35d400ea2680` | Unchanged |
| `03-forms/QF-021_PM_Record.md` | `bbb2312763e8afb17e54367d5c3467c2dc13e165` | Unchanged |
| `03-forms/QF-022_Customer_Complaint.md` | `99c191b64ed65b17590ab7c4b79c30dcc6f094f4` | Unchanged |
| `03-forms/QF-023_Risk_Register.md` | `c9579ed71582cd7de12e1bb3ea9d9e0122889f34` | Unchanged |
| `03-forms/QF-024_Customer_Property_Log.md` | `585857554e7ea02d5d2664dcbabb3df3e8716fcb` | Unchanged |
| `03-forms/QF-025_Document_Change_Request.md` | `6df265aa24d999f68479dbddd29e2de50636fbb5` | Unchanged |
| `03-forms/QF-026_FOD_Checklist.md` | `a1701706851643a86bf1be3cbc8bcce7125dab55` | Unchanged |
| `03-forms/QF-027_Equipment_List.md` | `9450d236c21bdcd5d2e0d5f4ed4bc73244d3a054` | Unchanged |
| `03-forms/QF-028_Measurement_Equipment_List.md` | `cbe675506b058a31a7535e04efc96cd5947724f6` | Unchanged |
| `03-forms/QF-029_Change_Notification.md` | `d54e8715cc9e2d8c1dd0e1c1941a173adc83a910` | Unchanged |
| `03-forms/QF-030_Calibration_Schedule.md` | `1f9ca672a53c64e303986792dd31dcc5f11fd845` | Unchanged |
| `03-forms/QF-031_Suspect_Counterfeit_Report.md` | `e3c09530383bab96b026754065796ff7ad59b00e` | Unchanged |
| `03-forms/QF-032_Context_Analysis.md` | `21f66208c6027765bceb0c189722721b59953e83` | Unchanged |
| `03-forms/QF-033_OOT_Impact_Assessment.md` | `5cd6aeba949627e1c6540bab51142745ccfcb673` | Unchanged |
| `03-forms/QF-034_Supplier_Audit_Checklist.md` | `27264951c64d299ac540765de752b2269af04797` | Unchanged |
| `03-forms/QF-035_Supplier_CAR.md` | `113780e38020e53eaef000bb996433789544dc1a` | Unchanged |
| `03-forms/QF-036_Training_Matrix.md` | `65fe993520b70e36c885fc43fec0e90936ea8ad2` | Unchanged |
| `03-forms/QF-037_Quality_Objectives_Tracker.md` | `7fe34d99c605e5176261631bef109d1857229160` | Unchanged |
| `03-forms/QF-038_Improvement_Log.md` | `e3e91bfa7f11b36b5d51a120a28890bf4bd7a732` | Unchanged |
| `04-supporting/PO_Quality_Clauses_Addendum.md` | `4758e8a3922fa9b626a2899ea33e793132201675` | Unchanged |
| `04-supporting/Record_Retention_Schedule.md` | `0a17891778ce34f1395912bab7d0e1eb55ea0e94` | Unchanged |
| `04-supporting/Risk_Matrix_5x5.md` | `49c2ef54acecc16010bb91a1d1e868e130c96650` | Unchanged |
| `06-registers/CNC_Program_Log.md` | `4d6d1d791ae1bb615b11a5af506d4177ae11fed3` | Unchanged |
| `06-registers/Drawing_Register.md` | `19e61cac9a4fcdb31dfc975edf7ba875f8d0f456` | Unchanged |
| `06-registers/Master_Document_List.md` | `2285bc5dd9d4558c45550648f06c0009eb654b35` | Branch-scope metadata adjusted |
| `06-registers/NCR_CAR_Log.md` | `ec53e33426ff63dcba31efa2b8df7750fb595f5f` | Unchanged |
| `06-registers/QMS_Recurring_Tasks.md` | `e6dceb7677802352f8c1fb081026e9561155cbf8` | PDF workflow navigation adjusted |
| `PDF_EXPORT.md` | `f6045a88dae0b887cc518132afb7d9395dd099a1` | Unchanged |
| `convert_md_to_pdf.py` | `3aa04714d2e8c8785b5bb39e04f95b549691bea5` | Unchanged |
| `supplier-paperwork/karman/submission/QA-1003_QM-001_Cross_Reference.md` | `94345e8154793e5287573ef8412fb48d6dce94cd` | Unchanged |
| `tests/test_convert_md_to_pdf.py` | `07807bd37c66cc910fa785117d7839a49161de48` | Unchanged |
