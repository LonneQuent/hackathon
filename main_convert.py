#Bibliothèque : 

import netCDF4 as nc
import pandas as pd
import numpy as np 
from numpy.ma import masked_array



# Ouvrir le fichier NetCDF en mode lecture
file_path = r'./files/bdd_brut.nc'  #faire un path auto
nc_file = nc.Dataset(file_path, 'r')

# Afficher la liste des variables
print("Liste des variables dans le fichier NetCDF:")
#for variable_name in nc_file.variables:
#    print(variable_name)

#chargement des données necessaires : 
profondeur = nc_file.variables['depth']
#temps = nc_file.variables['time'][0]
latitude = nc_file.variables['latitude']
longitude = nc_file.variables['longitude']
utotal_variable = nc_file.variables['utotal'][0]
vtotal_variable = nc_file.variables['vtotal'][0]
utide_variable = nc_file.variables['utide'][0]
vtide_variable = nc_file.variables['vtide'][0]


#Traitement sur les données à 4 dimensions : 

# Convertir le tableau masked_array en un tableau normal
array_list = [ma.filled(np.nan) for ma in utotal_variable]
utot_array = np.array(array_list) #result array 

array_list = [ma.filled(np.nan) for ma in vtotal_variable]
vtot_array = np.array(array_list) #result array 

array_list = [ma.filled(np.nan) for ma in utide_variable]
utid_array = np.array(array_list) #result array 

array_list = [ma.filled(np.nan) for ma in vtide_variable]
vtid_array = np.array(array_list) #result array 



#suppression des valeurs manquante (étape facultative)
nan_mask_utot = np.isnan(utot_array[0])
nan_mask_vtot = np.isnan(vtot_array[0])
nan_mask_utid = np.isnan(utid_array[0])
nan_mask_vtid = np.isnan(vtid_array[0])

index = []
for i in range (len(nan_mask_utot)) : 
    #for j in range (len(nan_mask[i])) : #pas la peine la boucle verifier juste la premiere valeur 
        if nan_mask_utot[i][0] or nan_mask_vtot[i][0] or nan_mask_utid[i][0] or nan_mask_vtid[i][0] : 
            index.append(i)

if index:
    utot_f = np.delete(utot_array[0], index, axis=0)
    vtot_f = np.delete(vtot_array[0], index, axis=0)
    utid_f = np.delete(utid_array[0], index, axis=0)
    vtid_f = np.delete(vtid_array[0], index, axis=0)

#le resultat represente les vitesses mesurées sur chaque zone 
    


#le but est de prendre deux zones de differentes coordonnées : 
#1ere pos : (1501,2308) italie / 2eme pos : (1405,3853) japon 
utot_f_ = [np.abs(utotal_variable[0][1501][2308]),np.abs(utotal_variable[0][1405][3853])]
vtot_f_ = [np.abs(vtotal_variable[0][1501][2308]),np.abs(vtotal_variable[0][1405][3853])]
utid_f_ = [np.abs(utide_variable[0][1501][2308]),np.abs(utide_variable[0][1405][3853])]
vtid_f_ = [np.abs(vtide_variable[0][1501][2308]),np.abs(vtide_variable[0][1405][3853])]

#doubler les variables necessaire au calcul de la profondeur: 
depth = [float(profondeur[0]),float(profondeur[0])]
latitude_f = [float(latitude[1501]),float(latitude[1405])]

zone = ['Italie,Venise', 'Japon,Iwaki']

# Créer un DataFrame pandas avec les données
df = pd.DataFrame({
    'zone' : zone, 
    'latitude': latitude_f,
    'depth' : depth, 
    'utotal' : utot_f_, 
    'vtotal' : vtot_f_ , 
    'utide' : utid_f_, 
    'vtide' : vtid_f_ , 
})

# Sauvegarder le DataFrame au format CSV
csv_output_path = r'./files/bdd.csv' #créer un path 
df.to_csv(csv_output_path, index=False)

print(f"Données converties avec succès en {csv_output_path}")
