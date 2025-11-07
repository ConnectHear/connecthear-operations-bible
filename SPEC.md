# ConnectHear Operations Portal - Technical Specification

**Version:** 1.0  
**Date:** November 2025  
**Project Type:** Static HTML/CSS/JavaScript Web Application  
**Target Platform:** Modern web browsers (Chrome, Firefox, Safari, Edge)  
**Development Tool:** Claude Code

---

## 1. PROJECT OVERVIEW

### 1.1 Purpose
Transform a 200+ page markdown Operations Bible into an interactive, searchable, navigable HTML web portal that makes it easy for ConnectHear team members to find and reference operational processes.

### 1.2 Goals
- **Usability:** Enable instant navigation to any department/area/workstream
- **Searchability:** Real-time search across all content
- **Maintainability:** Easy to update from markdown source
- **Accessibility:** Works offline, no backend required
- **Scalability:** Handles 8 departments × 40+ areas × 200+ workstreams
- **Professional:** Clean, modern design suitable for enterprise use

### 1.3 Source Material
- **Input File:** `ConnectHear_Operations_Bible_v2.md` (provided)
- **Format:** Markdown with specific hierarchy structure
- **Size:** ~200+ pages when complete, currently ~60 pages (BD + Finance complete)

---

## 2. TECHNICAL ARCHITECTURE

### 2.1 Technology Stack
- **Frontend:** Pure HTML5, CSS3, JavaScript (ES6+)
- **No Dependencies:** Zero external libraries (no jQuery, React, etc.)
- **Data Format:** JSON embedded in HTML or separate JSON file
- **Build Process:** Python script to parse markdown → generate HTML

### 2.2 Architecture Pattern
```
┌─────────────────────────────────────────────────────────────┐
│                     Input Layer                              │
│  ConnectHear_Operations_Bible_v2.md (Markdown Source)       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Processing Layer                           │
│  Python Parser: markdown → structured JSON                   │
│  - Department hierarchy extraction                           │
│  - Content parsing (RACI, lists, tables)                     │
│  - Metadata extraction (frequency, owners)                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                 Generation Layer                             │
│  HTML Generator: JSON → static HTML site                     │
│  - Navigation tree generation                                │
│  - Content section generation                                │
│  - Search index building                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                 Presentation Layer                           │
│  Static HTML + CSS + JavaScript                              │
│  - Collapsible navigation                                    │
│  - Real-time search                                          │
│  - Responsive design                                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. DATA STRUCTURE

### 3.1 Markdown Hierarchy
The source markdown follows this strict hierarchy:

```markdown
# N. 🔷 Department Name

## 📍 Area: Area Name

### Workstream: Workstream Name

**Description:** Text here...

**Frequency:** Daily/Weekly/Monthly/etc.

**Output:**
- Bullet point
- Bullet point

**Dependencies:**
- Department/Team (for explanation)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Name | ✅ | | | |

**Key Process Notes:** or **Critical Implementation Requirements:** or **Implementation Note:**
- Note 1
- Note 2
```

### 3.2 Target JSON Structure

```json
{
  "departments": [
    {
      "id": "business-development",
      "name": "Business Development",
      "emoji": "🔷",
      "areas": [
        {
          "id": "partnerships-sales",
          "name": "Partnerships & Sales",
          "emoji": "📍",
          "workstreams": [
            {
              "id": "lead-sourcing",
              "name": "Lead Sourcing & Tracking",
              "description": "Full description text...",
              "frequency": "Weekly (CRM updates), Daily (new lead logging)",
              "output": [
                "Updated CRM sheet with all leads",
                "Lead status tracking with pipeline stages"
              ],
              "dependencies": [
                {
                  "team": "Marketing",
                  "reason": "for social media traffic and campaigns"
                }
              ],
              "raci": [
                {
                  "role": "BD Associate (Hiba/Ahmed)",
                  "responsible": true,
                  "accountable": false,
                  "consulted": false,
                  "informed": false
                }
              ],
              "notes": [
                {
                  "title": "Indirect Lead Scenarios",
                  "content": ["Point 1", "Point 2"]
                }
              ],
              "content_raw": "Full markdown content for this workstream"
            }
          ]
        }
      ]
    }
  ],
  "metadata": {
    "version": "2.0",
    "last_updated": "November 2025",
    "total_departments": 8,
    "total_areas": 45,
    "total_workstreams": 200
  }
}
```

---

## 4. FILE STRUCTURE

### 4.1 Project Directory
```
operations-portal/
├── src/
│   ├── parser.py              # Markdown → JSON parser
│   ├── generator.py           # JSON → HTML generator
│   └── templates/
│       ├── base.html          # Main HTML template
│       ├── styles.css         # CSS styles
│       └── scripts.js         # JavaScript functionality
├── input/
│   └── ConnectHear_Operations_Bible_v2.md
├── output/
│   ├── index.html             # Generated portal
│   ├── data.json              # Extracted data (optional)
│   └── assets/
│       ├── styles.css         # Compiled CSS
│       └── scripts.js         # Compiled JS
├── tests/
│   ├── test_parser.py
│   └── test_generator.py
├── README.md
├── requirements.txt
└── build.sh                   # Build script
```

### 4.2 Generated Output
- **Single HTML file** (preferred): All CSS/JS inlined, self-contained
- **Alternative:** HTML + separate CSS/JS files

---

## 5. FUNCTIONAL REQUIREMENTS

### 5.1 Navigation System

#### 5.1.1 Sidebar Navigation
- **Left sidebar:** Fixed, scrollable, 320px wide
- **Hierarchy display:**
  - Level 1: Departments (🔷 icon + name) - **Bold, collapsible**
  - Level 2: Areas (📍 icon + name) - **Indented, collapsible**
  - Level 3: Workstreams (name only) - **Indented, clickable**
- **Collapse/Expand behavior:**
  - Click department → toggle all areas
  - Click area → toggle workstreams
  - Visual indicator: ▶ (collapsed) / ▼ (expanded)
- **Active state:** Highlight currently viewed workstream
- **Smooth scrolling:** Animate sidebar scroll to active item

#### 5.1.2 Content Display
- **Main content area:** Flex-grow, scrollable, padding 2-3rem
- **Show/hide behavior:** Only display selected workstream content
- **Default view:** Welcome/home screen with overview
- **Breadcrumbs:** Always show current location path
- **Scroll to top:** When switching workstreams

### 5.2 Search Functionality

#### 5.2.1 Search Input
- **Location:** Top right of header, 400px wide
- **Placeholder:** "Search workstreams, owners, departments..."
- **Real-time filtering:** Search as user types (debounce 300ms)
- **Clear button:** X to clear search

#### 5.2.2 Search Algorithm
Search across:
- Department names
- Area names
- Workstream names
- Workstream descriptions
- Owner names (RACI roles)
- Frequency values
- Dependencies

**Matching logic:**
- Case-insensitive
- Partial word matching
- Highlight matching text in results
- Rank by relevance (title matches > content matches)

#### 5.2.3 Search Results Display
- **In navigation:** Show only matching items, expand parents
- **In content:** Option to show all matches on one page
- **Result count:** "Showing 12 results for 'Umaima'"
- **Clear indication:** Dim non-matching items

### 5.3 Content Rendering

#### 5.3.1 Workstream Card Layout
Each workstream displayed as a card with sections:

1. **Header:** Workstream name (large, bold)
2. **Metadata bar:** Frequency and Owner tags
3. **Description:** Full text with formatting
4. **Output:** Bulleted list
5. **Dependencies:** List with team names highlighted
6. **RACI Table:** Full table with checkmarks
7. **Notes/Requirements:** Expandable sections for long content

#### 5.3.2 Content Formatting
- **Markdown rendering:**
  - `**bold**` → `<strong>`
  - `*italic*` → `<em>`
  - Bulleted lists → `<ul><li>`
  - Numbered lists → `<ol><li>`
  - Tables → HTML `<table>` with styling
- **Special handling:**
  - Process flows with arrows preserved
  - Code blocks with syntax highlighting (if present)
  - Links made clickable

#### 5.3.3 RACI Tables
- **Styling:** Professional table with header row
- **Header colors:** Blue background for visibility
- **Checkmarks:** ✅ rendered clearly
- **Hover effects:** Row highlighting
- **Responsive:** Horizontal scroll on small screens

### 5.4 Responsive Design

#### 5.4.1 Desktop (>1024px)
- Sidebar: 320px fixed width
- Content: Remaining space
- Two-column layout

#### 5.4.2 Tablet (768px - 1024px)
- Sidebar: 280px
- Content: Adjust accordingly
- Maintain two-column layout

#### 5.4.3 Mobile (<768px)
- Sidebar: Hidden by default, slide-in drawer
- Hamburger menu button to toggle sidebar
- Content: Full width
- Search: Full width in header

### 5.5 URL Handling

#### 5.5.1 Deep Linking
- **Format:** `index.html#department-area-workstream`
- **Example:** `index.html#business-development-partnerships-sales-lead-sourcing`
- **Behavior:** 
  - Auto-expand parent department/area
  - Scroll to workstream
  - Update breadcrumbs

#### 5.5.2 Sharing
- Copy link button for each workstream
- Shareable URLs work even when sent via email/Slack
- Hash-based navigation (no server routing needed)

---

## 6. NON-FUNCTIONAL REQUIREMENTS

### 6.1 Performance
- **Initial load:** < 2 seconds on average connection
- **Search response:** < 100ms for any query
- **Navigation:** Instant (no perceptible delay)
- **File size:** < 5MB total (for 200+ workstreams)

### 6.2 Browser Support
- **Chrome:** 90+
- **Firefox:** 88+
- **Safari:** 14+
- **Edge:** 90+
- **Mobile browsers:** iOS Safari, Chrome Android

### 6.3 Accessibility
- **Keyboard navigation:** Tab through all interactive elements
- **Screen reader:** ARIA labels for navigation
- **Contrast:** WCAG AA compliance
- **Focus indicators:** Clear visual focus states

### 6.4 Offline Capability
- **No server required:** All resources embedded or inline
- **Works from file system:** Can open file:/// URLs
- **No external dependencies:** No CDN, no API calls

---

## 7. PARSER IMPLEMENTATION

### 7.1 Markdown Parser (`parser.py`)

#### 7.1.1 Core Functions

```python
def parse_operations_bible(md_file_path: str) -> dict:
    """
    Main parsing function
    Returns structured JSON matching schema in section 3.2
    """
    pass

def extract_departments(lines: list) -> list:
    """
    Extract all department sections
    Looks for: # N. 🔷 Department Name
    """
    pass

def extract_areas(dept_lines: list) -> list:
    """
    Extract all areas within a department
    Looks for: ## 📍 Area: Area Name
    """
    pass

def extract_workstreams(area_lines: list) -> list:
    """
    Extract all workstreams within an area
    Looks for: ### Workstream: Workstream Name
    """
    pass

def parse_workstream_content(content_lines: list) -> dict:
    """
    Parse workstream content into structured sections:
    - description
    - frequency
    - output
    - dependencies
    - raci
    - notes
    """
    pass

def parse_raci_table(table_lines: list) -> list:
    """
    Parse RACI markdown table into structured data
    """
    pass

def extract_frequency(content: str) -> str:
    """
    Extract frequency from "**Frequency:** Daily/Weekly/etc."
    """
    pass

def extract_owner(raci_data: list) -> str:
    """
    Extract primary owner from RACI (who has R or A)
    """
    pass

def markdown_to_html(md_text: str) -> str:
    """
    Convert markdown formatting to HTML
    - **bold** → <strong>
    - *italic* → <em>
    - Lists → <ul>/<ol>
    - Preserve structure
    """
    pass
```

#### 7.1.2 Parsing Logic

**Step 1: Split by Departments**
```python
# Regex: ^# \d+\. 🔷 (.+)$
# This captures: "# 1. 🔷 Business Development"
```

**Step 2: Within each department, split by Areas**
```python
# Regex: ^## 📍 Area: (.+)$
# This captures: "## 📍 Area: Partnerships & Sales"
```

**Step 3: Within each area, split by Workstreams**
```python
# Regex: ^### Workstream: (.+)$
# This captures: "### Workstream: Lead Sourcing & Tracking"
```

**Step 4: Parse workstream content**
- Look for `**Description:**` → capture until next `**` marker
- Look for `**Frequency:**` → capture text on same line
- Look for `**Output:**` → capture bulleted list until next section
- Look for `**Dependencies:**` → parse list items
- Look for `**RACI:**` → parse table (next 5-15 lines)
- Look for `**Key Process Notes:**` or similar → capture bulleted list

#### 7.1.3 RACI Table Parsing

```
| Role | R | A | C | I |
|------|---|---|---|---|
| BD Associate | ✅ | | | |
| BD Manager | | ✅ | | |
```

Parse into:
```json
[
  {
    "role": "BD Associate",
    "responsible": true,
    "accountable": false,
    "consulted": false,
    "informed": false
  },
  {
    "role": "BD Manager",
    "responsible": false,
    "accountable": true,
    "consulted": false,
    "informed": false
  }
]
```

#### 7.1.4 Error Handling
- **Missing sections:** Log warning, continue with empty value
- **Malformed tables:** Skip table, include raw text
- **Unknown format:** Include as raw markdown in `content_raw`

---

## 8. GENERATOR IMPLEMENTATION

### 8.1 HTML Generator (`generator.py`)

#### 8.1.1 Core Functions

```python
def generate_html(data: dict, output_path: str):
    """
    Main generation function
    Creates complete HTML file from JSON data
    """
    pass

def generate_navigation_html(departments: list) -> str:
    """
    Generate sidebar navigation tree HTML
    """
    pass

def generate_workstream_html(dept: dict, area: dict, ws: dict) -> str:
    """
    Generate HTML for a single workstream card
    """
    pass

def generate_raci_table_html(raci: list) -> str:
    """
    Generate RACI table HTML
    """
    pass

def generate_search_index(data: dict) -> str:
    """
    Generate JavaScript search index for client-side search
    """
    pass

def inline_css() -> str:
    """
    Return CSS styles to inline in HTML
    """
    pass

def inline_javascript() -> str:
    """
    Return JavaScript code to inline in HTML
    """
    pass
```

#### 8.1.2 Template Structure

The generated HTML should have this structure:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConnectHear Operations Bible v2.0</title>
    <style>
        /* Inline all CSS here */
    </style>
</head>
<body>
    <header class="header">
        <!-- Title and search bar -->
    </header>
    
    <div class="container">
        <nav class="sidebar">
            <!-- Generated navigation tree -->
        </nav>
        
        <main class="content">
            <!-- Home/welcome section -->
            
            <!-- All workstream sections (hidden by default) -->
            <div class="workstream-section" id="dept-area-ws">
                <!-- Workstream content -->
            </div>
            <!-- Repeat for all workstreams -->
        </main>
    </div>
    
    <script>
        // Inline all JavaScript here
        const DATA = /* Embedded JSON data */;
        // Navigation functions
        // Search functions
        // URL routing functions
    </script>
</body>
</html>
```

---

## 9. JAVASCRIPT FUNCTIONALITY

### 9.1 Core Functions

```javascript
// Navigation
function toggleDepartment(deptId) { }
function toggleArea(areaId) { }
function showWorkstream(wsId) { }
function updateBreadcrumbs(dept, area, ws) { }

// Search
function initSearch() { }
function performSearch(query) { }
function highlightSearchResults(query) { }
function clearSearch() { }

// URL Routing
function initRouting() { }
function handleHashChange() { }
function navigateToHash(hash) { }

// Utilities
function scrollToTop() { }
function generateId(text) { }
function debounce(func, delay) { }
```

### 9.2 Data Embedding

Embed JSON data directly in JavaScript:
```javascript
const OPERATIONS_DATA = {
  "departments": [ /* full data here */ ]
};
```

This allows:
- No external file loading
- Instant search (data already in memory)
- Offline functionality

---

## 10. CSS STYLING

### 10.1 Design System

```css
:root {
  /* Colors */
  --primary: #2563eb;
  --secondary: #0ea5e9;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --bg-main: #ffffff;
  --bg-sidebar: #f8fafc;
  --border: #e2e8f0;
  --hover: #e0e7ff;
  
  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  
  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.5rem;
  --font-size-2xl: 2rem;
  
  /* Borders */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
}
```

### 10.2 Component Styling

Key components to style:
1. Header (fixed, with shadow)
2. Sidebar navigation (scrollable, collapsible items)
3. Workstream cards (bordered, with sections)
4. Tables (RACI tables with hover)
5. Tags (frequency, owner badges)
6. Breadcrumbs
7. Search input (with focus states)

---

## 11. BUILD PROCESS

### 11.1 Build Script (`build.sh`)

```bash
#!/bin/bash

echo "Building ConnectHear Operations Portal..."

# Step 1: Parse markdown
echo "Parsing markdown..."
python3 src/parser.py input/ConnectHear_Operations_Bible_v2.md output/data.json

# Step 2: Generate HTML
echo "Generating HTML..."
python3 src/generator.py output/data.json output/index.html

# Step 3: Validate
echo "Validating output..."
# Check file size, check HTML validity

echo "Build complete! Open output/index.html in your browser."
```

### 11.2 Development Workflow

```bash
# Initial build
./build.sh

# During development (with watch mode)
python3 src/watch.py  # Rebuilds on markdown changes

# Testing
python3 -m pytest tests/

# Production build
./build.sh --production  # Minify CSS/JS
```

---

## 12. TESTING REQUIREMENTS

### 12.1 Parser Tests

```python
def test_parse_department():
    """Test department extraction"""
    pass

def test_parse_area():
    """Test area extraction"""
    pass

def test_parse_workstream():
    """Test workstream extraction and content parsing"""
    pass

def test_parse_raci_table():
    """Test RACI table parsing"""
    pass

def test_markdown_to_html():
    """Test markdown conversion"""
    pass
```

### 12.2 Generator Tests

```python
def test_generate_navigation():
    """Test navigation HTML generation"""
    pass

def test_generate_workstream_card():
    """Test workstream card HTML"""
    pass

def test_complete_build():
    """Test end-to-end build process"""
    pass
```

### 12.3 Manual Testing Checklist

- [ ] All departments visible in navigation
- [ ] All areas expandable/collapsible
- [ ] All workstreams clickable and display correctly
- [ ] Search works across all fields
- [ ] RACI tables render correctly
- [ ] Breadcrumbs update properly
- [ ] Deep links work (hash URLs)
- [ ] Responsive design works on mobile
- [ ] Works offline
- [ ] No console errors
- [ ] All content from markdown is present

---

## 13. EDGE CASES & SPECIAL HANDLING

### 13.1 Content Variations

Some workstreams may have:
- No RACI table (just narrative)
- Multiple tables (not just RACI)
- Long process flows with arrows
- Nested lists
- Bold/italic mixed formatting

**Handling:** Include all content in `content_raw` field, attempt structured parsing but fall back to raw display.

### 13.2 Large Content

Some workstreams (especially Finance) have very long descriptions with:
- 10+ bullet points in Output
- Complex process flows
- Multiple note sections

**Handling:** Use expandable sections for long content (click to expand).

### 13.3 Special Characters

Handle:
- Emojis (🔷 📍 ✅)
- Arrows (→ ← ↓ ↑)
- Checkmarks
- Special markdown characters

**Handling:** Preserve UTF-8 encoding, don't escape emojis.

---

## 14. FUTURE ENHANCEMENTS (Out of Scope for V1)

### 14.1 Phase 2 Features
- **User authentication:** Show only relevant workstreams
- **Edit mode:** Update content directly in browser
- **Export:** Download as PDF or Word doc
- **Comments:** Team members can add notes
- **Version history:** Track changes over time

### 14.2 Advanced Features
- **Smart filters:** 
  - Show me everything I'm Responsible for
  - Show me all Monthly tasks
  - Show me Finance department only
- **Analytics:**
  - Track most viewed workstreams
  - Search analytics
- **Integrations:**
  - Link to ERPNext processes
  - Slack notifications for updates

---

## 15. DELIVERABLES

### 15.1 Core Deliverables
1. ✅ `parser.py` - Markdown parser (fully functional)
2. ✅ `generator.py` - HTML generator (fully functional)
3. ✅ `index.html` - Complete operations portal (single file)
4. ✅ `build.sh` - Build script
5. ✅ Tests for parser and generator

### 15.2 Documentation
1. ✅ README.md - How to use and update
2. ✅ SPEC.md - This technical specification
3. ✅ DEVELOPMENT.md - Developer guide

### 15.3 Quality Criteria
- **Completeness:** ALL content from markdown is present
- **Functionality:** All features in section 5 work
- **Performance:** Meets requirements in section 6.1
- **Design:** Professional, matches mockups
- **Code quality:** Clean, commented, maintainable

---

## 16. DEVELOPMENT PHASES

### Phase 1: Parser (Week 1, Day 1-2)
- [ ] Set up project structure
- [ ] Implement markdown parser
- [ ] Extract all departments, areas, workstreams
- [ ] Parse workstream content sections
- [ ] Parse RACI tables
- [ ] Output JSON file
- [ ] Write parser tests

### Phase 2: Generator (Week 1, Day 3-4)
- [ ] Create HTML template
- [ ] Implement CSS styling
- [ ] Generate navigation HTML
- [ ] Generate workstream cards
- [ ] Generate RACI tables
- [ ] Embed data in JavaScript
- [ ] Write generator tests

### Phase 3: JavaScript (Week 1, Day 5)
- [ ] Implement navigation functions
- [ ] Implement search functionality
- [ ] Implement URL routing
- [ ] Add smooth scrolling
- [ ] Add keyboard shortcuts
- [ ] Test all interactions

### Phase 4: Polish & Testing (Week 2, Day 1-2)
- [ ] Responsive design testing
- [ ] Browser compatibility testing
- [ ] Performance optimization
- [ ] Accessibility testing
- [ ] Final QA
- [ ] Documentation

### Phase 5: Deployment (Week 2, Day 3)
- [ ] Generate production build
- [ ] Create deployment guide
- [ ] User training materials
- [ ] Handoff to ConnectHear team

---

## 17. SUCCESS METRICS

### 17.1 Technical Metrics
- ✅ 100% of markdown content parsed and displayed
- ✅ < 2 second load time
- ✅ < 100ms search response
- ✅ 0 console errors
- ✅ Works in all target browsers

### 17.2 User Metrics
- ✅ User can find any workstream in < 10 seconds
- ✅ Navigation intuitive (no training needed)
- ✅ Content readable on mobile
- ✅ Team adopts portal over old document

---

## 18. REFERENCE FILES

### 18.1 Input File
**Location:** `/mnt/user-data/outputs/ConnectHear_Operations_Bible_v2.md`

**Current State:**
- ✅ Business Development - COMPLETE (all areas and workstreams)
- ✅ Finance & Compliance - COMPLETE (all areas and workstreams)
- 🚧 Other 6 departments - PLACEHOLDERS (to be added later)

**Structure Example:**
```markdown
# 1. 🔷 Business Development

## 📍 Area: Partnerships & Sales

### Workstream: Lead Sourcing & Tracking

**Description:** Full text...

**Frequency:** Weekly

**Output:**
- Item 1
- Item 2

**Dependencies:**
- Team (reason)

**RACI:**

| Role | R | A | C | I |
|------|---|---|---|---|
| Person | ✅ | | | |
```

### 18.2 Sample Output Structure

The parser should extract this into:
```json
{
  "id": "lead-sourcing-tracking",
  "name": "Lead Sourcing & Tracking",
  "description": "Full text...",
  "frequency": "Weekly",
  "output": ["Item 1", "Item 2"],
  "dependencies": [{"team": "Team", "reason": "reason"}],
  "raci": [{"role": "Person", "r": true, "a": false, "c": false, "i": false}]
}
```

---

## 19. CONTACT & SUPPORT

**Project Owner:** Talal, ConnectHear  
**Development Tool:** Claude Code  
**Timeline:** 2 weeks  
**Questions:** Review this spec with Claude Code, iterate as needed

---

## 20. APPENDIX

### 20.1 Color Palette
```
Primary Blue: #2563eb
Secondary Blue: #0ea5e9
Success Green: #10b981
Warning Yellow: #f59e0b
Error Red: #ef4444
Gray 50: #f8fafc
Gray 100: #f1f5f9
Gray 200: #e2e8f0
Gray 300: #cbd5e1
Gray 400: #94a3b8
Gray 500: #64748b
Gray 600: #475569
Gray 700: #334155
Gray 800: #1e293b
Gray 900: #0f172a
```

### 20.2 Typography Scale
```
Base size: 16px
Scale: 1.125 (Major Second)

xs: 0.75rem (12px)
sm: 0.875rem (14px)
base: 1rem (16px)
lg: 1.125rem (18px)
xl: 1.5rem (24px)
2xl: 2rem (32px)
3xl: 2.5rem (40px)
```

### 20.3 Spacing Scale
```
xs: 0.25rem (4px)
sm: 0.5rem (8px)
md: 1rem (16px)
lg: 1.5rem (24px)
xl: 2rem (32px)
2xl: 3rem (48px)
3xl: 4rem (64px)
```

---

## FINAL NOTES FOR CLAUDE CODE

**This specification is comprehensive and complete.** You have everything you need to build the Operations Portal:

1. **Start with the parser** - This is the foundation
2. **Test incrementally** - Parse one department first, validate output
3. **Then build the generator** - Once you have good JSON, HTML generation is straightforward
4. **Reference the existing files** - The markdown file has the exact structure to parse
5. **Ask questions** - If anything is unclear, ask before implementing

**The goal:** Create a single, self-contained HTML file that contains ALL the content from the markdown file in a beautiful, navigable, searchable interface.

**Good luck! 🚀**
