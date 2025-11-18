#!/usr/bin/env python3
"""Debug script to test Process Steps parsing"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from parser import parse_process_steps

# Test data - actual format from markdown
test_lines = [
    "**Process Steps:**",
    "",
    "#### 1. Receive and Verify Invoice",
    "- Receive invoice from vendor (email or physical delivery)",
    "- Check invoice includes: Vendor name and NTN",
    "- If incomplete → Email vendor requesting missing information",
    "",
    "#### 2. Verify Purchase Order (PO)",
    "- Check if invoice references a PO number",
    "- If YES: Login to ERPNext",
    "",
    "#### Decision Points",
    "**If invoice > PKR 10,000:** Get approval from Arhum/Azima",
    "**If vendor docs missing:** Stop process, request documents",
    "",
    "#### Common Issues",
    "**Issue:** Vendor not in ERPNext",
    "**Solution:** Create new supplier first",
    "",
    "#### Tools & Access Required",
    "- ERPNext (Finance role) - https://hub.connecthear.org",
    "- HBL Bank Portal",
    "",
    "#### Key Thresholds",
    "- Withholding Tax Rate: 4%",
    "- Approval Threshold: PKR 10,000",
    "",
    "---"
]

print("Testing Process Steps Parser")
print("=" * 60)
print()

result, next_idx = parse_process_steps(test_lines, 0)

print(f"Parsed {len(result['steps'])} steps")
print(f"Parsed {len(result['decision_points'])} decision points")
print(f"Parsed {len(result['common_issues'])} common issues")
print(f"Parsed {len(result['tools'])} tools")
print()

print("Steps:")
for step in result['steps']:
    print(f"  {step['number']}. {step['title']}")
    for detail in step['details']:
        print(f"     - {detail}")
print()

print("Decision Points:")
for dp in result['decision_points']:
    print(f"  {dp['condition']}: {dp['action']}")
print()

print("Common Issues:")
for issue in result['common_issues']:
    print(f"  Issue: {issue['issue']}")
    print(f"  Solution: {issue['solution']}")
print()

print("Tools:")
for tool in result['tools']:
    print(f"  - {tool}")
