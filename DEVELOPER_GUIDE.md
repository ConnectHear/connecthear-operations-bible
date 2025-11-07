# ConnectHear Operations Portal - Developer Guide

## 🚀 Quick Start for Claude Code

Hey Claude Code! Welcome to the ConnectHear Operations Portal project. This guide will help you understand the project and get started quickly.

---

## 📋 What You're Building

**Goal:** Transform a 200-page markdown document into an interactive HTML web portal.

**Input:** `ConnectHear_Operations_Bible_v2.md` (structured markdown)  
**Output:** `index.html` (single self-contained HTML file)

**Key Features:**
- Collapsible sidebar navigation (3-level hierarchy)
- Real-time search across all content
- RACI table parsing and display
- Deep linking (shareable URLs to specific sections)
- Mobile responsive
- Works offline (no backend needed)

---

## 📁 Files You Have

1. **`SPEC.md`** ← READ THIS FIRST!
   - Complete technical specification
   - Data structures, requirements, implementation details
   - Everything you need to know

2. **`ConnectHear_Operations_Bible_v2.md`**
   - Source markdown file (currently ~60 pages)
   - Contains Business Development and Finance & Compliance departments
   - More departments to be added later

3. **`operations_bible.html`**
   - Demo/prototype HTML (incomplete content)
   - Use as design reference only

4. **`README_HTML_Portal.md`**
   - End-user documentation
   - How to use the final product

---

## 🎯 Your Mission

Build a Python-based system that:

1. **Parses** the markdown file into structured JSON
2. **Generates** a complete HTML portal from that JSON
3. **Embeds** all CSS and JavaScript inline (single file output)
4. **Includes** ALL content from the markdown (nothing missing!)

---

## 🏗️ Recommended Architecture

```
operations-portal/
├── src/
│   ├── parser.py          # YOU BUILD THIS - Parse markdown → JSON
│   ├── generator.py       # YOU BUILD THIS - Generate JSON → HTML
│   ├── templates/
│   │   ├── base.html      # HTML template
│   │   ├── styles.css     # CSS styles
│   │   └── scripts.js     # JavaScript code
│   └── utils.py           # Shared utilities
├── input/
│   └── ConnectHear_Operations_Bible_v2.md  # Source file
├── output/
│   └── index.html         # Generated portal (your output)
├── tests/
│   ├── test_parser.py     # Test your parser
│   └── test_generator.py  # Test your generator
├── build.py               # Main build script
├── requirements.txt       # Python dependencies (should be minimal!)
└── README.md             # Project README
```

---

## 🔨 Implementation Steps

### Step 1: Set Up Project Structure
```bash
# Create directories
mkdir -p src/templates tests input output

# Copy the markdown file to input/
cp ConnectHear_Operations_Bible_v2.md input/

# Create empty Python files
touch src/parser.py src/generator.py src/utils.py
touch tests/test_parser.py tests/test_generator.py
touch build.py
```

### Step 2: Build the Parser (`src/parser.py`)

**What it does:**
- Reads markdown file
- Extracts hierarchy: Departments → Areas → Workstreams
- Parses workstream content: description, frequency, output, dependencies, RACI table, notes
- Outputs structured JSON

**Key functions to implement:**
```python
def parse_markdown(file_path: str) -> dict:
    """Main entry point - returns full JSON structure"""

def extract_departments(lines: list) -> list:
    """Find all '# N. 🔷 Department Name' headers"""

def extract_areas(lines: list) -> list:
    """Find all '## 📍 Area: Name' headers"""

def extract_workstreams(lines: list) -> list:
    """Find all '### Workstream: Name' headers"""

def parse_workstream_content(lines: list) -> dict:
    """Parse content between workstream headers"""

def parse_raci_table(lines: list) -> list:
    """Parse markdown table into structured data"""
```

**Test it:**
```python
# Should parse this:
"""
### Workstream: Lead Sourcing

**Description:** Text here...
**Frequency:** Weekly
**RACI:**
| Role | R | A |
|------|---|---|
| Person | ✅ | |
"""

# Into this:
{
  "name": "Lead Sourcing",
  "description": "Text here...",
  "frequency": "Weekly",
  "raci": [{"role": "Person", "r": true, "a": false}]
}
```

### Step 3: Build the Generator (`src/generator.py`)

**What it does:**
- Takes JSON from parser
- Generates complete HTML file
- Inlines CSS and JavaScript
- Creates navigation tree
- Creates workstream cards

**Key functions to implement:**
```python
def generate_html(data: dict, output_path: str):
    """Main entry point - creates HTML file"""

def generate_navigation(departments: list) -> str:
    """Generate sidebar HTML"""

def generate_workstream_card(workstream: dict) -> str:
    """Generate workstream content HTML"""

def generate_raci_table(raci: list) -> str:
    """Generate RACI table HTML"""

def inline_css() -> str:
    """Return CSS to embed"""

def inline_javascript() -> str:
    """Return JavaScript to embed"""
```

### Step 4: Create Templates

**`templates/base.html`** - HTML structure  
**`templates/styles.css`** - All styling  
**`templates/scripts.js`** - All JavaScript (navigation, search, routing)

See `operations_bible.html` for design reference.

### Step 5: Build Script

**`build.py`** - Main build script:
```python
from src.parser import parse_markdown
from src.generator import generate_html

# Parse markdown
data = parse_markdown('input/ConnectHear_Operations_Bible_v2.md')

# Generate HTML
generate_html(data, 'output/index.html')

print("✅ Build complete!")
```

### Step 6: Test Everything

```bash
# Run tests
python -m pytest tests/

# Build
python build.py

# Open in browser
open output/index.html
```

---

## 🎨 Design Requirements

**Reference:** Look at `operations_bible.html` for visual design

**Key design elements:**
- Clean, professional aesthetic
- Blue color scheme (#2563eb primary)
- Ample white space
- Clear hierarchy
- Readable typography
- Hover effects for interactivity

**Must-haves:**
- Fixed header with search bar
- Fixed sidebar with scroll
- Collapsible navigation items
- Workstream cards with clear sections
- Styled RACI tables
- Breadcrumbs for navigation
- Responsive design

---

## 🐛 Common Pitfalls to Avoid

1. **Missing Content**
   - Make sure EVERY workstream from markdown appears in HTML
   - Don't skip content that's hard to parse - include it as raw markdown if needed

2. **Broken Navigation**
   - Test that clicking every nav item works
   - Test that expand/collapse works for all departments

3. **Search Not Working**
   - Search needs to work across all text, not just titles
   - Test with real queries: "Umaima", "Monthly", "RACI"

4. **RACI Tables**
   - These are in markdown table format - parse carefully
   - Handle empty cells correctly (no checkmark = false)

5. **Special Characters**
   - Preserve emojis (🔷 📍 ✅)
   - Handle markdown special chars (**, *, -, →)

6. **Performance**
   - With 200+ workstreams, ensure smooth scrolling
   - Lazy load content if needed
   - Keep search fast (< 100ms)

---

## 📊 How to Verify Success

### Checklist for Complete Build

**Parser Output:**
- [ ] JSON file is created
- [ ] All 2 departments present (BD, Finance)
- [ ] All areas present (12+ areas total)
- [ ] All workstreams present (50+ workstreams total)
- [ ] All RACI tables parsed correctly
- [ ] All frequencies extracted
- [ ] All dependencies captured

**HTML Output:**
- [ ] Single HTML file created
- [ ] File size reasonable (< 5MB)
- [ ] Opens in browser without errors
- [ ] All departments visible in sidebar
- [ ] Navigation expands/collapses correctly
- [ ] Search bar works
- [ ] All workstreams clickable and display content
- [ ] RACI tables render correctly
- [ ] Breadcrumbs update when navigating
- [ ] Responsive on mobile (test in DevTools)

**Content Verification:**
- [ ] Spot-check: Search for "Umaima" → should show all her workstreams
- [ ] Spot-check: Click "Business Development" → should expand
- [ ] Spot-check: Click "Lead Sourcing & Tracking" → should show full content
- [ ] Spot-check: RACI table has checkmarks in right places
- [ ] No "undefined" or "null" displayed anywhere

---

## 🚦 Testing Strategy

### Unit Tests

```python
# tests/test_parser.py
def test_parse_department():
    """Test department extraction"""
    sample = "# 1. 🔷 Business Development"
    result = extract_departments([sample])
    assert result[0]['name'] == 'Business Development'

def test_parse_raci_table():
    """Test RACI table parsing"""
    sample = """
| Role | R | A |
|------|---|---|
| Person | ✅ | |
"""
    result = parse_raci_table(sample.split('\n'))
    assert result[0]['role'] == 'Person'
    assert result[0]['responsible'] == True
    assert result[0]['accountable'] == False
```

### Integration Test

```python
def test_full_build():
    """Test complete build process"""
    # Parse
    data = parse_markdown('input/test_sample.md')
    
    # Generate
    generate_html(data, 'output/test.html')
    
    # Verify
    with open('output/test.html', 'r') as f:
        html = f.read()
        assert 'Business Development' in html
        assert '<table' in html  # RACI tables exist
        assert 'class="sidebar"' in html  # Navigation exists
```

---

## 💡 Pro Tips

1. **Start Small**
   - Parse just ONE workstream first
   - Get that perfect, then scale up

2. **Use Regex Carefully**
   - Markdown has special characters
   - Test regex with edge cases

3. **Debug with Print**
   - Print what you're parsing at each step
   - Makes debugging much easier

4. **Reference the Spec**
   - SPEC.md has EVERYTHING
   - Data structures, examples, edge cases

5. **Test in Browser Early**
   - Don't wait until everything is done
   - Generate HTML early, even if incomplete
   - See what it looks like

---

## 🆘 Need Help?

**Stuck on parsing?**
- Check SPEC.md Section 7 (Parser Implementation)
- Look at the markdown file structure
- Start with simple regex matches

**Stuck on HTML generation?**
- Look at `operations_bible.html` for structure
- Copy the CSS/JS, then customize
- Generate simple HTML first, add complexity later

**Stuck on JavaScript?**
- Check SPEC.md Section 9 (JavaScript Functionality)
- Start with basic show/hide for sections
- Add search and routing later

**Something unclear in spec?**
- The spec is comprehensive but ask if confused
- Better to clarify than build wrong thing

---

## 🎯 Success Criteria

**You've succeeded when:**
1. ✅ You can run `python build.py`
2. ✅ It creates `output/index.html`
3. ✅ You open it in a browser
4. ✅ You see all departments in sidebar
5. ✅ You can click any workstream and see full content
6. ✅ Search works (try "Umaima", "RACI", "Monthly")
7. ✅ No content is missing from the markdown file
8. ✅ It looks professional and works on mobile

**Deliver:** One perfect `index.html` file that Talal can share with his team.

---

## 🚀 Let's Build!

You have:
- ✅ Complete spec (SPEC.md)
- ✅ Source markdown file
- ✅ Design reference (operations_bible.html)
- ✅ This developer guide

**Now go build something awesome!** 

Start with the parser, test it thoroughly, then move to the generator. Take it step by step and you'll have a beautiful operations portal in no time.

Good luck! 🎉
