import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

# Open the netCDF file
netcdf_file = 'your_spectral_data.nc'
data = nc.Dataset(netcdf_file, 'r')

# Extract spectral band data
spectral_data = data.variables['your_band_variable'][:]
data.close()

# Create a georeferenced metadata file (e.g., GeoTIFF) if available
metadata_file = 'your_metadata.tif'
with rasterio.open(metadata_file) as src:
    # Display the spectral band data
   
