#!/usr/bin/env python3
"""Test if parse_process_steps is being called and what it receives"""

import sys
import re
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

# Read the markdown file
with open('input/ConnectHear_Operations_Bible_v2.1_WITH_PROCESS_STEPS.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Find the first **Process Steps:** line
for i, line in enumerate(lines):
    if line.strip() == '**Process Steps:**':
        print(f"Found **Process Steps:** at line {i}")
        print(f"Next 20 lines:")
        for j in range(i, min(i+20, len(lines))):
            print(f"  {j}: {repr(lines[j][:80])}")
        break

# Test the regex pattern
test_line = "#### 1. Receive and Verify Invoice"
subsection_title = test_line.replace('####', '').strip()
print(f"\nTest line: {repr(test_line)}")
print(f"After removing ####: {repr(subsection_title)}")

step_match = re.match(r'^(\d+)\.\s*(.+)$', subsection_title)
if step_match:
    print(f"MATCHED! Number: {step_match.group(1)}, Title: {step_match.group(2)}")
else:
    print("NO MATCH")
