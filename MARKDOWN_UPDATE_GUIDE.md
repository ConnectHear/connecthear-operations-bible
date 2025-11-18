# How to Add Process Steps to Operations Bible

**Quick Guide:** Adding step-by-step instructions to your markdown and rebuilding the HTML portal

---

## 📝 Step 1: Update Your Markdown File

### Format for Adding Process Steps

In your `ConnectHear_Operations_Bible_v2.md`, add a new section under each workstream:

```markdown
### Workstream: Accounts Payable

**Description:** Process all outgoing payments to vendors...

**Frequency:** Weekly

**Output:**
- Vendor payments processed
- Withholding tax filed

**Dependencies:**
- AdminOps (for PO verification)

**RACI:**
[existing table]

**Process Steps:**

#### 1. Receive and Verify Invoice
- Check invoice includes vendor name, NTN, amount, bank details
- If incomplete → Email vendor for missing info

#### 2. Verify Purchase Order
- Search ERPNext for PO number
- Verify amounts match
- If < PKR 10,000 and no PO → Can proceed
- If > PKR 10,000 and no PO → Get approval from Arhum/Azima

#### 3. Calculate Withholding Tax
- Formula: Invoice Amount × 0.04 = Withholding
- Example: PKR 100,000 × 0.04 = PKR 4,000
- Net Payment = PKR 96,000

#### 4. Create Payment Entry in ERPNext
- Click: https://hub.connecthear.org/app/payment-entry/new
- Fill in: Type (Pay), Supplier, Amount (net after withholding)
- Select Cost Center from: Main, 8100-Marketing, 8200-BizDev, etc.
- Save as Draft

[Continue with remaining steps...]

#### Decision Points
**If amount > PKR 10,000:** Get approval from Arhum/Azima via Slack
**If vendor docs missing:** Stop and request documents

#### Common Issues
**Issue:** Payment fails at bank
**Solution:** Check balance, verify bank details, retry or contact vendor

**Key Process Notes:** [existing notes]
```

### Where to Insert

The `**Process Steps:**` section goes:
- **After** RACI table
- **Before** existing "Key Process Notes"

---

## 🔄 Step 2: Copy from Finance Template

For Finance workstreams, you can copy directly from:
- **File:** `PROCESS_STEPS_FINANCE.md`
- **Contains:** Complete, detailed steps for all Finance workstreams

**Example:**
1. Open `PROCESS_STEPS_FINANCE.md`
2. Find "Workstream: Accounts Payable"
3. Copy the entire "Step-by-Step Process" section
4. Paste into your markdown under `**Process Steps:**`
5. Adjust formatting if needed (add #### for step headers)

---

## 🔄 Step 3: For Other Departments

For BD and other departments:
- **Use:** `PROCESS_STEPS_STRUCTURE.md` as template
- **Fill in** the [AHMED: ...] and [DETAILS NEEDED] placeholders
- **Follow format** from Finance examples

---

## 🛠️ Step 4: Rebuild the HTML

Once you've updated the markdown:

### Option A: If You Have Claude Code Project Set Up

```bash
# Navigate to project folder
cd connecthear-operations-portal

# Run build script
python build.py

# Output will be: output/index.html
```

### Option B: Manual Update

If you don't have the automated build yet:
1. The existing HTML generator should pick up the new `**Process Steps:**` section
2. Or: manually add process steps to the HTML template

---

## 📋 Quick Update Checklist

For each workstream you're adding process steps to:

- [ ] Add `**Process Steps:**` section in markdown
- [ ] Include numbered steps (#### 1., #### 2., etc.)
- [ ] Add Decision Points section
- [ ] Add Common Issues section
- [ ] Include exact system links (ERPNext, FBR, etc.)
- [ ] Specify thresholds (PKR 10,000 for approvals, etc.)
- [ ] Note tools and access required
- [ ] Test: Can someone follow these steps?

---

## 🎯 Priority Order

**Do these first:**
1. ✅ Finance workstreams (use PROCESS_STEPS_FINANCE.md - ready now)
2. ⏳ BD workstreams (after Ahmed responds)
3. ⏳ Sign Language workstreams (after Ismail interview)
4. ⏳ Other departments (as you gather with HODs)

---

## 💡 Tips

### Keep It Organized
- One workstream at a time
- Complete all sections before moving to next
- Test the steps by walking through them

### Use Real Examples
- Show calculations: "PKR 100,000 × 0.04 = PKR 4,000"
- Give exact navigation: "Click link: https://..."
- Specify exact field names from ERPNext

### Format Consistently
```markdown
#### Step Number: Action Name
- Detail line 1
- Detail line 2
- If X → Then Y
```

### Link Related Workstreams
At end of process steps:
```markdown
**Related Workstreams:**
- Tax Compliance (Finance): For monthly withholding tax filing
- Bank Reconciliation (Finance): For payment confirmation
```

---

## 🚀 Result

Once complete, your Operations Bible will have:
- ✅ WHAT each workstream is (Description)
- ✅ WHO does it (RACI)
- ✅ WHEN it happens (Frequency)
- ✅ WHAT you produce (Output)
- ✅ **HOW to actually DO it** (Process Steps) ⭐ NEW!

And your HTML portal will display it all beautifully with:
- Expandable process steps sections
- Easy-to-follow numbered lists
- Searchable (find by system name, step keyword, etc.)

**This transforms your Operations Bible from documentation into a true SOP manual!** 🎉
