import netCDF4 as nc
import xarray as xr
import os


# Specify the path to your NetCDF file
nc_file_path = './files/test.nc'

# Open the NetCDF file using xarray
ds = xr.open_dataset(nc_file_path)

# Convert the dataset to a pandas DataFrame
df = ds.to_dataframe()

# Reset the index to make it a flat DataFrame
df = df.reset_index()

# Close the NetCDF file
ds.close()
df_test = df.head(3)

# Specify the path for the CSV file in the "files" directory
csv_file_path = os.path.join('./files', 'output.csv')

# Export the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)