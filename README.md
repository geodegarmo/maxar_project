# Using Open-Source tools and DASK, AWS, and Jupyter Notebook for Sentinel-2A Image Analysis
<!DOCTYPE html>
<html>
<body>

<p>These tools are valuable for a global solution.</p>


<h1>Working With  Python and Kernels in Ipykernel Jupyter Notebook</h1>

<p>Download a GUI of your choice, for this example we used Visual Studio Code</p>

<h2>GitHub Resources</h2>

<p>A great resource for using basemaps:</p> 

Leaflet: https://github.com/Leaflet/Leaflet

Dask: https://odc-stac.readthedocs.io/en/latest/intro.html

<h2>Getting Started</h2>

````mkdir maxar && cd maxar && git clone https://github.com/geodegarmo/maxar_project.git```` 

<h2>Create a new virtual environment and Install Dependencies with A Requirements File.</h2>

<p>By using a requirements.txt file we skip dependency issues.</p>

These are the steps for Unix/macOS:

See this page for windows: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Change directory to maxar.  

If not, `cd maxar`

Create a virtual environment using pip:

````python3 -m venv .venv````

Activate the virtual environment:

```source .venv/bin/activate```

Confirm that the virtual environment is activated, check the location of your python interpreter:

```which python```

Install using pip and the requirements.txt file:

```pip install -r /path/to/requirements.txt```

Activate your kernel, Visual Studio Code:

https://code.visualstudio.com/docs/datascience/jupyter-kernel-management

Test by running the `import modules` portion of the `access_Sentinel_2_data_aws_SF_Search.ipynb`

<h2>Available Notebooks</h2>

<h3>1. San Francisco Bay Area Analysis</h3>

- `access_Sentinel_2_data_aws_SF_Search.ipynb` - Original San Francisco analysis using Sentinel-2 data
- `access_Sentinel_2_data_aws_newSearch.ipynb` - Updated San Francisco search examples

<h3>2. North Carolina Hurricane Helene Analysis (NEW)</h3>

- **Notebook**: `notebooks/north_carolina_hurricane_helene_analysis.ipynb`
- **Documentation**: `notebooks/README_NC_ANALYSIS.md`

This notebook provides comprehensive analysis of Hurricane Helene's impact on North Carolina:
- **EPSG Projection**: EPSG:32617 (UTM Zone 17N for North Carolina)
- **Water Detection**: Automated water area detection using NDWI and MNDWI indices
- **Hurricane Date**: September 27, 2024
- **Before Period**: 3 months before hurricane (June 27 - September 27, 2024)
- **After Period**: 3 months after hurricane (September 27 - December 27, 2024)
- **Historical Analysis**: Optional 10-year water coverage trend analysis (2015-2024)
- **Study Area**: Western North Carolina (Asheville region)

Features:
- Automated Sentinel-2 imagery queries with cloud cover filtering
- Binary water masks for flood detection
- Before/after comparison visualizations
- Change detection analysis
- GeoTIFF export capabilities
- Comprehensive documentation

See `notebooks/README_NC_ANALYSIS.md` for detailed usage instructions.

<h2>Questions or Comments</h2>

Feel free to contact me with any questions or comments at this email address christopher.degarmo@gmail.com.  

Check back soon for more material where urban/rural exists around the globe.

Thank you very much for following along.







