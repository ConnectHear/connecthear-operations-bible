# ConnectHear Operations Bible

**Version 2.1 - WITH PROCESS STEPS**  
**Last Updated:** November 2025  
**Purpose:** Complete operational reference guide with step-by-step HOW-TO instructions

---

## 🎯 What's New in v2.1

**Added:** Step-by-step "Process Steps" sections to Finance workstreams
- Real ERPNext links and navigation
- Exact thresholds and approval flows
- Decision points (If X then Y)
- Common issues and solutions
- Tools and access requirements

**Coming Soon:** Process Steps for BD, Sign Language, and other departments

---

## How to Use This Document

- **Hierarchy:** Department → Area → Workstream → Process
- **RACI Key:** 
  - **R** = Responsible (does the work)
  - **A** = Accountable (final authority)
  - **C** = Consulted (provides input)
  - **I** = Informed (kept in the loop)
- **Visual Guide:** Each department marked with 🔷, each area with 📍
- **NEW: Process Steps** = Step-by-step HOW-TO instructions for doing the work

---

**NOTE:** This file is READY to use with Claude Code. Simply:
1. Place in `input/` folder as `ConnectHear_Operations_Bible_v2.md`
2. Run `python build.py`
3. Process Steps will appear in the HTML portal

---

*[All Business Development content remains unchanged - see original file lines 21-523]*
*[For brevity, BD section content not repeated here - it's identical to v2.0]*

---

# 2. 🔷 Finance & Compliance

## 📍 Area: Finance Operations

### Workstream: Accounts Payable

**Description:** Processing all outgoing payments to vendors, contractors, and service providers following proper authorization, documentation, and withholding tax requirements.

**Frequency:** Weekly (payment processing), Monthly (withholding tax filing with FBR)

**Output:**
- Vendor payments processed in ERPNext and bank
- Withholding tax (4%) deducted and filed monthly
- Payment receipts filed
- Vendor documentation maintained

**Dependencies:**
- AdminOps (for PO verification)
- Tax Compliance (for monthly withholding filing with FBR)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate (Umaima) | ✅ | | | |
| Finance Manager | | ✅ | | |
| AdminOps (procurement) | | | ✅ | |
| Arhum/Azima (approval >10k) | | | ✅ | |

**Process Steps:**

#### 1. Receive and Verify Invoice
- Receive invoice from vendor (email or physical delivery)
- Check invoice includes: Vendor name and NTN, invoice number and date, itemized list, total amount, bank details
- If incomplete → Email vendor requesting missing information

#### 2. Verify Purchase Order (PO)
- Check if invoice references a PO number
- If YES: Login to ERPNext, search for PO, verify amounts and items match
- If NO PO and < PKR 10,000 → Can proceed (record in notes)
- If NO PO and ≥ PKR 10,000 → Escalate to Arhum/Azima for approval first

#### 3. Verify Vendor Documentation
- Check vendor docs on file: NTN, CNIC/incorporation cert, bank details
- Location: TBD (to be organized in Google Drive > Finance > Vendors)
- If missing → Email vendor, do NOT proceed until received

#### 4. Calculate Withholding Tax
- Formula: Invoice Amount × 0.04 = Withholding Amount
- Example: PKR 100,000 × 0.04 = PKR 4,000 withholding
- Net Payment = PKR 100,000 - PKR 4,000 = PKR 96,000

#### 5. Create Payment Entry in ERPNext
- Click: https://hub.connecthear.org/app/payment-entry/new-payment-entry-zsnndqemii
- Fill in: Type (Pay), Supplier (select vendor), Paid Amount (net after withholding)
- Add deduction row: Tax Deducted at Source = withholding amount
- Select Cost Center: Main-CHPL, 8100-Marketing, 8200-BizDev, 8300-Product&Projects, 8400-Content&Design, 8500-SL&Training, 8600-Finance, 8700-Legal, 8800-AdminOps
- Link to Project if applicable
- Attach invoice PDF
- Click "Save" → Status: "Draft"

#### 6. Get Approval (if required)
- If amount > PKR 10,000: Slack message to Arhum/Azima with details and ERPNext link
- If amount ≤ PKR 10,000: No approval needed, proceed

#### 7. Submit Payment Entry
- Review all fields
- Click "Submit" → Status: "Submitted"
- Note payment entry number

#### 8. Process Payment via HBL Bank
- Login to HBL bank portal
- Navigate: Payments → Make Payment
- Enter vendor bank details and NET amount (after withholding)
- Upload supporting document (ERPNext payment entry)
- Submit and note transaction reference

#### 9. Update ERPNext
- Add bank transaction reference to payment entry
- Mark status as "Paid"

#### 10. File Withholding Tax with FBR (Monthly - by 5th)
- On or before 5th of each month for PREVIOUS month
- Login: https://iris.fbr.gov.pk
- Navigate: Returns → Withholding Tax
- Enter all vendor payments with 4% withheld
- Submit return and download challan

#### 11. Issue Tax Challan to Vendor (If Requested)
- Currently only if vendor requests
- Email challan with details
- CC: arhum@connecthear.com, azima@connecthear.com

#### 12. File Records
- Naming: CHPL-PMT-.MM-.YY-.####
- Save: Invoice, payment entry, bank receipt, FBR challan
- Location: TBD (Google Drive > Finance > Payments > [Year] > [Month])

#### Decision Points
**If invoice > PKR 10,000 with no PO:** Get approval from Arhum/Azima
**If vendor docs missing:** Stop process, request documents
**If bank payment fails:** Check balance, verify details, retry or escalate

#### Common Issues
**Issue:** Vendor not in ERPNext
**Solution:** Create new supplier first (Buying → Supplier → New), then return to payment

**Issue:** Payment fails at bank
**Solution:** Check account balance, verify vendor bank details are correct, retry or contact vendor

**Issue:** FBR portal down on filing deadline
**Solution:** Note deadline, file as soon as restored, document that portal was unavailable

#### Tools & Access Required
- ERPNext (Finance role) - https://hub.connecthear.org
- HBL Bank Portal
- FBR Portal - https://iris.fbr.gov.pk
- Google Drive (Finance folder)

#### Key Thresholds
- Withholding Tax Rate: 4%
- Approval Threshold: PKR 10,000
- Tax Filing Deadline: 5th of each month (for previous month)
- Physical Invoice Delivery: ~30% of invoices (especially out-of-city)

---

### Workstream: Accounts Receivable

**Description:** Generating client invoices, sending to clients, tracking payment status, and reconciling receipts against bank statements.

**Frequency:** Per Service Delivery (invoicing), Weekly (payment tracking)

**Output:**
- Client invoices generated in ERPNext
- Invoices sent via email (70%) or physical delivery (30%)
- Payment reminders sent (2 weeks before, on due date, weekly after)
- Payments reconciled in ERPNext

**Dependencies:**
- Sign Language Department (service delivery confirmation)
- Product Team (for product/feature deliverables)
- BD (for contract terms and client relationship)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager | | ✅ | | |
| BD (for overdue) | | | ✅ | |

**Process Steps:**

#### 1. Confirm Service Delivery
- Receive confirmation from Ismail (interpretation) or Project team (training/product)
- Verify against contract: deliverable in scope, pricing/rates correct, payment terms

#### 2. Gather Invoice Details
- Client legal name, billing address, NTN (if available)
- Service description, quantity, rate from contract
- Calculate total amount
- Determine due date based on payment terms (Net 15, Net 30)

#### 3. Create Sales Invoice in ERPNext
- Search: "New Sales Invoice" from top search bar
- Fill in: Customer, Posting Date (today), Due Date (calculated)
- Add item row: Service type, description, quantity, rate
- Select Cost Center: 8500-SL&Training (interpretation/training), 8300-Product&Projects (tech)
- Link to Project if applicable
- Set Payment Terms (Net 15, Net 30)
- Attach supporting docs
- Click "Save" → Status: "Draft"

#### 4. Submit Invoice
- Review all fields
- Click "Submit" → Invoice number auto-generated: CHPL-INV-.MM-.YY-.####
- Example: CHPL-INV-.11-.24-.0123

#### 5. Export and Deliver
- Click "Print" → Download PDF
- Check contract for delivery preference:
  - **Email (70%)**: Most common, faster - Send to billing contact with payment details
  - **Physical (30%)**: Out-of-city, government - Print, courier via TCS/Leopards
- Record delivery in ERPNext (add comment with date sent)

#### 6. Set Payment Reminders
- First reminder: 2 weeks before due date (friendly)
- Second reminder: On due date (payment due notice)
- Follow-up: Weekly after due date if unpaid
- Currently manual reminders (transitioning to ERPNext automation)

#### 7. Receive Payment Confirmation
- Bank notification when payment received
- Verify amount matches invoice
- Note transaction reference number and date

#### 8. Reconcile in ERPNext
- Go to invoice → Create → Payment Entry
- OR search "New Payment Entry"
- Fill in: Type (Receive), Customer, Received Amount, Bank account
- Link to invoice, add payment reference
- Submit → Invoice status updates to "Paid"

#### 9. Update Aging Report
- Invoice removed from outstanding aging report once paid
- If overdue: Escalate to Arhum/Azima and BD/account manager

#### 10. File Records
- Naming: CHPL-INV-.MM-.YY-.#### (same as invoice number)
- Save: Invoice PDF, service delivery confirmation, email correspondence, payment receipt
- Location: TBD (Google Drive > Finance > Invoices > [Year] > [Month])

#### Decision Points
**Email vs Physical:** Check contract - default email unless specified physical
**Reminder escalation:** 2 weeks before (friendly) → on due date (firm) → 1 week overdue (urgent) → 2 weeks overdue (escalate to leadership)

#### Common Issues
**Issue:** Client disputes invoice amount
**Solution:** Review contract pricing, check service delivery records, reconcile with client, issue credit note if needed

**Issue:** Client hasn't received invoice (email)
**Solution:** Check email sent successfully, resend, try alternate email, send via WhatsApp as backup

**Issue:** Payment received but wrong amount
**Solution:** Contact client for clarification - check if tax withheld, partial payment, or error

#### Tools & Access
- ERPNext (Finance role)
- Email (finance@connecthear.org or personal @connecthear.org)
- Courier account (TCS/Leopards)

#### Key Numbers
- Invoice Naming: CHPL-INV-.MM-.YY-.####
- Delivery Split: 70% email, 30% physical/courier
- Reminder Schedule: 2 weeks before, on due, weekly after
- Typical Terms: Net 15 or Net 30

---

### Workstream: Tax Compliance

**Description:** Monthly filing of payroll tax, sales tax (15%), and withholding tax (4%) with Federal Board of Revenue (FBR).

**Frequency:** Monthly (by 5th of each month for previous month)

**Output:**
- Payroll tax return filed
- Sales tax return filed (if applicable)
- Withholding tax return filed
- Tax challans downloaded and saved
- Any tax payments processed

**Dependencies:**
- Payroll (for payroll tax data)
- Accounts Payable (for withholding tax data)
- Accounts Receivable (for sales tax data)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager | | ✅ | | |

**Process Steps:**

**FILING DEADLINE:** By 5th of each month for PREVIOUS month (e.g., file Feb 5th for January taxes)

#### A. PAYROLL TAX FILING

**1. Generate Payroll Report**
- After payroll processed: Go to HR → Payroll Entry → Select month
- Download report showing gross salary, tax deducted, net salary
- Note total payroll tax deducted

**2. Login to FBR Portal**
- Go to: https://iris.fbr.gov.pk
- Enter shared Finance credentials

**3. File Payroll Tax Return**
- Navigate: Returns → Payroll Tax
- Select: Previous month and year
- Enter: Total payroll, total tax deducted, number of employees
- Upload payroll report
- Submit and download challan
- If payment required: Process via bank

**4. Record in ERPNext**
- Add comment to payroll entry: "Tax filed on [date], Challan #[number]"
- Attach challan PDF

#### B. SALES TAX FILING

**1. Identify Taxable Transactions**
- Review all payments RECEIVED (not invoices issued) in previous month
- Filter ERPNext: Accounts → Payment Entry (received) → Previous month
- Calculate 15% on taxable receipts (most services exempt - verify contract)

**2. Login to FBR Portal**
- Navigate: Returns → Sales Tax

**3. File Sales Tax Return**
- Select: Previous month
- Enter: Total sales, taxable amount, sales tax (15%), input tax, net tax payable
- Upload: Payment receipts and invoices
- Submit and download challan

**4. Record in ERPNext**
- Create journal entry or note: "Sales tax filed for [month], Amount PKR [X]"

#### C. WITHHOLDING TAX FILING

**1. Compile Vendor Payments**
- ERPNext: Accounts → Payment Entry (paid) → Previous month
- For each: Note vendor NTN, invoice amount, withholding (4%)
- Create summary spreadsheet

**2. Login to FBR Portal**
- Navigate: Returns → Withholding Tax

**3. File Withholding Tax Return**
- Select: Previous month
- For each vendor: Enter NTN, withholding amount, nature of payment
- Attach invoice/payment proofs
- Submit and download master challan

**4. Issue Vendor Challans (If Requested)**
- Currently: Only if vendor requests
- Download individual challan from FBR
- Email to vendor with subject: "Withholding Tax Challan - [Month]"
- Future: Proactively send to all vendors

**5. Record in ERPNext**
- Update all payment entries: Add comment with filing date and challan number
- Attach master challan

#### Monthly Checklist (Complete by 5th)
- [ ] Payroll tax: Report downloaded, FBR filed, challan saved, payment made
- [ ] Sales tax: Receipts identified, FBR filed, challan saved, payment made
- [ ] Withholding tax: Vendors compiled, FBR filed, challans saved, issued if requested
- [ ] All challans saved to Google Drive > Finance > Tax > [Year] > [Month]
- [ ] ERPNext entries updated

#### Decision Points
**If deadline approaching with incomplete data:** File with estimates to avoid penalty, amend later if needed
**If FBR portal down:** Document unavailability, file immediately when restored
**If vendor lacks NTN:** They must obtain NTN to receive payment (legal requirement)

#### Common Issues
**Issue:** FBR portal login fails
**Solution:** Try different browser, clear cache, incognito mode, contact FBR helpline

**Issue:** Sales tax unclear (exempt vs taxable)
**Solution:** Check contract, consult Arhum/tax advisor, when in doubt file conservatively

**Issue:** Missed filing deadline
**Solution:** File ASAP, FBR charges late penalty (usually small), document reason

#### Tools & Access
- FBR Portal: https://iris.fbr.gov.pk (shared Finance login)
- ERPNext: Payroll and Accounts modules
- Bank portal: For tax payments

#### Key Rates & Deadlines
- Payroll Tax: Variable by employee bracket
- Sales Tax: 15% (many services exempt)
- Withholding Tax: 4% on vendor payments
- Deadline: 5th of each month for previous month

---

### Workstream: Bank Reconciliation

**Description:** Daily matching of bank statement transactions with ERPNext payment entries to ensure accurate records and identify discrepancies.

**Frequency:** Daily (target), Weekly (current practice)

**Output:**
- Bank transactions matched to ERPNext entries
- Discrepancies identified and resolved
- Closing balance reconciled
- Monthly reconciliation report

**Dependencies:**
- Accounts Payable (for outgoing payments)
- Accounts Receivable (for incoming payments)
- Payroll (for salary disbursements)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager | | ✅ | | |

**Process Steps:**

**CURRENT STATE:** Manual in Google Sheets
**TARGET STATE:** Daily in ERPNext (transitioning)

#### CURRENT MANUAL PROCESS

**1. Download Bank Statement**
- Login to HBL bank portal
- Navigate: Statements / Transaction History
- Select: Previous business day (or since last reconciliation)
- Download as Excel or PDF
- Save: CHPL-BANK-.MM-.DD-.YY.xlsx

**2. Open Reconciliation Sheet**
- Location: TBD (Google Sheets - to be organized)
- Columns: Date, Type (Debit/Credit), Reference, Description, Amount, ERPNext Match, Status, Notes

**3. Import Bank Transactions**
- Copy from downloaded statement
- Paste into reconciliation sheet
- Sort by date (oldest first)

**4. Match with ERPNext**
- Open ERPNext: Accounts → Payment Entry → List
- Filter by same date range
- For each bank transaction:
  - Look for matching payment: amount, date (±1-2 days), party name
  - If found: Note ERPNext number in sheet, mark "Matched"
  - If not found: Mark "Unmatched", investigate

**5. Identify Discrepancies**
- **In bank but not ERPNext:** Could be direct deposits, fees, interest, refunds → Create ERPNext entry
- **In ERPNext but not bank:** Could be processing, failed, future-dated → Verify with bank, may cancel ERPNext entry

**6. Create Missing ERPNext Entries**
- For legitimate bank transactions not in ERPNext:
  - Create payment entry (Type: Receive for credit, Pay for debit)
  - Match amount, date, description
  - Assign cost center
  - Note in remarks: "From bank rec [date]"

**7. Calculate Closing Balance**
- Opening balance + Credits - Debits = Closing balance
- Compare to bank statement ending balance
- If mismatch: Review for missing transactions, check date cutoffs

**8. Document and File**
- Save reconciliation sheet
- Export as PDF
- Location: TBD (Google Drive > Finance > Reconciliation > [Year] > [Month])

#### TRANSITIONING TO ERPNEXT

**1. Enable Bank Reconciliation**
- Go to: Accounts → Bank Reconciliation Tool

**2. Import Bank Statement**
- Click "Import Bank Statement"
- Upload file (Excel/CSV)
- Map columns to ERPNext fields
- Preview and confirm

**3. Auto-Match**
- ERPNext attempts auto-match (exact amounts, similar dates)
- Review suggested matches (Green = high confidence, Yellow = possible, Red = unmatched)
- Accept accurate matches

**4. Manual Matching**
- For unmatched: Click transaction, search for payment entry
- If found: Link manually
- If not found: Create new entry

**5. Submit Reconciliation**
- Review summary
- Check: Opening + transactions = closing
- Submit → All linked entries marked "Reconciled"
- Generate report for filing

#### Decision Points
**Bank transaction not in ERPNext:**
- Known (fee/interest/deposit) → Create entry
- Unknown → Investigate before creating
- Duplicate → Check if already entered differently

**ERPNext payment not in bank:**
- Still processing (1-2 day lag) → Mark "Pending"
- Failed → Verify, may need to cancel and redo
- Future-dated → No action needed yet

#### Common Issues
**Issue:** Unrecognized bank transaction
**Solution:** URGENT - Contact bank immediately (could be fraud)

**Issue:** Missing transaction in statement
**Solution:** Check date range, may be just outside range or still processing

**Issue:** ERPNext "Paid" but not in bank
**Solution:** Payment likely failed - contact bank, cancel ERPNext entry, investigate why

**Issue:** Timing differences (1-2 day lag)
**Solution:** Normal - mark "Pending" and reconcile next day

#### Tools & Access
- HBL Bank Portal (statement download)
- ERPNext Accounts module
- Google Sheets (temporary during transition)

#### Best Practices
- Daily reconciliation: 15-30 min/day prevents errors from compounding
- Document everything: Unexplained transactions MUST be investigated
- Month-end priority: Must be 100% reconciled before closing month

---

### Workstream: Payroll & Stipends

**Description:** Monthly processing of employee salaries, stipends, and contractual payments with proper tax deduction, project allocation, and bank disbursement.

**Frequency:** Monthly (on payday - typically end of month)

**Output:**
- Payroll processed in ERPNext
- Salary payments made via bank
- Salary slips distributed to employees
- Payroll tax filed with FBR (by 5th of next month)
- Expenses properly allocated to cost centers and projects

**Dependencies:**
- HR (for attendance, leaves, salary changes)
- Project Teams (for project time allocation)
- Tax Compliance (for monthly payroll tax filing)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager/Arhum | | ✅ | | |
| HR | | | ✅ | |

**Process Steps:**

#### 1. Verify Employee Data
- Go to: HR → Employee → List
- For each employee verify: Salary structure active, bank details correct, tax settings configured, any changes approved

#### 2. Process Attendance (if applicable)
- HR → Attendance → Bulk Attendance
- Review month: Mark present/absent, record leaves
- Calculate deductions for unpaid leaves

#### 3. Create Payroll Entry
- HR → Payroll Entry → New
- Fill in: Posting Date (last day of month), Company (ConnectHear), Frequency (Monthly), Start/End dates
- Payment Account: HBL bank account
- Cost Center: 8600-Finance or split by department

#### 4. Get Employees
- Click "Get Employees"
- Review list: Remove those who shouldn't be paid this month
- Verify all expected employees included

#### 5. Generate Salary Slips
- Click "Create Salary Slips"
- Review each slip: Gross correct? Deductions correct? Net pay correct?
- If errors: Edit salary structure, regenerate

#### 6. Link to Projects/Service Delivery ⭐ CRITICAL
- For each employee identify which projects they worked on
- Use ERPNext Project field to link salary expense to client projects
- Example: Interpreter on ABC Corp training → Link to "ABC Corp Training" project
- Multiple projects → Split proportionally
- Back-office staff → Link to Main-CHPL (overhead)

#### 7. Assign Cost Centers
- By role/department:
  - Interpreters/trainers → 8500-SL&Training
  - Product/tech → 8300-Product&Projects
  - BD → 8200-BizDev
  - Finance → 8600-Finance
  - Marketing → 8100-Marketing
  - AdminOps → 8800-AdminOps
  - Mixed/shared → Main-CHPL

#### 8. Calculate Payroll Tax
- System auto-calculates based on employee tax bracket
- Verify calculation correct
- Total tax = Amount to file with FBR

#### 9. Submit Payroll Entry
- Review summary: Total gross, deductions, net pay
- Click "Submit" → Salary slips finalized

#### 10. Generate Bank Payment File
- Click "Make Bank Entry" or export payment list
- Download with: Employee name, bank account, IBAN, net pay
- Format for HBL bulk upload if needed

#### 11. Process Bank Payments
- Login to HBL bank portal
- Navigate: Bulk Payments / Salary Upload
- Upload file, review total, authorize
- Get confirmation and transaction reference

#### 12. Update ERPNext
- Add comment: "Payments processed [date], Bank ref: [number]"
- Status: "Paid"

#### 13. File Payroll Tax
- By 5th of next month
- Follow Tax Compliance workstream process
- Use total tax deducted from this payroll entry

#### 14. Distribute Salary Slips
- Generate PDF slips (each employee or bulk print)
- Email to employees: "Please find attached your salary slip for [Month]"
- Or upload to employee self-service portal

#### Decision Points
**Mid-month joiner:** Prorate based on working days
**Unpaid leaves:** Deduct proportionally: (Unpaid days / Total days) × Monthly salary
**Salary change mid-month:** May need two slips (old rate + new rate prorated)
**Resignation before payday:** Calculate final settlement with pro-rated salary, leave encashment, dues

#### Common Issues
**Issue:** Bank upload file format rejected
**Solution:** Check HBL format requirements (columns, headers, date format), reformat and re-upload

**Issue:** Employee bank details wrong
**Solution:** Payment bounces, get correct details, process individual payment, update for next month

**Issue:** Project linking unclear (employee across departments)
**Solution:** Use timesheet if available, or manager estimate percentage split, document assumption

#### Tools & Access
- ERPNext (HR and Accounts modules)
- HBL Bank Portal (bulk payment feature)
- FBR Portal (for tax filing)

#### Key Notes
- Project linking CRITICAL for accurate client costing and invoicing
- Cost center assignment enables department expense tracking
- File tax by 5th of next month (coordinate with Tax Compliance workstream)

---

### Workstream: Expense Claims Processing

**Description:** Processing employee reimbursement requests for business expenses with proper documentation, approval, and project/cost center allocation.

**Frequency:** As submitted (weekly processing)

**Output:**
- Expense claims verified and approved
- Reimbursements paid to employees
- Expenses properly allocated to projects and cost centers
- Records filed

**Dependencies:**
- HR (for employee verification)
- Department Heads (for approval)
- Projects (for project-specific expense allocation)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager | | ✅ | | |
| Line Manager | | | ✅ | |

**Process Steps:**

#### 1. Receive Expense Claim
- Employee submits via ERPNext OR email with receipts
- Must include: Date, description/purpose, amount, receipt/invoice, cost center, project (if applicable)

#### 2. Verify Supporting Documents
- Check receipts/invoices: Valid (original, legible)? Amounts match? Vendor visible? Date reasonable?
- If missing/unclear: Return to employee for correction

#### 3. Verify Expense is Legitimate
- Business-related: Travel (client meetings, events), meals (client entertainment), supplies (office/project), other approved
- If questionable: Ask employee, check with line manager, refer to expense policy

#### 4. Verify Approval
- Must be approved by: Line manager (operational), Department head (larger amounts), Arhum/Azima (if > PKR 10k)
- If not approved: Route to appropriate approver

#### 5. Create/Review in ERPNext
- If via email/paper: Create new (HR → Expense Claim → New)
- If in ERPNext: Open and review
- Fill in all fields

#### 6. Link to Cost Center and Project ⭐ CRITICAL
- Assign Cost Center by department (8100-Marketing, 8200-BizDev, etc.)
- If project-specific: Link to Project and Customer
- Example: Travel for ABC Corp training → Project "ABC Corp Training", Customer "ABC Corp"
- Purpose: Accurate project costing for billing/profitability

#### 7. Calculate Reimbursement
- Usually: Full expense amount
- Check: Per-diem limits, category caps, subtract any advance given
- Net reimbursement = Total - Advance - Disallowed

#### 8. Submit in ERPNext
- Review all fields, attach receipts
- Click "Submit" → Status: "Submitted"

#### 9. Create Payment Entry
- From expense claim: Create → Payment Entry
- Type: Pay, Party: Employee, Amount: Reimbursement
- Link to expense claim

#### 10. Process Payment
- **Bank Transfer (preferred):** HBL portal, enter employee bank details, process payment, note transaction reference
- **Cash (small amounts < PKR 1k):** From petty cash, get employee signature

#### 11. Update ERPNext
- Add comment with payment details
- Mark status "Paid"

#### 12. File Records
- Naming: CHPL-EXP-.MM-.YY-.####
- Save: Claim form, receipts, payment confirmation
- Location: TBD (Google Drive > Finance > Expense Claims > [Year] > [Month])

#### Decision Points
**Exceeds policy limit:** Get special approval from Arhum/Azima, document reason
**Receipt missing:** Cannot reimburse without proof (except <PKR 500 with employee declaration)
**Questionable expense:** Discuss with employee and manager - if approved process, if rejected inform employee
**Needs advance:** Process as Cash Advance (different from reimbursement), deduct from later claim

#### Common Issues
**Issue:** Claim submitted months late
**Solution:** Check policy (usually 30-60 day limit), if beyond may need special approval

**Issue:** Receipt illegible
**Solution:** Ask for vendor duplicate receipt, if unavailable employee declaration + manager approval for small amounts

**Issue:** Wrong project linked
**Solution:** Amend expense claim, correct project, resubmit (critical for accurate costing)

**Issue:** Multiple expenses spanning different cost centers
**Solution:** Split into multiple claims OR use line-item cost center assignment

#### Tools & Access
- ERPNext (HR and Accounts)
- HBL Bank Portal
- Google Drive

#### Key Notes
- Project linking essential for client projects (accurate cost tracking)
- Timely processing (7-14 days) keeps employees satisfied
- Documentation (receipts) non-negotiable for > PKR 500

---

### Workstream: Grant Transaction Tagging

**Description:** Tagging all grant-funded expenses and revenues to specific grants and budget categories for donor reporting and compliance.

**Frequency:** Per Transaction (real-time tagging), Monthly (utilization review)

**Output:**
- All grant transactions tagged to grant projects in ERPNext
- Budget utilization tracked by category
- Monthly grant reports
- Quarterly/annual donor reports

**Dependencies:**
- Accounts Payable (for expense tagging)
- Accounts Receivable (if grant generates revenue)
- Payroll (for salary allocation)
- Grant Management (for budget and compliance oversight)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Finance Associate | ✅ | | | |
| Finance Manager/Azima | | ✅ | | |
| Grant Manager | | | ✅ | |

**Process Steps:**

#### 1. Understand Grant Structure (One-Time Setup)
- For each grant document in ERPNext: Grant name/number, donor, amount, period, budget categories, restrictions
- Create Project in ERPNext for the grant
- Set up Budget linked to grant project

#### 2. Identify Grant-Eligible Transactions
- When processing ANY transaction ask: "Is this funded by a grant?"
- If YES: Determine which grant
- If NO: Tag as "General Operations"
- Grant-eligible: Salaries (for staff on grant), program supplies, travel for grant activities, training costs, equipment (if approved)

#### 3. Tag Transaction to Grant Project
- In every ERPNext form (Payment Entry, Expense Claim, Payroll Entry, Purchase Invoice):
  - Project Field: Select grant project
  - Cost Center: May be grant-specific or regular
  - Customer: If grant services specific client/community
- Example: Interpreter salary for GSMA grant → Project "GSMA Deaf Education", Cost Center "8500-SL&Training", Note "50% time on GSMA"

#### 4. Allocate to Budget Category
- Each grant has categories (Personnel, Travel, Equipment, Supplies, Other per agreement)
- Use ERPNext Accounting Dimension or custom field
- If not available: Use description/remarks

#### 5. Document Justification
- Add notes in ERPNext: Why charged to grant? What activity? What budget line?
- Example in remarks: "Grant: GSMA, Activity: Teacher training workshop, Budget: Travel-Domestic, Justification: Transport for 2 trainers per deliverable 3.2"

#### 6. Verify Against Budget
- Before processing: Check ERPNext → Projects → [Grant] → Budget
- View: Budgeted vs Actual vs Remaining
- If exceeded: Stop, check if reallocation allowed, get approval, document
- If not allowed: Cannot charge, use general funds

#### 7. Monthly Utilization Review
- Generate: Project-wise transactions report
- Review by budget category: Total spent, remaining, burn rate
- Share summary with grant manager/Azima and donor if required

#### 8. Quarterly/Annual Reporting
- Prepare for donors: Budget vs actual by category, narrative on funded activities, supporting docs
- Export from ERPNext: Financial report, budget utilization
- Format per donor requirements, submit by deadline

#### 9. Audit Trail Maintenance
- Keep: Transaction records, receipts, timesheets, approvals, reports submitted
- Location: TBD (Google Drive > Finance > Grants > [Grant Name])
- Retention: Per grant (usually 5-7 years post-grant)

#### Decision Points
**Transaction applies to multiple grants:** Determine primary or split proportionally (60% Grant A, 40% Grant B), document split ratio
**Budget category overspent but surplus elsewhere:** Check if reallocation allowed, if YES get donor approval and document, if NO use general funds
**Unsure if eligible:** Review grant agreement, consult grant manager, if doubt charge to general (safer for audit)

#### Common Issues
**Issue:** Forgot to tag transaction
**Solution:** Amend in ERPNext, add project/grant tag, resubmit ASAP

**Issue:** Tagged to wrong grant
**Solution:** Amend, change to correct grant, document correction

**Issue:** Grant budget exhausted mid-project
**Solution:** Review spending, request reallocation if possible, escalate for additional funding or scope reduction

**Issue:** Donor rejects expense in audit
**Solution:** Move from grant to general funds retroactively, update reports, learn for future

**Issue:** Multiple staff partially on grant
**Solution:** Use timesheets for % of time, allocate proportionally (30% time = 30% of salary to grant)

#### Tools & Access
- ERPNext (Projects, Budget, Accounts)
- Google Drive (grant documentation)
- Grant agreements

#### Key Notes
- Tag EVERY transaction (missing tags = inaccurate reports = donor issues)
- Budget monitoring continuous (don't wait for month-end)
- Documentation CRITICAL (audits can happen years later)
- When in doubt, ask (better to clarify than mis-charge)

---

### Workstream: Petty Cash Management

**Description:** Managing small cash fund for urgent, minor expenses that cannot wait for regular payment processing.

**Frequency:** Daily (disbursements), Weekly (reconciliation), Monthly (replenishment and reporting)

**Output:**
- Petty cash disbursed for approved small expenses
- Petty cash register maintained with all transactions
- Regular reconciliation (cash on hand matches register)
- Monthly petty cash report

**Dependencies:**
- AdminOps (often petty cash custodian)
- All Departments (for small urgent purchases)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Petty Cash Custodian (AdminOps/Finance) | ✅ | | | |
| Finance Associate | | ✅ | | |

**Process Steps:**

#### 1. Petty Cash Setup (One-Time)
- Determine fund size: PKR 5,000 - 10,000 (based on monthly small expenses)
- Create petty cash register (Excel/log book)
- Columns: Date, Description, Amount, Receipt #, Paid To, Approved By, Balance
- Designate custodian
- Set limits: <PKR 500 no approval, PKR 500-1000 supervisor approval, >PKR 1000 avoid petty cash

#### 2. Initial Funding
- Withdraw from bank (approved amount)
- Record in ERPNext: Payment Entry, From Bank to Petty Cash account
- Place in secure box/drawer
- Record opening balance in register

#### 3. Disbursing Cash
- Staff requests: Purpose? Amount? Urgent?
- Verify: Urgent and can't wait? Within limits?
- If approved: Count and give cash, get acknowledgment (signature), note "Receipt due within 24 hours"

#### 4. Receiving Receipts
- Staff returns with: Receipt/invoice from vendor, any change
- Verify: Receipt valid (vendor, amount, date), amount matches or staff returns change
- If no receipt: Staff declaration for small amounts (<PKR 200), larger amounts staff must reimburse

#### 5. Recording Transactions
- In register: Date, description (what purchased), amount, receipt #, paid to (staff/vendor), approved by (if needed), running balance
- Attach receipt to register or file separately

#### 6. Daily/Weekly Reconciliation
- Count physical cash
- Compare to register balance
- Formula: Opening - Disbursements + Replenishments = Current balance
- If mismatch: Investigate (unrecorded transaction? Error? Missing receipt?), resolve immediately, report shortage if unresolved

#### 7. Replenishing Petty Cash
- When low (e.g., <PKR 2,000): Tally receipts since last replenishment
- Prepare request: Total expenses PKR X, current balance PKR Y, replenishment needed PKR X
- Submit receipts to Finance for verification
- Get approval

#### 8. Processing Replenishment
- Finance verifies receipts
- Create payment entry: Bank → Petty Cash, amount = replenishment
- Attach all receipts
- Withdraw cash, hand to custodian
- Update register: "Replenishment received PKR X"

#### 9. Assign Cost Centers
- When recording in ERPNext (replenishment or month-end):
  - Office supplies for BD → 8200-BizDev
  - Courier for Finance → 8600-Finance
  - General office → 8800-AdminOps
  - Project-specific → Link to project

#### 10. Monthly Report
- Tally all expenses: By category (supplies, courier, refreshments, repairs, misc)
- Create summary: Opening balance, total expenses (by category), replenishments, closing balance
- Submit to Finance
- Finance records in ERPNext if not already done

#### 11. Secure Storage
- Locked drawer or cash box
- Access only by custodian(s)
- Not left unattended
- Key: Custodian holds, spare with supervisor

#### Decision Points
**Exceeds limit:** Use regular payment process (Accounts Payable), don't deplete petty cash
**No receipt:** <PKR 200 staff declaration may be accepted, >PKR 200 staff must reimburse OR produce receipt
**Running low before schedule:** Replenish immediately (don't wait)
**Shortage in reconciliation:** Investigate, if can't explain custodian may be responsible, document and report

#### Common Issues
**Issue:** Staff takes without signing
**Solution:** Enforce policy - no signature = no cash

**Issue:** Receipt submitted late
**Solution:** Set policy (24-48 hours max), if late staff may explain or reimburse

**Issue:** Constantly running out
**Solution:** Increase fund size OR encourage planning and regular payments

**Issue:** Receipt lost
**Solution:** Staff declaration with detail, if frequent staff reimburses personally

**Issue:** Cash vs register mismatch
**Solution:** Recount, re-check math, review recent transactions, if persistent investigate thoroughly and report

#### Tools & Access
- Physical cash box (secure)
- Petty cash register (Excel/log book)
- Bank access for withdrawal

#### Key Numbers
- Transaction Limit: PKR 500-2,000 max
- Fund Size: PKR 5,000-10,000 typical
- Approval Threshold: <PKR 500 no approval, >PKR 500 supervisor
- Receipt Required: Mandatory (except <PKR 200 with declaration)

---

## 📍 Area: Accounting & Reporting

[5 workstreams would go here - Monthly Financial Statements, Budget Tracking, Cost Allocation, Financial Reporting, Year-End Closing]

---

## 📍 Area: Grants Management

[4 workstreams would go here - Grant Proposal Support, Grant Budget Management, Grant Reporting, Grant Compliance]

---

## 📍 Area: Legal & Compliance

[4 workstreams would go here - Contract Management, Corporate Compliance, IP Management, Litigation Support]

---

## 📍 Area: Procurement & Vendor Management

[4 workstreams would go here - Vendor Onboarding, Purchase Orders, Vendor Performance, Contract Negotiation]

---

## 📍 Area: Audit & Internal Controls

[3 workstreams would go here - Internal Audit, External Audit, Controls Documentation]

---

# 3-8. 🔷 Other Departments

**NOTE:** Other departments (Content & Design, Product & Projects, Sign Language, Marketing, AdminOps, Leadership/PMO) maintain their v2.0 structure. Process Steps will be added as they are documented.

[Rest of departments unchanged from v2.0]

---

# 📋 Document Control

**Version History:**
- v1.0: Initial structure with departments, areas, workstreams
- v2.0: Added comprehensive BD and Finance details
- v2.1: Added Process Steps to Finance workstreams (THIS VERSION)

**Next Updates:**
- v2.2: Add Process Steps to BD workstreams (after Ahmed's input)
- v2.3: Add Process Steps to Sign Language workstreams
- v3.0: All departments with complete Process Steps

---

**END OF OPERATIONS BIBLE v2.1**
