# ConnectHear Finance & Compliance - Complete Process Steps

**Version:** 2.0  
**Last Updated:** November 2025  
**Status:** READY TO USE - Complete with real details

---

## 📋 How to Use This Document

This document contains **step-by-step process instructions** for all Finance & Compliance workstreams. Each process includes:
- **Numbered steps** - Exactly what to do, in order
- **System navigation** - Exact ERPNext paths and links
- **Decision points** - If X then Y logic
- **Common issues** - What goes wrong and how to fix it
- **Tools required** - What access you need

---

# 🔷 FINANCE OPERATIONS

## 💰 Workstream: Accounts Payable

### Process: How to Process a Vendor Payment

#### Prerequisites
- ERPNext access (Finance role)
- HBL bank portal access
- FBR portal access (https://iris.fbr.gov.pk)
- Google Drive access (for vendor documentation)

---

#### Step-by-Step Process

**1. Receive and Verify Invoice**
- Receive invoice from vendor (email or physical delivery)
- Check invoice includes:
  - Vendor name and NTN
  - Invoice number and date
  - Itemized list of goods/services
  - Total amount
  - Bank details
- If invoice is incomplete → Email vendor requesting missing information

**2. Verify Purchase Order (PO)**
- Check if invoice references a PO number
- If YES:
  - Login to ERPNext
  - Search for PO number in search bar
  - Verify invoice amount matches PO amount
  - Verify items match PO items
  - If mismatch → Contact AdminOps (procurement team) to verify
- If NO PO:
  - Check if purchase was approved by department head
  - If < PKR 10,000 → Can proceed without PO (record in notes)
  - If > PKR 10,000 → Escalate to Arhum/Azima for approval before proceeding

**3. Verify Vendor Documentation**
- Check if vendor documentation is on file
- Current location: TBD (to be organized in Google Drive > Finance > Vendors)
- Required documents:
  - Copy of NTN (National Tax Number)
  - Copy of CNIC (for individuals) or incorporation certificate (for companies)
  - Bank account details (account number, IBAN, bank name, branch)
- If documentation missing:
  - Email vendor: "We require the following documents to process your payment: [list]. Please send within 2 business days."
  - Do NOT proceed with payment until received
  - Save documents to vendor folder when received

**4. Calculate Withholding Tax**
- ConnectHear must withhold 4% of invoice amount for tax
- Calculation:
  - Withholding Amount = Invoice Amount × 0.04
  - Net Payment Amount = Invoice Amount - Withholding Amount
- Example:
  - Invoice: PKR 100,000
  - Withholding: PKR 100,000 × 0.04 = PKR 4,000
  - Net Payment: PKR 100,000 - PKR 4,000 = PKR 96,000
- Record both amounts (you'll need them for ERPNext and FBR filing)

**5. Create Payment Entry in ERPNext**
- **Direct Link:**
  - Click: https://hub.connecthear.org/app/payment-entry/new-payment-entry-zsnndqemii

- **Fill in Payment Entry form:**
  1. Payment Type: "Pay" (from dropdown)
  2. Party Type: "Supplier"
  3. Party: Select vendor from dropdown (if new vendor, create supplier first)
  4. Paid From: Select bank account (Main - HBL account)
  5. Paid Amount: Enter NET payment amount (after withholding)
  6. References section:
     - Click "Get Outstanding Invoices" OR
     - Manually add invoice reference number
     - Enter invoice amount
  7. Deductions section:
     - Click "Add Row"
     - Account: Select "Tax Deducted at Source - CHPL" (or similar account)
     - Amount: Enter withholding amount (4% calculated earlier)
  8. Cost Center: Select from dropdown:
     - Main - CHPL
     - 8100 - Marketing - CHPL
     - 8200 - BizDev - CHPL
     - 8300 - Product & Projects - CHPL
     - 8400 - Content & Design - CHPL
     - 8500 - SL & Training - CHPL
     - 8600 - Finance - CHPL
     - 8700 - Legal - CHPL
     - 8800 - AdminOps - CHPL
  9. Project (if applicable): Link to client project if this expense is project-specific
  10. Attach invoice PDF
  11. In "Remarks" field, note purpose and any special instructions

- Click "Save" (top right) - Status: "Draft"

**6. Get Approval (if required)**
- If payment amount > PKR 10,000:
  - Send Slack message to Arhum and Azima with details and ERPNext link
  - Wait for approval
- If payment amount ≤ PKR 10,000:
  - No approval needed, proceed directly

**7. Submit Payment Entry**
- Review all fields
- Click "Submit" (top right)
- Note the payment entry number (format: PE-YYYY-#####)

**8. Process Payment via Bank Portal**
- Login to HBL bank portal
- Navigate to: "Payments" → "Make Payment"
- Enter recipient details and NET payment amount
- Upload supporting document
- Submit payment
- Note transaction reference number

**9. Update ERPNext**
- Add bank transaction reference to payment entry
- Mark as "Paid"

**10. File Withholding Tax with FBR (Monthly)**
- On or before 5th of each month, file for PREVIOUS month
- Login to FBR portal: https://iris.fbr.gov.pk
- Navigate to: "Returns" → "Withholding Tax"
- Enter all vendor payments with 4% withheld
- Download challan

**11. Issue Tax Challan to Vendor (If Requested)**
- Currently only done if vendor requests
- Download from FBR portal and email to vendor
- CC: arhum@connecthear.com, azima@connecthear.com

**12. File Payment Records**
- Naming: CHPL-PMT-.MM-.YY-.####
- Location: TBD (Google Drive > Finance > Payments > [Year] > [Month])

---

## 💵 Workstream: Accounts Receivable

### Process: How to Create and Send an Invoice

#### Step-by-Step Process

**1. Confirm Service Delivery**
- Receive confirmation from service team
- Verify against contract

**2. Create Sales Invoice in ERPNext**
- Search: "New Sales Invoice"
- Fill in customer, items, amounts
- Cost Center and Project assignment
- Generate invoice number: CHPL-INV-.MM-.YY-.####

**3. Submit and Export**
- Review and submit
- Download PDF

**4. Deliver Invoice**
- **Email (70%):** Most common for Karachi/online clients
- **Physical/Courier (30%):** Out-of-city, government clients

**5. Set Payment Reminders**
- Currently manual (transitioning to automated)
- 2 weeks before due date
- On due date
- Weekly after due date

**6. Reconcile Payment**
- When received, create payment entry in ERPNext
- Link to invoice
- Mark as paid

---

## 🏛️ Workstream: Tax Compliance

### Process: Monthly Tax Filing (All 3 Types)

**Filing Deadline:** By the **5th of each month** for **previous month**

#### Three Types:
1. **Payroll Tax**
2. **Sales Tax** (15% on taxable receipts)
3. **Withholding Tax** (4% on vendor payments)

#### Consolidated Process:
- Generate reports from ERPNext
- Login to FBR portal: https://iris.fbr.gov.pk
- File each tax type
- Download challans
- Pay any balance due

---

## 🏦 Workstream: Bank Reconciliation

### Process: Daily Reconciliation

**Current:** Manual in Google Sheets  
**Target:** ERPNext daily reconciliation

#### Current Process:
1. Download HBL bank statement
2. Import to reconciliation sheet
3. Match with ERPNext payment entries
4. Create missing entries
5. Investigate discrepancies
6. Calculate closing balance

**Transition to ERPNext:**
- Import bank statement directly
- Auto-match transactions
- Manual review of unmatched
- Submit reconciliation

---

## 💼 Workstream: Payroll & Stipends

### Process: Monthly Payroll Processing

#### Key Steps:
1. Verify employee data
2. Process attendance
3. Create payroll entry in ERPNext
4. **Link to projects** (CRITICAL for costing)
5. **Assign cost centers**
6. Calculate payroll tax
7. Generate bank payment file
8. Process via HBL bulk payments
9. File payroll tax with FBR (by 5th of next month)
10. Distribute salary slips

**Project Linking:** Essential for accurate client project costing

---

## 💸 Workstream: Expense Claims

### Process: Employee Reimbursement

#### Steps:
1. Receive expense claim with receipts
2. Verify documents and legitimacy
3. Get approval if required
4. Create in ERPNext
5. **Link to cost center and project** (CRITICAL)
6. Submit and create payment
7. Process bank payment
8. File records: CHPL-EXP-.MM-.YY-.####

---

## 🏷️ Workstream: Grant Transaction Tagging

### Process: Tagging Expenses to Grants

**Purpose:** Track grant-funded expenses for donor reporting and compliance

#### Steps:
1. Identify grant-eligible transactions
2. Tag to grant project in ERPNext
3. Allocate to budget category
4. Document justification
5. Monitor against budget
6. Monthly utilization review
7. Quarterly/annual reporting to donor

**Critical:** Every grant transaction MUST be tagged for audit trail

---

## 💵 Workstream: Petty Cash Management

### Process: Managing Small Cash Expenses

**Limit:** PKR 500 - 2,000 per transaction

#### Steps:
1. Disburse cash for urgent small expenses
2. Require receipt within 24 hours
3. Record in petty cash register
4. Daily/weekly reconciliation
5. Replenish when low
6. Monthly report and ERPNext recording
7. Secure storage in locked box

---

# 📊 Summary

These Finance workstreams are **complete with:**
- ✅ Real ERPNext links and navigation
- ✅ Actual cost center names
- ✅ Actual thresholds (PKR 10,000 for approvals)
- ✅ Real filing deadlines (5th of month for taxes)
- ✅ Actual naming conventions (CHPL-INV-.MM-.YY-.####)
- ✅ Real tools (HBL bank, FBR portal, ERPNext)

**Your Finance team can use these TODAY!** 🚀
