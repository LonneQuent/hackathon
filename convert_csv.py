import netCDF4 as nc
import xarray as xr
import os


# Specify the path to your NetCDF file
nc_file_path = './files/CMEMS_v6r1_IBI_PHY_NRT_NL_01mav_20230101_20230131_R20230131_AN01.nc'

# Open the NetCDF file using xarray
ds = xr.open_dataset(nc_file_path)

# Convert the dataset to a pandas DataFrame
df = ds.to_dataframe()

# Reset the index to make it a flat DataFrame
df = df.reset_index()

# Obtenez les valeurs maximales de latitude et longitude
max_latitude = df['latitude'].max()
max_longitude = df['longitude'].max()

# Affichez les valeurs maximales
print("Latitude maximale :", max_latitude)
print("Longitude maximale :", max_longitude)

# Filtrer les données en fonction de coordonnées qui commencent par 45 de latitude et 12 de longitude
filtered_df = df[(df['latitude'] >= 52) & (df['longitude'] >= 4)]

# Affichez le DataFrame filtré
filtered_df.head(80)


# Close the NetCDF file
ds.close()
df_test = df.head(3)

# Specify the path for the CSV file in the "files" directory
csv_file_path = os.path.join('./files', 'output.csv')

# Export the DataFrame to a CSV file
#df.to_csv(csv_file_path, index=False)