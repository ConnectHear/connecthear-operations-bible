#!/usr/bin/env python3
"""
ConnectHear Operations Portal - HTML Generator

Generates a complete, self-contained HTML file from parsed JSON data.
Includes navigation tree, workstream cards, RACI tables, and embedded CSS/JS.
"""

import json
import html
from pathlib import Path
from typing import Dict, List


def escape_html(text: str) -> str:
    """Escape HTML special characters."""
    return html.escape(text) if text else ''


def convert_markdown_bold(text: str) -> str:
    """Convert markdown bold (**text**) to HTML strong tags."""
    if not text:
        return ''
    # Escape HTML first
    text = html.escape(text)
    # Then convert **text** to <strong>text</strong>
    import re
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text


def load_template_file(filename: str) -> str:
    """Load a template file from src/templates/"""
    template_path = Path(__file__).parent / 'templates' / filename
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_navigation_html(departments: List[Dict]) -> str:
    """
    Generate the sidebar navigation tree HTML.

    Args:
        departments: List of department dictionaries

    Returns:
        Navigation HTML string
    """
    nav_html = '<ul class="nav-tree">\n'

    for dept in departments:
        dept_id = dept['id']
        dept_name = escape_html(dept['name'])
        dept_emoji = dept.get('emoji', '🔷')

        nav_html += f'''
  <li class="nav-department" data-dept-id="{dept_id}">
    <div class="nav-department-header">
      <span class="toggle-icon">▶</span>
      {dept_emoji} <strong>{dept_name}</strong>
    </div>
    <ul class="nav-areas">
'''

        # Generate areas
        for area in dept.get('areas', []):
            area_id = area['id']
            area_name = escape_html(area['name'])
            area_emoji = area.get('emoji', '📍')

            nav_html += f'''
      <li class="nav-area" data-area-id="{area_id}">
        <div class="nav-area-header">
          <span class="toggle-icon">▶</span>
          {area_emoji} {area_name}
        </div>
        <ul class="nav-workstreams">
'''

            # Generate workstreams
            for ws in area.get('workstreams', []):
                ws_id = ws['id']
                ws_name = escape_html(ws['name'])
                full_id = f"{dept_id}-{area_id}-{ws_id}"

                nav_html += f'''
          <li class="nav-workstream">
            <a href="#{full_id}"
               class="nav-workstream-link"
               data-workstream-id="{full_id}">
              {ws_name}
            </a>
          </li>
'''

            nav_html += '''
        </ul>
      </li>
'''

        nav_html += '''
    </ul>
  </li>
'''

    nav_html += '</ul>\n'
    return nav_html


def generate_raci_table_html(raci: List[Dict]) -> str:
    """
    Generate RACI table HTML.

    Args:
        raci: List of RACI role dictionaries

    Returns:
        HTML table string
    """
    if not raci:
        return '<p class="text-muted">No RACI information available.</p>'

    html_content = '''
<div class="raci-table-container">
  <table class="raci-table">
    <thead>
      <tr>
        <th>Role</th>
        <th>R</th>
        <th>A</th>
        <th>C</th>
        <th>I</th>
      </tr>
    </thead>
    <tbody>
'''

    for role_entry in raci:
        role_name = escape_html(role_entry.get('role', ''))
        r_check = '✅' if role_entry.get('responsible', False) else ''
        a_check = '✅' if role_entry.get('accountable', False) else ''
        c_check = '✅' if role_entry.get('consulted', False) else ''
        i_check = '✅' if role_entry.get('informed', False) else ''

        html_content += f'''
      <tr>
        <td>{role_name}</td>
        <td><span class="raci-check">{r_check}</span></td>
        <td><span class="raci-check">{a_check}</span></td>
        <td><span class="raci-check">{c_check}</span></td>
        <td><span class="raci-check">{i_check}</span></td>
      </tr>
'''

    html_content += '''
    </tbody>
  </table>
</div>
'''

    return html_content


def generate_workstream_html(dept: Dict, area: Dict, ws: Dict) -> str:
    """
    Generate HTML for a single workstream card.

    Args:
        dept: Department dictionary
        area: Area dictionary
        ws: Workstream dictionary

    Returns:
        HTML string for the workstream section
    """
    ws_id = f"ws-{dept['id']}-{area['id']}-{ws['id']}"
    ws_name = escape_html(ws.get('name', 'Untitled Workstream'))

    # Build TOC based on available sections
    toc_items = []
    if ws.get('description'):
        toc_items.append(('description', 'Description', '📝'))
    if ws.get('output'):
        toc_items.append(('output', 'Output', '📊'))
    if ws.get('dependencies'):
        toc_items.append(('dependencies', 'Dependencies', '🔗'))
    if ws.get('raci'):
        toc_items.append(('raci', 'RACI Matrix', '👥'))
    if ws.get('notes'):
        toc_items.append(('notes', 'Notes', '💡'))

    html_content = f'''
<section class="workstream-section" id="{ws_id}">
  <div class="workstream-header">
    <h1 class="workstream-title">{ws_name}</h1>
    <div class="workstream-meta">
'''

    # Add frequency tag
    if ws.get('frequency'):
        frequency = escape_html(ws['frequency'])
        html_content += f'''
      <div class="meta-tag">
        <strong>Frequency:</strong> {frequency}
      </div>
'''

    # Add owner tag (extract from RACI)
    if ws.get('raci'):
        owners = [r['role'] for r in ws['raci'] if r.get('responsible') or r.get('accountable')]
        if owners:
            owners_text = escape_html(', '.join(owners[:2]))  # Show first 2 owners
            html_content += f'''
      <div class="meta-tag">
        <strong>Owner:</strong> {owners_text}
      </div>
'''

    html_content += '''
    </div>
  </div>
'''

    # Add mini-TOC if we have sections
    if toc_items:
        html_content += '''
  <nav class="workstream-toc">
    <div class="toc-header">Quick Jump:</div>
    <ul class="toc-list">
'''
        for section_id, section_name, icon in toc_items:
            html_content += f'''
      <li class="toc-item">
        <a href="#" class="toc-link" data-section-id="{ws_id}-{section_id}" onclick="scrollToSection('{ws_id}-{section_id}'); return false;">
          <span class="toc-icon">{icon}</span>
          <span class="toc-text">{section_name}</span>
        </a>
      </li>
'''
        html_content += '''
    </ul>
  </nav>
'''

    # Description section
    if ws.get('description'):
        description = convert_markdown_bold(ws['description'])
        html_content += f'''
  <div class="content-section" id="{ws_id}-description">
    <h2 class="section-title">Description</h2>
    <div class="section-content">
      <p>{description}</p>
    </div>
  </div>
'''

    # Output section
    if ws.get('output'):
        html_content += f'''
  <div class="content-section" id="{ws_id}-output">
    <h2 class="section-title">Output</h2>
    <div class="section-content">
      <ul>
'''
        for output_item in ws['output']:
            output_text = convert_markdown_bold(output_item)
            html_content += f'        <li>{output_text}</li>\n'

        html_content += '''
      </ul>
    </div>
  </div>
'''

    # Dependencies section
    if ws.get('dependencies'):
        html_content += f'''
  <div class="content-section" id="{ws_id}-dependencies">
    <h2 class="section-title">Dependencies</h2>
    <div class="section-content">
      <ul class="dependency-list">
'''
        for dep in ws['dependencies']:
            team = convert_markdown_bold(dep.get('team', ''))
            reason = convert_markdown_bold(dep.get('reason', ''))
            html_content += f'''
        <li class="dependency-item">
          <span class="dependency-team">{team}</span>
'''
            if reason:
                html_content += f'          <span class="dependency-reason"> — {reason}</span>\n'

            html_content += '        </li>\n'

        html_content += '''
      </ul>
    </div>
  </div>
'''

    # RACI section
    if ws.get('raci'):
        html_content += f'''
  <div class="content-section" id="{ws_id}-raci">
    <h2 class="section-title">RACI Matrix</h2>
    <div class="section-content">
'''
        html_content += generate_raci_table_html(ws['raci'])
        html_content += '''
    </div>
  </div>
'''

    # Notes section
    if ws.get('notes'):
        # Wrap all notes in a container with the ID (only one ID for all notes)
        html_content += f'  <div id="{ws_id}-notes">\n'
        for note in ws['notes']:
            note_title = convert_markdown_bold(note.get('title', 'Notes'))
            html_content += f'''
  <div class="notes-section">
    <div class="notes-title">{note_title}</div>
    <div class="notes-content">
'''
            if isinstance(note.get('content'), list):
                html_content += '      <ul>\n'
                for item in note['content']:
                    item_text = convert_markdown_bold(item)
                    html_content += f'        <li>{item_text}</li>\n'
                html_content += '      </ul>\n'
            else:
                content_text = convert_markdown_bold(str(note.get('content', '')))
                html_content += f'      <p>{content_text}</p>\n'

            html_content += '''
    </div>
  </div>
'''
        html_content += '  </div>\n'

    html_content += '</section>\n'
    return html_content


def generate_home_section(metadata: Dict) -> str:
    """
    Generate the home/welcome section HTML.

    Args:
        metadata: Metadata dictionary

    Returns:
        HTML string for home section
    """
    total_depts = metadata.get('total_departments', 0)
    total_areas = metadata.get('total_areas', 0)
    total_ws = metadata.get('total_workstreams', 0)
    version = escape_html(metadata.get('version', '2.0'))
    last_updated = escape_html(metadata.get('last_updated', 'November 2025'))

    html_content = f'''
<div id="home-section" class="home-section">
  <h1>ConnectHear Operations Bible v{version}</h1>
  <p class="text-muted">Complete operational reference guide for all departments, areas, workstreams, and processes</p>

  <h2>How to Use This Portal</h2>
  <ul>
    <li>Use the <strong>sidebar navigation</strong> to browse departments, areas, and workstreams</li>
    <li>Use the <strong>search bar</strong> to find specific workstreams, people, or processes</li>
    <li>Click on any workstream to view its complete details including RACI, dependencies, and outputs</li>
    <li>Use breadcrumbs to navigate back to parent sections</li>
  </ul>

  <h2>RACI Key</h2>
  <ul>
    <li><strong>R</strong> = Responsible (does the work)</li>
    <li><strong>A</strong> = Accountable (final authority)</li>
    <li><strong>C</strong> = Consulted (provides input)</li>
    <li><strong>I</strong> = Informed (kept in the loop)</li>
  </ul>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">{total_depts}</div>
      <div class="stat-label">Departments</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{total_areas}</div>
      <div class="stat-label">Areas</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{total_ws}</div>
      <div class="stat-label">Workstreams</div>
    </div>
  </div>

  <p class="text-muted" style="margin-top: 2rem;">Last updated: {last_updated}</p>
</div>
'''

    return html_content


def generate_html(data: Dict, output_path: str):
    """
    Main generation function - creates complete HTML file.

    Args:
        data: Parsed data dictionary from parser
        output_path: Path to save the HTML file
    """
    print("Generating HTML...")

    # Load CSS and JavaScript
    css_content = load_template_file('styles.css')
    js_content = load_template_file('scripts.js')

    # Generate navigation
    print("  - Generating navigation tree...")
    navigation_html = generate_navigation_html(data['departments'])

    # Generate home section
    print("  - Generating home section...")
    home_html = generate_home_section(data['metadata'])

    # Generate all workstream sections
    print("  - Generating workstream sections...")
    workstreams_html = ''
    for dept in data['departments']:
        for area in dept['areas']:
            for ws in area['workstreams']:
                workstreams_html += generate_workstream_html(dept, area, ws)

    # Convert data to JSON for embedding
    data_json = json.dumps(data, ensure_ascii=False)

    # Build complete HTML
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConnectHear Operations Bible v{data['metadata'].get('version', '2.0')}</title>
    <style>
{css_content}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-title">
            <span class="emoji">📘</span>
            <span>
                ConnectHear Operations Bible
                <span class="header-version">v{data['metadata'].get('version', '2.0')}</span>
            </span>
        </div>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle menu">☰</button>
        <div class="search-container">
            <input
                type="text"
                id="search-input"
                class="search-input"
                placeholder="Search workstreams, owners, departments..."
                autocomplete="off"
            />
            <button id="search-clear" class="search-clear" aria-label="Clear search">×</button>
        </div>
    </header>

    <!-- Main Container -->
    <div class="container">
        <!-- Sidebar Navigation -->
        <nav class="sidebar">
{navigation_html}
        </nav>

        <!-- Main Content -->
        <main class="content">
            <!-- Breadcrumbs -->
            <div id="breadcrumbs" class="breadcrumbs">
                <div class="breadcrumb-item">Home</div>
            </div>

            <!-- Home Section -->
{home_html}

            <!-- Workstream Sections -->
{workstreams_html}
        </main>
    </div>

    <!-- JavaScript -->
    <script>
        // Embed data
        const OPERATIONS_DATA = {data_json};

        // Include all JavaScript
{js_content}
    </script>
</body>
</html>
'''

    # Write to file
    print(f"  - Writing to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

    # Calculate file size
    file_size = Path(output_path).stat().st_size / 1024 / 1024  # MB
    print(f"  - File size: {file_size:.2f} MB")


if __name__ == '__main__':
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'output/data.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output/index.html'

    print(f"Loading data from {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    generate_html(data, output_file)
    print("✅ HTML generation complete!")
