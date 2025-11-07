# ConnectHear Operations Bible - HTML Portal

## 📚 What You Have

You now have an **interactive HTML Operations Portal** that makes your massive operations document easy to navigate and use!

### Files Created:

1. **`operations_bible.html`** - Your interactive portal (READY TO USE!)
2. **`ConnectHear_Operations_Bible_v2.md`** - Master markdown source
3. **`convert_md_to_html.py`** - Conversion script (for future updates)

---

## 🚀 How to Use

### Option 1: Open Locally (Easiest)
1. Download `operations_bible.html` to your computer
2. Double-click to open in your web browser
3. That's it! No server needed, works offline

### Option 2: Host on Your Intranet
1. Upload `operations_bible.html` to your internal server
2. Share the link with your team (e.g., `http://intranet.connecthear.com/operations`)
3. Everyone can access from anywhere

### Option 3: Host on GitHub Pages (Free, Public)
1. Create a GitHub repository
2. Upload `operations_bible.html` and rename to `index.html`
3. Enable GitHub Pages in repository settings
4. Access at `https://yourusername.github.io/reponame`

---

## ✨ Features

### 🔍 Search
- Type in the search bar at the top
- Instantly filters workstreams, owners, departments
- Results highlight as you type

### 📂 Navigation
- Click any department (🔷) to expand
- Click any area (📍) to see workstreams
- Click any workstream to view details
- Collapsible sidebar keeps everything organized

### 🔗 Direct Links
- Each workstream has a unique URL
- Share specific sections: `operations_bible.html#bd-lead-sourcing`
- Bookmarkable for quick access

### 📱 Responsive
- Works on desktop, tablet, and mobile
- Sidebar collapses on small screens
- Clean, professional design

---

## 🔄 How to Update Content

### When You Finish Other Departments

**Step 1: Edit the Markdown**
- Open `ConnectHear_Operations_Bible_v2.md`
- Add new departments following the same format:
  ```markdown
  # 3. 🔷 Content & Design
  
  ## 📍 Area: Brand & Visual Identity
  
  ### Workstream: Brand Governance
  
  **Description:** ...
  **Frequency:** ...
  **Output:** ...
  ```

**Step 2: Update the HTML (Manual - Quick)**
- Open `operations_bible.html` in a text editor
- Find the navigation section (around line 500)
- Add new department entries following the pattern
- Add workstream content sections at the bottom
- Save and refresh in browser

**Step 3: Use Conversion Script (Automated - Later)**
- Once you're comfortable with Python:
  ```bash
  python3 convert_md_to_html.py
  ```
- This will auto-generate the full HTML (script needs finishing)

---

## 💡 Customization Ideas

### Change Colors
Edit the CSS variables at the top of the HTML (around line 18):
```css
:root {
    --primary-color: #2563eb;  /* Change to your brand color */
    --sidebar-bg: #f8fafc;
    --accent-color: #0ea5e9;
}
```

### Add Your Logo
Replace line 219 with:
```html
<h1>
    <img src="logo.png" style="height: 40px;">
    ConnectHear Operations Bible
</h1>
```

### Add Filters
You can add buttons to filter by:
- Owner (Show me everything Umaima is responsible for)
- Frequency (Show me all monthly tasks)
- Department (Show me only Finance)

---

## 🎯 Tips for Team Adoption

### For Leadership
- Bookmark specific sections you review frequently
- Share direct links in Slack/email: "Check process here: [link]"
- Use search to quickly find who owns what

### For Department Heads
- Expand your department by default
- Print your section as PDF (browser print function)
- Update your areas as processes evolve

### For Staff
- Search your name to see your responsibilities
- Use RACI tables to know who to ask for what
- Mobile-friendly for checking on the go

---

## 📊 Current Status

### ✅ Complete Departments
- **Business Development** - All 6 areas, 25+ workstreams
- **Finance & Compliance** - All 6 areas, 25+ workstreams

### 🚧 To Be Added (You'll add after sessions with Arhum)
- Content & Design
- Product & Projects  
- Sign Language – Training & Interpretation
- Marketing
- AdminOps
- Leadership / PMO

---

## 🐛 Troubleshooting

### Search not working?
- Make sure JavaScript is enabled in browser
- Try refreshing the page

### Sections not expanding?
- Check that you're clicking the department name
- Try opening in a different browser

### Want to print?
- Use browser's print function (Ctrl+P / Cmd+P)
- The CSS is print-friendly

### Need help?
- The HTML is self-contained (no external dependencies)
- Works in any modern browser (Chrome, Firefox, Safari, Edge)
- Can be edited in any text editor

---

## 🎉 What Makes This Better Than a Document?

| Feature | PDF/Word | HTML Portal |
|---------|----------|-------------|
| **Search** | Basic | Live filtering |
| **Navigation** | Table of contents | Collapsible tree |
| **Updates** | Re-send entire file | Just refresh browser |
| **Sharing** | Email attachment | Send one link |
| **Mobile** | Awkward scrolling | Responsive design |
| **Size** | 200+ pages | Loads sections on demand |
| **Links** | Hard to share specific section | Direct URL to any workstream |

---

## 📝 Next Steps

1. ✅ **You have:** Working HTML portal with BD and Finance
2. 🔜 **Next:** Add remaining departments as you complete them with Arhum
3. 🚀 **Future:** Consider adding user login to show personalized view

---

## 💬 Questions?

This is a **living document** and **living portal**. As processes evolve:
- Update the markdown (source of truth)
- Refresh the HTML (presentation layer)
- Share the link (no need to re-send files)

**Pro tip:** Host on your company's Google Drive or Sharepoint and share the link. Everyone always has the latest version!

---

**Created with ❤️ for ConnectHear**
*Making operations documentation actually usable*
