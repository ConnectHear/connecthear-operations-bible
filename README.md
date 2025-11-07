# ConnectHear Operations Portal

An interactive HTML web portal for ConnectHear's Operations Bible - transforming 200+ pages of operational documentation into a navigable, searchable, professional interface.

---

## 🎯 Project Overview

**Problem:** ConnectHear has a comprehensive Operations Bible (200+ pages) that documents every department's processes. It's difficult to navigate, search, and use.

**Solution:** Build an interactive HTML portal with:
- Collapsible sidebar navigation (Department → Area → Workstream)
- Real-time search functionality
- Professional design
- Mobile responsive
- Works offline (no backend needed)

---

## 📦 What's Included

### Documentation
- **`SPEC.md`** - Complete technical specification (READ THIS FIRST!)
- **`DEVELOPER_GUIDE.md`** - Implementation guide for Claude Code
- **`README_HTML_Portal.md`** - End-user documentation

### Source Files
- **`ConnectHear_Operations_Bible_v2.md`** - Source markdown (currently BD + Finance complete)
- **`operations_bible.html`** - Design reference (prototype)

### To Be Built
- **`src/parser.py`** - Markdown → JSON parser
- **`src/generator.py`** - JSON → HTML generator
- **`build.py`** - Build script
- **`output/index.html`** - Final product

---

## 🚀 Quick Start for Claude Code

```bash
# 1. Read the spec
cat SPEC.md

# 2. Read the developer guide
cat DEVELOPER_GUIDE.md

# 3. Create project structure
mkdir -p src/templates tests input output

# 4. Copy source file
cp ConnectHear_Operations_Bible_v2.md input/

# 5. Start building!
# Build the parser first (src/parser.py)
# Then the generator (src/generator.py)
# Then the build script (build.py)

# 6. Test your build
python build.py
open output/index.html
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│  ConnectHear_Operations_Bible.md   │  Source (Markdown)
└─────────────────────────────────────┘
                ↓
         [Parser.py]
                ↓
┌─────────────────────────────────────┐
│     Structured JSON Data            │  Intermediate
└─────────────────────────────────────┘
                ↓
        [Generator.py]
                ↓
┌─────────────────────────────────────┐
│    index.html (Self-contained)      │  Output
│    - Embedded CSS                   │
│    - Embedded JavaScript            │
│    - All content                    │
└─────────────────────────────────────┘
```

---

## 📋 Requirements

### Python
- Python 3.8+
- No external libraries needed (use standard library only)
- Optional: `pytest` for testing

### Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## 🎨 Features

### Navigation
- ✅ 3-level collapsible sidebar (Department → Area → Workstream)
- ✅ Breadcrumbs showing current location
- ✅ Smooth scrolling
- ✅ Active state highlighting

### Search
- ✅ Real-time filtering (< 100ms response)
- ✅ Search across all content (titles, descriptions, owners)
- ✅ Results highlighting
- ✅ Auto-expand matching items

### Content Display
- ✅ Professional workstream cards
- ✅ RACI table rendering
- ✅ Metadata badges (frequency, owner)
- ✅ Formatted lists and tables
- ✅ Responsive design

### Technical
- ✅ Single HTML file (no external dependencies)
- ✅ Works offline
- ✅ Deep linking (shareable URLs to specific sections)
- ✅ < 5MB file size
- ✅ Mobile responsive

---

## 📊 Current Status

### ✅ Complete
- Specification document (SPEC.md)
- Developer guide (DEVELOPER_GUIDE.md)
- Source markdown file (Business Development + Finance)
- Design prototype (operations_bible.html)

### 🚧 To Build
- Markdown parser
- HTML generator
- Build system
- Tests

---

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/

# Manual testing checklist
- [ ] Parse markdown successfully
- [ ] Generate HTML successfully
- [ ] All departments visible
- [ ] All workstreams clickable
- [ ] Search works
- [ ] RACI tables display correctly
- [ ] Mobile responsive
- [ ] No console errors
```

---

## 📈 Success Metrics

**Technical:**
- 100% of markdown content in HTML
- < 2 second load time
- < 100ms search response
- 0 console errors

**User:**
- Team can find any process in < 10 seconds
- No training needed to use
- Mobile-friendly
- Actually used (adoption > 80%)

---

## 🎯 Development Phases

**Phase 1: Parser** (2 days)
- Extract departments, areas, workstreams
- Parse content sections (description, frequency, output, etc.)
- Parse RACI tables
- Output JSON

**Phase 2: Generator** (2 days)
- Create HTML template
- Generate navigation
- Generate workstream cards
- Inline CSS/JS

**Phase 3: Polish** (1 day)
- Test all features
- Fix bugs
- Optimize performance
- Final QA

**Total:** ~1 week for full implementation

---

## 📝 Notes for Development

### Parser Focus
- Use regex for header detection
- Handle edge cases (missing sections, malformed tables)
- Preserve special characters (emojis, arrows)
- Test with real markdown file

### Generator Focus
- Create reusable HTML components
- Embed data as JSON in JavaScript
- Inline all CSS and JS
- Optimize for file size

### Quality Checks
- Validate all content is present
- Test navigation thoroughly
- Test search with real queries
- Test on mobile device
- Test in all browsers

---

## 🤝 Team

**Project Owner:** Talal, ConnectHear  
**Developer:** Claude Code  
**Timeline:** 1-2 weeks  

---

## 📞 Support

Questions? Check:
1. SPEC.md - Complete technical specification
2. DEVELOPER_GUIDE.md - Implementation guide
3. Source markdown file - See exact structure to parse

---

## 🎉 Goal

**Deliver:** One perfect `index.html` file that contains:
- ✅ All content from the markdown file
- ✅ Beautiful, professional interface
- ✅ Fully functional navigation and search
- ✅ Works offline, no dependencies
- ✅ Ready to share with the team

**Let's build something great! 🚀**
