# Project Structure Template

This is the recommended directory structure for the ConnectHear Operations Portal project.

```
operations-portal/
│
├── README.md                          # Project overview (already created)
├── SPEC.md                            # Technical specification (already created)
├── DEVELOPER_GUIDE.md                 # Implementation guide (already created)
├── requirements.txt                   # Python dependencies (already created)
├── .gitignore                         # Git ignore file
│
├── input/                             # Source files
│   └── ConnectHear_Operations_Bible_v2.md
│
├── output/                            # Generated files
│   ├── index.html                     # Final portal (TO BE GENERATED)
│   └── data.json                      # Optional: intermediate JSON
│
├── src/                               # Source code
│   ├── __init__.py
│   ├── parser.py                      # Markdown → JSON parser (TO BUILD)
│   ├── generator.py                   # JSON → HTML generator (TO BUILD)
│   ├── utils.py                       # Shared utilities (TO BUILD)
│   └── templates/                     # HTML/CSS/JS templates
│       ├── base.html                  # HTML structure (TO BUILD)
│       ├── styles.css                 # CSS styling (TO BUILD)
│       └── scripts.js                 # JavaScript code (TO BUILD)
│
├── tests/                             # Test files
│   ├── __init__.py
│   ├── test_parser.py                 # Parser tests (TO BUILD)
│   ├── test_generator.py              # Generator tests (TO BUILD)
│   └── fixtures/                      # Test data
│       └── sample.md                  # Sample markdown for testing
│
├── build.py                           # Main build script (TO BUILD)
└── watch.py                           # Optional: auto-rebuild on changes
```

---

## File Descriptions

### Already Created
- **README.md** - Project overview and quick start
- **SPEC.md** - Complete technical specification (45+ pages)
- **DEVELOPER_GUIDE.md** - Step-by-step implementation guide
- **requirements.txt** - Python dependencies (minimal)
- **README_HTML_Portal.md** - End-user documentation
- **operations_bible.html** - Design reference (prototype)

### To Build - Core Files

#### `src/parser.py`
Parses markdown into structured JSON.

Key functions:
- `parse_markdown(file_path: str) -> dict`
- `extract_departments(lines: list) -> list`
- `extract_areas(lines: list) -> list`
- `extract_workstreams(lines: list) -> list`
- `parse_workstream_content(lines: list) -> dict`
- `parse_raci_table(lines: list) -> list`

#### `src/generator.py`
Generates HTML from JSON data.

Key functions:
- `generate_html(data: dict, output_path: str)`
- `generate_navigation(departments: list) -> str`
- `generate_workstream_card(workstream: dict) -> str`
- `generate_raci_table(raci: list) -> str`
- `inline_css() -> str`
- `inline_javascript() -> str`

#### `src/utils.py`
Shared utility functions.

Suggested functions:
- `generate_id(text: str) -> str` - Convert text to HTML ID
- `markdown_to_html(md: str) -> str` - Convert markdown to HTML
- `escape_html(text: str) -> str` - Escape HTML special chars
- `read_file(path: str) -> str` - Read file contents
- `write_file(path: str, content: str)` - Write file contents

#### `build.py`
Main build script - orchestrates everything.

```python
#!/usr/bin/env python3
"""
Build script for ConnectHear Operations Portal
"""

from src.parser import parse_markdown
from src.generator import generate_html
from pathlib import Path

def main():
    print("=" * 60)
    print("Building ConnectHear Operations Portal")
    print("=" * 60)
    
    # Parse markdown
    print("\n1. Parsing markdown...")
    data = parse_markdown('input/ConnectHear_Operations_Bible_v2.md')
    print(f"   ✓ Found {len(data['departments'])} departments")
    
    # Generate HTML
    print("\n2. Generating HTML...")
    generate_html(data, 'output/index.html')
    print("   ✓ HTML generated")
    
    # Validate
    print("\n3. Validating output...")
    output_path = Path('output/index.html')
    if output_path.exists():
        size = output_path.stat().st_size / 1024 / 1024  # MB
        print(f"   ✓ Output file: {size:.2f} MB")
    
    print("\n" + "=" * 60)
    print("Build complete! Open output/index.html in your browser.")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

### To Build - Templates

#### `src/templates/base.html`
HTML structure template. Should include:
- Header with title and search bar
- Sidebar navigation (placeholder for generated nav)
- Main content area (placeholder for generated content)
- Placeholders for CSS and JavaScript injection

#### `src/templates/styles.css`
Complete CSS styling. See `operations_bible.html` for reference.

Sections to include:
- CSS variables (colors, spacing, fonts)
- Reset/base styles
- Header styles
- Sidebar styles
- Content styles
- Table styles (RACI tables)
- Responsive media queries

#### `src/templates/scripts.js`
JavaScript functionality.

Functions to include:
- Navigation (toggle departments/areas, show workstreams)
- Search (real-time filtering)
- URL routing (hash-based navigation)
- Utilities (scroll, debounce, etc.)

### To Build - Tests

#### `tests/test_parser.py`
Unit tests for parser functions.

Example tests:
- `test_extract_departments()` - Test department extraction
- `test_extract_areas()` - Test area extraction
- `test_extract_workstreams()` - Test workstream extraction
- `test_parse_raci_table()` - Test RACI table parsing
- `test_parse_full_workstream()` - Test complete workstream parsing
- `test_edge_cases()` - Test malformed content handling

#### `tests/test_generator.py`
Unit tests for generator functions.

Example tests:
- `test_generate_navigation()` - Test nav HTML generation
- `test_generate_workstream_card()` - Test workstream HTML
- `test_generate_raci_table()` - Test RACI table HTML
- `test_complete_html_generation()` - Test full HTML output
- `test_css_inline()` - Test CSS embedding
- `test_javascript_inline()` - Test JS embedding

---

## Getting Started

### Step 1: Create Directory Structure
```bash
mkdir -p operations-portal/{src/templates,tests/fixtures,input,output}
cd operations-portal
touch src/{__init__,parser,generator,utils}.py
touch src/templates/{base.html,styles.css,scripts.js}
touch tests/{__init__,test_parser,test_generator}.py
touch build.py watch.py
```

### Step 2: Copy Files
```bash
# Copy source markdown
cp /path/to/ConnectHear_Operations_Bible_v2.md input/

# Copy documentation
cp /path/to/{README,SPEC,DEVELOPER_GUIDE}.md .
cp /path/to/requirements.txt .
```

### Step 3: Start Building
```bash
# Install dependencies (optional)
pip install -r requirements.txt

# Start with the parser
# Implement src/parser.py following SPEC.md

# Then the generator
# Implement src/generator.py following SPEC.md

# Create build script
# Implement build.py

# Test it!
python build.py
open output/index.html
```

---

## Development Workflow

### 1. Parser Development
```bash
# Write parser code
vim src/parser.py

# Test parser
python -m pytest tests/test_parser.py -v

# Debug with sample
python -c "from src.parser import parse_markdown; import json; print(json.dumps(parse_markdown('input/sample.md'), indent=2))"
```

### 2. Generator Development
```bash
# Write generator code
vim src/generator.py

# Test generator
python -m pytest tests/test_generator.py -v

# Generate HTML from sample data
python -c "from src.generator import generate_html; generate_html(sample_data, 'output/test.html')"
```

### 3. Integration Testing
```bash
# Full build
python build.py

# Check output
open output/index.html

# Check for errors in browser console
# Verify all content is present
# Test search functionality
# Test navigation
```

---

## Best Practices

### Code Quality
- Use type hints for all functions
- Add docstrings to all functions
- Follow PEP 8 style guide
- Keep functions focused and small
- Handle errors gracefully

### Testing
- Write tests as you build (TDD approach)
- Test edge cases (missing sections, malformed content)
- Test with real markdown file
- Validate output HTML in browser

### Version Control
```bash
# Initialize git
git init

# Add .gitignore
echo "output/
__pycache__/
*.pyc
.pytest_cache/
.coverage
htmlcov/
.DS_Store
*.swp" > .gitignore

# Commit your work frequently
git add .
git commit -m "Initial implementation of parser"
```

---

## Validation Checklist

Before considering the project complete:

### Parser
- [ ] Extracts all departments
- [ ] Extracts all areas
- [ ] Extracts all workstreams
- [ ] Parses descriptions correctly
- [ ] Parses frequencies correctly
- [ ] Parses output lists correctly
- [ ] Parses dependencies correctly
- [ ] Parses RACI tables correctly
- [ ] Parses notes/requirements sections
- [ ] Handles edge cases gracefully
- [ ] Outputs valid JSON

### Generator
- [ ] Creates valid HTML5
- [ ] Embeds CSS inline
- [ ] Embeds JavaScript inline
- [ ] Generates complete navigation tree
- [ ] Generates all workstream cards
- [ ] Renders RACI tables correctly
- [ ] Implements search functionality
- [ ] Implements URL routing
- [ ] Responsive design works
- [ ] No console errors

### Build System
- [ ] build.py runs without errors
- [ ] Output file is created
- [ ] File size is reasonable (< 5MB)
- [ ] Can run multiple times (idempotent)

### End-to-End
- [ ] All content from markdown appears in HTML
- [ ] Navigation works (expand/collapse/click)
- [ ] Search works (try "Umaima", "Monthly", etc.)
- [ ] Deep links work (URLs with #hashes)
- [ ] Breadcrumbs update correctly
- [ ] Works on mobile
- [ ] Works in all browsers
- [ ] No missing or broken content

---

## Success! 🎉

When you've completed this checklist and validated everything works, you'll have a professional, production-ready Operations Portal that makes ConnectHear's 200-page operations document actually usable!

**Deliverable:** One perfect `index.html` file that the team can use immediately.

Good luck! 🚀
