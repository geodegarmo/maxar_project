# Using open-source tools like DASK AWS and Jupyter Notebooks for Sentinel2A Analysis
<!DOCTYPE html>
<html>
<body>

<p>These tools are valuable for a global solution where we are able to calculate based on multiple lat/lon bounding box examples for a global solution.</p>

<p></p>

<h1>Working With  Python and Kernels in .ipynb</h1>

<p>Download a GUI of your choice, I use visual studio code </p>

<h2>GitHub Resources</h2>

<p>A great resource for using basemaps:</p> 

Leaflet:              https://github.com/Leaflet/Leaflet

Dask: 

<h2>Getting Started</h2>

`mkdir maxar` && cd maxar &&  git clone https://github.com/geodegarmo/maxar_project.git` 


<h2>Create a new virtual environment and Install Dependencies Using the requirement.txt file</h2>

<p>By using a requirements.txt file we skip the dependency issues when calling  `import modules`.</p>

These are the steps for Unix/maxOS:

See this page for windows: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Now check that you are in your directory maxar.  
If not, `cd maxar`

Create a virtual env using pip:
`python3 -m venv .venv`

Activate the virtual environment:
`source .venv/bin/activate`

Confirm that the virtual environment is activated, check the location of your python interpreter:
`which python`

Install using pip and the requirements.txt file:
pip install -r /path/to/requirements.txt

Now test that this works after activating your kernel inside Visual Studio Code:
https://code.visualstudio.com/docs/datascience/jupyter-kernel-management

Test by running the `import modules` portion of the  access_Sentinel_2_data_aws_SF_Search.ipynb

<h2>Questions or Comments</h2>
Feel free to contact me with any questions or comments at this email address christopher.degarmo@gmail.com.  

Thank you very much for following along.







