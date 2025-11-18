# ConnectHear Operations Portal - Specification v2.0

**What's New:** Process Steps section added to workstreams  
**Base Spec:** SPEC.md (v1.0) - All original requirements still apply  
**This Document:** Only the ADDITIONS/CHANGES for v2.0

---

## 🎯 What Changed in v2.0

**Added:** Step-by-step process instructions for each workstream

**Why:** Makes Operations Bible actually usable:
- New hires can follow step-by-step
- No need to ask "how do I do this?"
- Reduces training time
- Creates true SOP manual

---

## 📊 Updated Data Structure

### v2.0 Workstream Object

```json
{
  "id": "accounts-payable",
  "name": "Accounts Payable",
  "description": "Process all outgoing payments...",
  "frequency": "Weekly",
  "output": ["List", "of", "outputs"],
  "dependencies": [{"team": "AdminOps", "reason": "for PO verification"}],
  "raci": [{"role": "Finance", "r": true, "a": false, "c": false, "i": false}],
  "notes": ["Note 1", "Note 2"],
  
  // NEW in v2.0:
  "process_steps": {
    "steps": [
      {
        "number": 1,
        "title": "Receive and Verify Invoice",
        "details": [
          "Check invoice includes vendor name, NTN, amount",
          "If incomplete → Email vendor"
        ]
      },
      {
        "number": 2,
        "title": "Verify Purchase Order",
        "details": ["Search ERPNext for PO", "Verify amounts match"]
      }
    ],
    "decision_points": [
      {
        "condition": "If amount > PKR 10,000",
        "action": "Get approval from Arhum/Azima"
      }
    ],
    "common_issues": [
      {
        "issue": "Payment fails at bank",
        "solution": "Check balance, verify details, retry"
      }
    ],
    "tools": ["ERPNext", "HBL Bank Portal", "FBR Portal"],
    "related_workstreams": ["Tax Compliance", "Bank Reconciliation"]
  }
}
```

---

## 🔍 Parser Updates

### New Parsing Function

```python
def parse_process_steps(content_lines: list) -> dict:
    """
    Parse the **Process Steps:** section
    Returns structured process_steps object
    """
    pass
```

### What to Extract

**1. Main Steps (numbered with ####)**
```markdown
#### 1. Receive and Verify Invoice
- Detail 1
- Detail 2
```
Parse as:
```json
{
  "number": 1,
  "title": "Receive and Verify Invoice",
  "details": ["Detail 1", "Detail 2"]
}
```

**2. Decision Points**
```markdown
#### Decision Points
**If X:** Then Y
**If A:** Then B
```
Parse as:
```json
{
  "decision_points": [
    {"condition": "If X", "action": "Then Y"},
    {"condition": "If A", "action": "Then B"}
  ]
}
```

**3. Common Issues**
```markdown
#### Common Issues
**Issue:** Problem description
**Solution:** How to fix
```
Parse as:
```json
{
  "common_issues": [
    {"issue": "Problem description", "solution": "How to fix"}
  ]
}
```

---

## 🎨 Generator Updates

### HTML Template for Process Steps

```html
<div class="process-steps">
  <h4>How to Do This:</h4>
  
  <div class="steps-list">
    <div class="step">
      <div class="step-number">1</div>
      <div class="step-content">
        <h5>Receive and Verify Invoice</h5>
        <ul>
          <li>Check invoice includes vendor name, NTN</li>
          <li>If incomplete → Email vendor</li>
        </ul>
      </div>
    </div>
    <!-- Repeat for each step -->
  </div>
  
  <div class="decision-points">
    <h5>Decision Points</h5>
    <div class="decision">
      <strong>If amount > PKR 10,000:</strong>
      <span>Get approval from Arhum/Azima</span>
    </div>
  </div>
  
  <div class="common-issues">
    <h5>Common Issues</h5>
    <div class="issue-solution">
      <p class="issue"><strong>Issue:</strong> Payment fails</p>
      <p class="solution"><strong>Solution:</strong> Check balance...</p>
    </div>
  </div>
</div>
```

### CSS Additions

```css
.process-steps {
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin-top: 1.5rem;
}

.steps-list {
  margin: 1rem 0;
}

.step {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.step-number {
  background: var(--primary-color);
  color: white;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  flex-shrink: 0;
}

.step-content h5 {
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.decision-points, .common-issues {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
}

.decision {
  background: white;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
  border-left: 3px solid var(--accent-color);
}

.issue-solution {
  background: white;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
  border-left: 3px solid #f59e0b;
}
```

---

## 🔧 Implementation Notes

### Parser Logic

**1. Detect Process Steps Section**
```python
if line.startswith('**Process Steps:**'):
    # Start capturing process steps
    in_process_steps = True
```

**2. Parse Numbered Steps**
```python
if line.startswith('#### ') and line[5].isdigit():
    # This is a step header
    # Extract number and title
```

**3. Capture Details**
```python
# Lines starting with "- " are details
# Lines starting with "→" or "If" are decision logic
```

**4. Identify Subsections**
```python
if '#### Decision Points' in line:
    # Switch to decision points parsing
if '#### Common Issues' in line:
    # Switch to issues parsing
```

### Generator Logic

**1. Check if workstream has process_steps**
```python
if workstream.get('process_steps'):
    html += generate_process_steps_html(workstream['process_steps'])
```

**2. Generate collapsible section** (optional)
```python
# Can make process steps expandable/collapsible
# Default: Expanded (always visible)
```

---

## 📋 Markdown Format Specification

### Standard Format

```markdown
**Process Steps:**

#### 1. Step Title
- Detail line
- Another detail
- If X → Then Y (decision logic inline)

#### 2. Next Step
- Details...

#### Decision Points
**If condition:** Action to take
**If other condition:** Other action

#### Common Issues
**Issue:** Problem description
**Solution:** How to fix
**Prevention:** How to avoid (optional)

#### Tools & Access
- Tool name (URL)
- Access level required

#### Related Workstreams
- Workstream name (Department): Brief note
```

### Allowed Variations

**Step numbering:** Can skip numbers, parser should handle
**Decision format:** Can be in steps or separate section
**Issues format:** Can include or omit Prevention line

---

## ✅ Testing Requirements

### Parser Tests

```python
def test_parse_process_steps():
    """Test process steps extraction"""
    sample = """
    **Process Steps:**
    
    #### 1. First Step
    - Detail one
    - Detail two
    
    #### Decision Points
    **If X:** Do Y
    """
    result = parse_process_steps(sample)
    assert len(result['steps']) == 1
    assert result['steps'][0]['title'] == 'First Step'
    assert len(result['decision_points']) == 1
```

### Generator Tests

```python
def test_generate_process_steps_html():
    """Test HTML generation for process steps"""
    data = {
        'steps': [{'number': 1, 'title': 'Test', 'details': ['A', 'B']}],
        'decision_points': [{'condition': 'If X', 'action': 'Do Y'}]
    }
    html = generate_process_steps_html(data)
    assert '<div class="process-steps">' in html
    assert '<div class="step-number">1</div>' in html
```

---

## 🎯 Backward Compatibility

**v1.0 workstreams (without process steps):**
- Should still parse correctly
- HTML generation should skip process steps section if not present
- No errors or warnings

**Migration path:**
- v1.0 Operations Bible still works
- Add process steps gradually
- Rebuild HTML as sections are added

---

## 📈 Success Criteria

**Parser:**
- [ ] Extracts all numbered steps
- [ ] Captures step details (bullet points)
- [ ] Identifies decision points
- [ ] Extracts common issues
- [ ] Handles missing sections gracefully

**Generator:**
- [ ] Creates numbered step layout
- [ ] Renders decision points clearly
- [ ] Displays issues with solutions
- [ ] Styling matches portal design
- [ ] Mobile responsive

**End-to-End:**
- [ ] Finance workstreams display complete steps
- [ ] Can follow steps from HTML portal
- [ ] Search includes process step content
- [ ] No broken formatting

---

## 🚀 Deployment

**Phase 1: Finance (Now)**
- Add process steps to Finance workstreams
- Test parser and generator
- Deploy and validate

**Phase 2: BD (After Ahmed)**
- Add BD process steps
- Rebuild and test

**Phase 3: All Others (Ongoing)**
- Add as departments are documented
- Incremental updates

---

## 📝 Summary of Changes

**v1.0 → v2.0:**
- ✅ Added process_steps object to workstream data structure
- ✅ Added parser function for Process Steps section
- ✅ Added HTML template for step-by-step display
- ✅ Added CSS for process steps styling
- ✅ All v1.0 features remain unchanged
- ✅ Backward compatible

**Result:** Operations Bible becomes true SOP manual with actionable instructions! 🎉

---

**For full v1.0 specification, see:** SPEC.md  
**For implementation guide, see:** DEVELOPER_GUIDE.md  
**For markdown updates, see:** MARKDOWN_UPDATE_GUIDE.md
