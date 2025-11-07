#!/usr/bin/env python3
"""
ConnectHear Operations Portal - Build Script

Orchestrates the complete build process:
1. Parse markdown → JSON
2. Generate JSON → HTML
3. Validate output
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from parser import parse_markdown, save_json
from generator import generate_html


def main():
    print("=" * 70)
    print("     ConnectHear Operations Portal - Build Process")
    print("=" * 70)
    print()

    # Define paths
    input_md = Path('input/ConnectHear_Operations_Bible_v2.md')
    output_json = Path('output/data.json')
    output_html = Path('output/index.html')

    # Ensure output directory exists
    output_json.parent.mkdir(parents=True, exist_ok=True)

    # Step 1: Parse Markdown
    print("STEP 1: Parsing Markdown")
    print("-" * 70)

    if not input_md.exists():
        print(f"❌ Error: Input file not found: {input_md}")
        print("   Please ensure the markdown file exists in the input/ directory.")
        return 1

    print(f"  📄 Input file: {input_md}")
    print(f"  📄 File size: {input_md.stat().st_size / 1024:.1f} KB")
    print()

    try:
        data = parse_markdown(str(input_md))
        print(f"  ✅ Parsed successfully!")
        print(f"     - {data['metadata']['total_departments']} departments")
        print(f"     - {data['metadata']['total_areas']} areas")
        print(f"     - {data['metadata']['total_workstreams']} workstreams")
        print()
    except Exception as e:
        print(f"  ❌ Parsing failed: {e}")
        return 1

    # Step 2: Save JSON (optional)
    print("STEP 2: Saving JSON Data")
    print("-" * 70)

    try:
        save_json(data, str(output_json))
        json_size = output_json.stat().st_size / 1024
        print(f"  ✅ JSON saved to: {output_json}")
        print(f"     - File size: {json_size:.1f} KB")
        print()
    except Exception as e:
        print(f"  ❌ JSON save failed: {e}")
        return 1

    # Step 3: Generate HTML
    print("STEP 3: Generating HTML Portal")
    print("-" * 70)

    try:
        generate_html(data, str(output_html))
        print(f"  ✅ HTML generated successfully!")
        print()
    except Exception as e:
        print(f"  ❌ HTML generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # Step 4: Validation
    print("STEP 4: Validation")
    print("-" * 70)

    if not output_html.exists():
        print(f"  ❌ Output file not found: {output_html}")
        return 1

    html_size = output_html.stat().st_size / 1024 / 1024  # MB
    print(f"  📄 Output file: {output_html}")
    print(f"  📊 File size: {html_size:.2f} MB")

    # Check file size
    if html_size > 10:
        print(f"  ⚠️  Warning: File size is large ({html_size:.2f} MB)")
        print(f"     Consider optimizing if performance is an issue.")
    else:
        print(f"  ✅ File size is good")

    # Validate HTML structure (basic check)
    with open(output_html, 'r', encoding='utf-8') as f:
        html_content = f.read()

    checks = {
        'DOCTYPE': '<!DOCTYPE html>' in html_content,
        'Navigation': 'class="sidebar"' in html_content,
        'Content': 'class="content"' in html_content,
        'Search': 'id="search-input"' in html_content,
        'JavaScript': 'OPERATIONS_DATA' in html_content,
        'CSS': 'class="workstream-section"' in html_content,
    }

    all_passed = True
    for check_name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check_name} check: {'Passed' if passed else 'FAILED'}")
        if not passed:
            all_passed = False

    print()

    # Final summary
    print("=" * 70)
    if all_passed:
        print("✅ BUILD SUCCESSFUL!")
        print()
        print(f"🌐 Your portal is ready: {output_html.absolute()}")
        print()
        print("To view:")
        print(f"  Open in browser: file://{output_html.absolute()}")
        print(f"  Or run: open {output_html}")
    else:
        print("❌ BUILD COMPLETED WITH WARNINGS")
        print()
        print("Some validation checks failed. Please review the output.")

    print("=" * 70)

    return 0 if all_passed else 1


if __name__ == '__main__':
    exit(main())
