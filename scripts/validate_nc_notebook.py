#!/usr/bin/env python3
"""
Validation script for the North Carolina Hurricane Helene analysis notebook.
This script validates the notebook structure and checks key components.
"""
import json
import sys

def validate_notebook(notebook_path):
    """Validate the North Carolina Hurricane Helene analysis notebook"""
    
    print("=" * 60)
    print("North Carolina Hurricane Helene Analysis Notebook Validation")
    print("=" * 60)
    
    try:
        # Load notebook
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
        print(f"✓ Successfully loaded notebook from {notebook_path}")
    except Exception as e:
        print(f"✗ Failed to load notebook: {e}")
        return False
    
    # Check notebook format
    if 'nbformat' not in nb or 'nbformat_minor' not in nb:
        print("✗ Invalid notebook format: missing nbformat")
        return False
    print(f"✓ Notebook format: {nb['nbformat']}.{nb['nbformat_minor']}")
    
    # Check cells exist
    if 'cells' not in nb or not nb['cells']:
        print("✗ No cells found in notebook")
        return False
    print(f"✓ Found {len(nb['cells'])} cells")
    
    # Count cell types
    markdown_cells = [c for c in nb['cells'] if c['cell_type'] == 'markdown']
    code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    print(f"  - Markdown cells: {len(markdown_cells)}")
    print(f"  - Code cells: {len(code_cells)}")
    
    # Check for key content
    all_content = ' '.join([''.join(cell.get('source', [])) for cell in nb['cells']])
    
    required_items = {
        'EPSG:32617': 'North Carolina EPSG projection',
        'Hurricane Helene': 'Hurricane reference',
        'September 27, 2024': 'Hurricane date',
        'NDWI': 'Water detection index',
        'MNDWI': 'Modified water detection index',
        'calculate_ndwi': 'NDWI function',
        'calculate_mndwi': 'MNDWI function',
        'create_water_mask': 'Water mask function',
        'sentinel-2-l2a': 'Sentinel-2 data',
        'stac_load': 'Data loading',
        'query_historical_data': '10-year analysis function',
        'before_start': 'Before period',
        'after_start': 'After period',
    }
    
    print("\nValidating key components:")
    all_found = True
    for item, description in required_items.items():
        if item in all_content:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ Missing: {description} ({item})")
            all_found = False
    
    # Check for specific functionality
    print("\nValidating functionality sections:")
    
    sections_to_check = [
        ('# North Carolina Hurricane Helene Analysis', 'Title section'),
        ('## Define North Carolina Area of Interest', 'Area of interest definition'),
        ('## Query Sentinel-2 Data: 3 Months Before', 'Before period query'),
        ('## Query Sentinel-2 Data: 3 Months After', 'After period query'),
        ('## Water Detection Function', 'Water detection implementation'),
        ('## 10-Year Historical Analysis', 'Historical analysis section'),
        ('## Compare Water Areas Before and After', 'Comparison section'),
    ]
    
    for section, description in sections_to_check:
        if section in all_content:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ Missing section: {description}")
            all_found = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_found:
        print("✓ VALIDATION PASSED: All required components found!")
        print("=" * 60)
        return True
    else:
        print("✗ VALIDATION FAILED: Some components are missing")
        print("=" * 60)
        return False

if __name__ == "__main__":
    import os
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to repo root, then into notebooks
    notebook_path = os.path.join(script_dir, '..', 'notebooks', 'north_carolina_hurricane_helene_analysis.ipynb')
    
    success = validate_notebook(notebook_path)
    
    if success:
        print("\nThe North Carolina Hurricane Helene analysis notebook is ready to use!")
        print("\nNext steps:")
        print("1. Open the notebook in Jupyter")
        print("2. Ensure all dependencies are installed (see requirements.txt)")
        print("3. Run cells sequentially to perform the analysis")
        print("4. See notebooks/README_NC_ANALYSIS.md for detailed instructions")
        sys.exit(0)
    else:
        print("\nPlease check the notebook and ensure all components are present.")
        sys.exit(1)
