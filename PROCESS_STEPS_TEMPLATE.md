# How to Write Effective Process Steps - Quick Guide

## 📝 Standard Template

```markdown
## Workstream: [Name]

### Process: [What you're doing]

#### Prerequisites
- System access needed
- Documents required

#### Step-by-Step Process

**1. [First Action]**
- Exactly what to do
- Where to click
- What to check

**2. [Next Action]**
...

#### Decision Points
**If X:** Then Y
**If A:** Then B

#### Common Issues & Solutions
**Issue:** [Problem]
**Solution:** [Fix]

#### Tools & Access Required
- System name (URL)
- Access level needed
```

## ✅ Good vs Bad Examples

### GOOD:
```
**3. Create Payment in ERPNext**
- Click: https://hub.connecthear.org/app/payment-entry/new
- Fill in:
  - Type: "Pay"
  - Supplier: Select vendor
  - Amount: PKR 48,000
- Click "Save" (top right)
- Status changes to "Draft"
```

### BAD:
```
**3. Create payment**
- Go to ERPNext and make a payment
```

## 🎯 Writing Rules

1. **Use active voice:** "Click Submit" not "Submit should be clicked"
2. **Be specific:** "Top right corner" not "somewhere on screen"
3. **Include exact names:** Field names, button labels as they appear
4. **Show calculations:** Formula + Example
5. **State outcomes:** "Status changes to..." "File is saved as..."

## 📊 Key Elements

### System Navigation
- Direct links when possible
- Menu path: Accounts → Payment → New
- Search alternative: "Type 'New Payment' in search"

### Decision Logic
```
Check amount:
→ If < 10,000: Proceed to step 5
→ If ≥ 10,000: Get approval, then step 5
```

### Calculations
```
Formula: Amount × 0.04 = Tax
Example: 100,000 × 0.04 = 4,000
```

## 🎓 How to Gather

**Ask person who does the work:**
1. "Walk me through it" - First step?
2. "Show me" - Screen share/sit together
3. "What if..." - All decision branches
4. "What goes wrong?" - Common problems
5. "What do you need?" - Systems, access, info

**Test it:**
- Give to someone new
- Watch them follow it
- Fix where they get stuck

## ✅ Quality Check

- [ ] Could a new hire follow this?
- [ ] All systems/links included?
- [ ] Decision points covered?
- [ ] Tested by walking through?
- [ ] Common problems addressed?

**Goal:** Someone can DO the work by following these steps, first time.
