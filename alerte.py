import pandas as pd
import numpy as np
import io
import requests


# Chemin du fichier CSV
chemin_fichier = r"./files/bdd.csv"

# Charger le fichier CSV dans un DataFrame
try:
    df = pd.read_csv(chemin_fichier)
    # Afficher les premières lignes du DataFrame pour vérifier
    print(df.head())
except FileNotFoundError:
    print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")


# Téléchargement du fichier csv depuis gi
#response = requests.get(csv_url)
data_csv = pd.read_csv(chemin_fichier)
#print(data_csv.columns)


# calcul de la profondeur de la marée
data_csv['seuil'] = data_csv['depth'] + data_csv['utotal'] * np.cos(np.radians(data_csv['latitude'])) + data_csv['utide'] * np.sin(np.radians(data_csv['latitude']))
# seuil critique 
seuil_critique = 0.53
# verifier si la profondeur de la marée est au dessus ou en dessous du seuil critique 
data_csv['message'] = np.where(data_csv['seuil'] > seuil_critique, 'critique', 'ok')
data_csv['Email'] = 'amel.mezemate@gmail.com'

# Sauvegarder le DataFrame au format CSV
csv_output_path = r'./files/alerte.csv' #créer un path 
data_csv.to_csv(csv_output_path, index=False)