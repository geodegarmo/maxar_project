# North Carolina Hurricane Helene Analysis

## Overview

This notebook analyzes water area changes in North Carolina before and after Hurricane Helene, which made landfall on September 27, 2024. The analysis uses Sentinel-2 satellite imagery from AWS to detect and quantify changes in water extent.

## Key Features

### 1. **EPSG Projection for North Carolina**
- Uses **EPSG:32617** (UTM Zone 17N)
- Appropriate for North Carolina's geographic location
- Ensures accurate spatial analysis

### 2. **Water Area Detection**
The notebook implements two water detection indices:
- **NDWI (Normalized Difference Water Index)**: `(Green - NIR) / (Green + NIR)`
- **MNDWI (Modified NDWI)**: `(Green - SWIR) / (Green + SWIR)`

MNDWI is used by default as it better distinguishes water from built-up areas.

### 3. **Before and After Hurricane Analysis**
- **Before Period**: June 27, 2024 - September 27, 2024 (3 months before)
- **After Period**: September 27, 2024 - December 27, 2024 (3 months after)
- Automatically queries Sentinel-2 L2A data with < 20% cloud cover

### 4. **10-Year Historical Analysis (Optional)**
- Supports querying historical data from 2015-2024 (Sentinel-2 availability)
- Analyzes long-term trends in water coverage
- Useful for understanding baseline conditions and climate patterns

## Study Area

The analysis focuses on **Western North Carolina**, particularly the Asheville region, which was heavily impacted by Hurricane Helene. The default bounding box covers approximately 100km x 100km centered on Asheville.

### Coordinates
- Center: (-82.5515°, 35.5951°) - Asheville, NC
- Radius: ~50 km

## Analysis Outputs

### Visualizations
1. **RGB Composite Images**: True-color imagery before and after the hurricane
2. **MNDWI Maps**: Water index values (-0.5 to 0.5 scale)
3. **Binary Water Masks**: Clear delineation of water areas
4. **Change Detection Map**: Shows new water areas (flooding) vs. water loss

### Statistics
- Number of water pixels detected
- Percentage of water coverage
- Net change in water extent
- Areas of new flooding vs. water recession

### Optional Exports
The notebook includes commented code to export results as GeoTIFF files:
- `water_mask_before_hurricane.tif`
- `water_mask_after_hurricane.tif`
- `water_change_hurricane_helene.tif`

## Requirements

All required packages are listed in the repository's `requirements.txt`:
- `pystac-client`: For querying STAC catalogs
- `odc-stac`: For loading and processing satellite data
- `dask`: For distributed computing
- `geopandas`: For spatial data handling
- `matplotlib`: For visualization
- `xarray`: For multi-dimensional array processing
- `numpy`: For numerical operations

## Usage

### Basic Usage
1. Open the notebook in Jupyter
2. Run cells sequentially
3. The notebook will automatically:
   - Query available Sentinel-2 imagery
   - Download and process the data
   - Generate water masks
   - Create comparison visualizations

### Advanced Usage: 10-Year Analysis
To run the historical analysis:
1. Locate the "10-Year Historical Analysis" section
2. Uncomment the analysis code
3. Be prepared for longer processing time
4. Results will show water coverage trends from 2015-2024

### Customization Options
You can modify:
- **Study area**: Change `nc_west_center` and `r` (radius) variables
- **Date ranges**: Adjust the time period for before/after analysis
- **Cloud cover threshold**: Modify the `query` parameter (default: < 20%)
- **Resolution**: Change `resolution` parameter (default: 100m)
- **Water detection threshold**: Adjust `threshold` in `create_water_mask()` function
- **Historical analysis period**: Modify `start_year`, `end_year`, and `month` parameters

## Technical Notes

### EPSG:32617 (UTM Zone 17N)
- Covers North Carolina's longitude range
- Preserves shape and distance accurately
- Uses meters as the unit of measurement
- Optimal for regional analysis

### Water Detection Thresholds
- Default threshold: 0.0 for MNDWI
- Values > 0 typically indicate water
- Adjust threshold based on local conditions and desired sensitivity

### Data Availability
- Sentinel-2 data available from 2015 onwards
- Revisit time: ~5 days
- Resolution: 10m-60m depending on band
- Free and open access via AWS

### Performance Considerations
- Uses Dask for distributed computing
- Chunked data loading for memory efficiency
- 100m resolution balances detail and performance
- Full 10-year analysis may take significant time

## Hurricane Helene Context

Hurricane Helene made landfall on September 27, 2024, causing significant flooding in Western North Carolina, particularly around Asheville. This analysis helps:
- Quantify the extent of flooding
- Identify affected areas
- Compare to historical baseline
- Support recovery and planning efforts

## References

- Sentinel-2 Data: https://registry.opendata.aws/sentinel-2-l2a-cogs/
- STAC Catalog: https://earth-search.aws.element84.com/v1/
- ODC-STAC Documentation: https://odc-stac.readthedocs.io/
- Water Index Research: McFeeters (1996), Xu (2006)

## Author

Created as part of the maxar_project repository for geospatial analysis and disaster response.

## License

This notebook uses open-source tools and free satellite data. Please respect data provider terms of use.
