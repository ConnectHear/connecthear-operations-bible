#!/usr/bin/env python3
"""
ConnectHear Operations Portal - Markdown Parser

Parses the Operations Bible markdown file into structured JSON.
Extracts hierarchy: Departments → Areas → Workstreams
Parses content sections: Description, Frequency, Output, Dependencies, RACI tables
"""

import re
import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime


def generate_id(text: str) -> str:
    """
    Convert text to a URL-friendly ID.

    Args:
        text: Original text (e.g., "Lead Sourcing & Tracking")

    Returns:
        URL-friendly ID (e.g., "lead-sourcing-tracking")
    """
    # Remove emojis and special characters
    text = re.sub(r'[🔷📍✅]', '', text)
    # Convert to lowercase and replace spaces/special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def parse_raci_table(lines: List[str]) -> List[Dict]:
    """
    Parse RACI markdown table into structured data.

    Expected format:
    | Role | R | A | C | I |
    |------|---|---|---|---|
    | Person Name | ✅ | | | |

    Args:
        lines: Lines containing the RACI table

    Returns:
        List of RACI role dictionaries
    """
    raci_data = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith('|---') or line.startswith('| Role'):
            continue

        # Split by pipe and clean
        parts = [p.strip() for p in line.split('|')]
        # Remove only the first and last empty elements (from | at start/end)
        if parts and parts[0] == '':
            parts = parts[1:]
        if parts and parts[-1] == '':
            parts = parts[:-1]

        if len(parts) >= 2:  # At least role + one column
            role = parts[0]
            raci_entry = {
                'role': role,
                'responsible': '✅' in parts[1] if len(parts) > 1 else False,
                'accountable': '✅' in parts[2] if len(parts) > 2 else False,
                'consulted': '✅' in parts[3] if len(parts) > 3 else False,
                'informed': '✅' in parts[4] if len(parts) > 4 else False
            }
            raci_data.append(raci_entry)

    return raci_data


def extract_list_items(lines: List[str]) -> List[str]:
    """
    Extract bullet point items from a list.

    Args:
        lines: Lines containing bullet points

    Returns:
        List of cleaned items
    """
    items = []
    for line in lines:
        line = line.strip()
        # Match lines starting with - or *
        if line.startswith('-') or line.startswith('*'):
            # Remove the bullet and clean
            item = re.sub(r'^[-*]\s*', '', line)
            items.append(item)
    return items


def parse_dependencies(lines: List[str]) -> List[Dict[str, str]]:
    """
    Parse dependencies from bulleted list.

    Format: "- Team Name (for reason)"

    Args:
        lines: Lines containing dependencies

    Returns:
        List of dependency dictionaries with 'team' and 'reason'
    """
    dependencies = []
    for line in lines:
        line = line.strip()
        if line.startswith('-') or line.startswith('*'):
            # Remove bullet
            item = re.sub(r'^[-*]\s*', '', line)

            # Try to extract team and reason
            match = re.match(r'(.+?)\s*\((.+?)\)', item)
            if match:
                dependencies.append({
                    'team': match.group(1).strip(),
                    'reason': match.group(2).strip()
                })
            else:
                # No parentheses, just the team name
                dependencies.append({
                    'team': item.strip(),
                    'reason': ''
                })

    return dependencies


def parse_process_steps(lines: List[str], start_idx: int) -> Tuple[Dict, int]:
    """
    Parse the **Process Steps:** section.

    Args:
        lines: All lines for this workstream
        start_idx: Index where Process Steps section starts

    Returns:
        Tuple of (process_steps dict, next_index)
    """
    process_steps = {
        'steps': [],
        'decision_points': [],
        'common_issues': [],
        'tools': [],
        'related_workstreams': []
    }

    i = start_idx + 1  # Skip the "**Process Steps:**" line
    current_step = None
    current_section = 'steps'  # Track which subsection we're in

    while i < len(lines):
        line = lines[i].strip()

        # Stop if we hit next workstream, area, or department
        # But NOT #### (which is a Process Steps subsection)
        if line.startswith('# ') and not line.startswith('#### '):
            break
        if line.startswith('## ') and not line.startswith('#### '):
            break
        if line.startswith('### ') and not line.startswith('#### '):
            break

        # Stop if we hit another major workstream section (like **Description:**, **RACI:**)
        # But NOT Process Steps subsections like **Issue:**, **Solution:**, **If X:**
        if (line.startswith('**') and ':' in line and
            not line.startswith('**If') and
            not line.startswith('**Issue:') and
            not line.startswith('**Solution:')):
            # This is a new section like **RACI:**, **Dependencies:**, stop parsing process steps
            break

        # Check for Process Steps subsections (#### headers)
        if line.startswith('####'):
            # Extract the subsection title
            subsection_title = line.replace('####', '').strip()

            if 'Decision Points' in subsection_title:
                current_section = 'decision_points'
                i += 1
                continue
            elif 'Common Issues' in subsection_title:
                current_section = 'common_issues'
                i += 1
                continue
            elif 'Tools' in subsection_title or 'Access' in subsection_title:
                current_section = 'tools'
                i += 1
                continue
            elif 'Key Thresholds' in subsection_title:
                current_section = 'tools'  # Treat thresholds as tools
                i += 1
                continue
            elif 'Related Workstreams' in subsection_title:
                current_section = 'related_workstreams'
                i += 1
                continue

            # Check if it's a numbered step (#### 1., #### 2., etc.)
            step_match = re.match(r'^(\d+)\.\s*(.+)$', subsection_title)
            if step_match and current_section == 'steps':
                # Save previous step if exists
                if current_step:
                    process_steps['steps'].append(current_step)

                # Start new step
                step_num = int(step_match.group(1))
                step_title = step_match.group(2).strip()
                current_step = {
                    'number': step_num,
                    'title': step_title,
                    'details': []
                }
                i += 1
                continue

        # Parse step details (bullet points) - only for steps section
        if current_section == 'steps' and current_step and (line.startswith('-') or line.startswith('*')):
            detail = re.sub(r'^[-*]\s*', '', line)
            current_step['details'].append(detail)
            i += 1
            continue

        # Parse Decision Points
        if current_section == 'decision_points':
            # Format: **If X:** Action OR **Condition:** Action
            decision_match = re.match(r'\*\*(.+?):\*\*\s*(.+)$', line)
            if decision_match:
                condition = decision_match.group(1).strip()
                action = decision_match.group(2).strip()
                process_steps['decision_points'].append({
                    'condition': condition,
                    'action': action
                })
            elif line.startswith('-') or line.startswith('*'):
                # Alternative format: - If X: Action
                detail = re.sub(r'^[-*]\s*', '', line)
                if ':' in detail:
                    parts = detail.split(':', 1)
                    process_steps['decision_points'].append({
                        'condition': parts[0].strip(),
                        'action': parts[1].strip()
                    })
            i += 1
            continue

        # Parse Common Issues
        if current_section == 'common_issues':
            # Format: **Issue:** Description **Solution:** Fix
            if line.startswith('**Issue:**'):
                issue_text = line.replace('**Issue:**', '').strip()
                solution_text = ''

                # Look ahead for solution on next line
                if i + 1 < len(lines) and '**Solution:**' in lines[i + 1]:
                    solution_text = lines[i + 1].replace('**Solution:**', '').strip()
                    i += 1

                process_steps['common_issues'].append({
                    'issue': issue_text,
                    'solution': solution_text
                })
            i += 1
            continue

        # Parse Tools & Access (bullet list)
        if current_section == 'tools' and (line.startswith('-') or line.startswith('*')):
            tool = re.sub(r'^[-*]\s*', '', line)
            process_steps['tools'].append(tool)
            i += 1
            continue

        # Parse Related Workstreams (bullet list)
        if current_section == 'related_workstreams' and (line.startswith('-') or line.startswith('*')):
            ws = re.sub(r'^[-*]\s*', '', line)
            process_steps['related_workstreams'].append(ws)
            i += 1
            continue

        # Skip empty lines
        if not line:
            i += 1
            continue

        i += 1

    # Save last step
    if current_step:
        process_steps['steps'].append(current_step)

    return process_steps, i


def parse_workstream_content(lines: List[str]) -> Dict:
    """
    Parse all content sections of a workstream.

    Sections: Description, Frequency, Output, Dependencies, RACI, Notes, Process Steps (v2.0)

    Args:
        lines: All lines for this workstream

    Returns:
        Dictionary with parsed content
    """
    content = {
        'description': '',
        'frequency': '',
        'output': [],
        'dependencies': [],
        'raci': [],
        'notes': [],
        'process_steps': None,  # v2.0: Process steps section
        'content_raw': '\n'.join(lines)
    }

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Extract Description
        if line.startswith('**Description:**'):
            desc_lines = []
            # Get text on same line
            desc_text = line.replace('**Description:**', '').strip()
            if desc_text:
                desc_lines.append(desc_text)

            # Continue until next ** section
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('**'):
                    break
                if next_line:
                    desc_lines.append(next_line)
                i += 1

            content['description'] = ' '.join(desc_lines)
            continue

        # Extract Frequency
        elif line.startswith('**Frequency:**'):
            content['frequency'] = line.replace('**Frequency:**', '').strip()

        # Extract Output
        elif line.startswith('**Output:**'):
            output_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('**'):
                    break
                if next_line and (next_line.startswith('-') or next_line.startswith('*')):
                    output_lines.append(next_line)
                elif next_line:
                    # Handle continuation of previous item
                    if output_lines:
                        output_lines[-1] += ' ' + next_line
                i += 1

            content['output'] = extract_list_items(output_lines)
            continue

        # Extract Dependencies
        elif line.startswith('**Dependencies:**'):
            dep_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('**'):
                    break
                if next_line and (next_line.startswith('-') or next_line.startswith('*')):
                    dep_lines.append(next_line)
                i += 1

            content['dependencies'] = parse_dependencies(dep_lines)
            continue

        # Extract RACI table
        elif line.startswith('**RACI:**'):
            raci_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('**') and not next_line.startswith('|'):
                    break
                if next_line.startswith('|'):
                    raci_lines.append(next_line)
                elif not next_line:
                    # Skip empty lines in table
                    pass
                elif next_line.startswith('**'):
                    break
                i += 1

            content['raci'] = parse_raci_table(raci_lines)
            continue

        # Extract Process Steps (v2.0)
        elif line.startswith('**Process Steps:**'):
            process_steps_data, next_i = parse_process_steps(lines, i)
            content['process_steps'] = process_steps_data
            i = next_i
            continue

        # Extract notes sections (Key Process Notes, Critical Implementation Requirements, etc.)
        elif re.match(r'\*\*(.+?Notes|.+?Requirements|Implementation Note):\*\*', line):
            note_title_match = re.match(r'\*\*(.+?):\*\*', line)
            note_title = note_title_match.group(1) if note_title_match else 'Notes'

            note_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('**') or next_line.startswith('###') or next_line.startswith('---'):
                    break
                if next_line:
                    note_lines.append(next_line)
                i += 1

            content['notes'].append({
                'title': note_title,
                'content': extract_list_items(note_lines) if any(l.startswith('-') or l.startswith('*') for l in note_lines) else ['\n'.join(note_lines)]
            })
            continue

        i += 1

    return content


def extract_workstreams(lines: List[str], area_id: str) -> List[Dict]:
    """
    Extract all workstreams within an area.

    Args:
        lines: Lines for this area
        area_id: Parent area ID

    Returns:
        List of workstream dictionaries
    """
    workstreams = []

    # Find all workstream headers
    workstream_indices = []
    for i, line in enumerate(lines):
        if line.strip().startswith('### Workstream:'):
            workstream_indices.append(i)

    # Parse each workstream
    for idx, start_idx in enumerate(workstream_indices):
        # Determine end index (next workstream or end of area)
        end_idx = workstream_indices[idx + 1] if idx + 1 < len(workstream_indices) else len(lines)

        # Extract workstream name
        header_line = lines[start_idx].strip()
        ws_name = header_line.replace('### Workstream:', '').strip()

        # Get all lines for this workstream
        ws_lines = lines[start_idx + 1:end_idx]

        # Parse content
        ws_content = parse_workstream_content(ws_lines)

        # Build workstream object
        workstream = {
            'id': generate_id(ws_name),
            'name': ws_name,
            **ws_content
        }

        workstreams.append(workstream)

    return workstreams


def extract_areas(lines: List[str], dept_id: str) -> List[Dict]:
    """
    Extract all areas within a department.

    Args:
        lines: Lines for this department
        dept_id: Parent department ID

    Returns:
        List of area dictionaries
    """
    areas = []

    # Find all area headers
    area_indices = []
    for i, line in enumerate(lines):
        if line.strip().startswith('## 📍 Area:'):
            area_indices.append(i)

    # Parse each area
    for idx, start_idx in enumerate(area_indices):
        # Determine end index (next area or end of department)
        end_idx = area_indices[idx + 1] if idx + 1 < len(area_indices) else len(lines)

        # Extract area name
        header_line = lines[start_idx].strip()
        area_name = header_line.replace('## 📍 Area:', '').strip()

        # Get all lines for this area
        area_lines = lines[start_idx + 1:end_idx]

        # Extract workstreams in this area
        workstreams = extract_workstreams(area_lines, generate_id(area_name))

        # Build area object
        area = {
            'id': generate_id(area_name),
            'name': area_name,
            'emoji': '📍',
            'workstreams': workstreams
        }

        areas.append(area)

    return areas


def extract_departments(lines: List[str]) -> List[Dict]:
    """
    Extract all departments from the markdown.

    Args:
        lines: All lines from the markdown file

    Returns:
        List of department dictionaries
    """
    departments = []

    # Find all department headers (format: # N. 🔷 Department Name)
    dept_indices = []
    for i, line in enumerate(lines):
        if re.match(r'^# \d+\.\s*🔷', line.strip()):
            dept_indices.append(i)

    # Parse each department
    for idx, start_idx in enumerate(dept_indices):
        # Determine end index (next department or end of file)
        end_idx = dept_indices[idx + 1] if idx + 1 < len(dept_indices) else len(lines)

        # Extract department name
        header_line = lines[start_idx].strip()
        dept_match = re.match(r'^# \d+\.\s*🔷\s*(.+)$', header_line)
        dept_name = dept_match.group(1).strip() if dept_match else 'Unknown'

        # Get all lines for this department
        dept_lines = lines[start_idx + 1:end_idx]

        # Extract areas in this department
        areas = extract_areas(dept_lines, generate_id(dept_name))

        # Build department object
        department = {
            'id': generate_id(dept_name),
            'name': dept_name,
            'emoji': '🔷',
            'areas': areas
        }

        departments.append(department)

    return departments


def parse_markdown(file_path: str) -> Dict:
    """
    Main parsing function - converts markdown file to structured JSON.

    Args:
        file_path: Path to the markdown file

    Returns:
        Complete data structure with departments, areas, workstreams
    """
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Extract departments (which contain areas and workstreams)
    departments = extract_departments(lines)

    # Calculate metadata
    total_areas = sum(len(dept['areas']) for dept in departments)
    total_workstreams = sum(
        len(area['workstreams'])
        for dept in departments
        for area in dept['areas']
    )

    # Build final structure
    data = {
        'departments': departments,
        'metadata': {
            'version': '2.0',
            'last_updated': datetime.now().strftime('%B %Y'),
            'total_departments': len(departments),
            'total_areas': total_areas,
            'total_workstreams': total_workstreams
        }
    }

    return data


def save_json(data: Dict, output_path: str):
    """
    Save parsed data to JSON file.

    Args:
        data: Parsed data dictionary
        output_path: Path to save JSON file
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    # Test the parser
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input/ConnectHear_Operations_Bible_v2.md'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output/data.json'

    print(f"Parsing {input_file}...")
    data = parse_markdown(input_file)

    print(f"\nExtracted:")
    print(f"  - {data['metadata']['total_departments']} departments")
    print(f"  - {data['metadata']['total_areas']} areas")
    print(f"  - {data['metadata']['total_workstreams']} workstreams")

    print(f"\nSaving to {output_file}...")
    save_json(data, output_file)

    print("✅ Done!")
