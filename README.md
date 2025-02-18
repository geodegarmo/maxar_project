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

<h2>Questions or Comments</h2>

Feel free to contact me with any questions or comments at this email address christopher.degarmo@gmail.com.  

Check back soon for more material where urban/rural exists around the globe.

Thank you very much for following along.







