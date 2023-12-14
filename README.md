# Weather Wizard (hackathon sent le caca (dixit amel))

Ce projet a été réalisé dans le cadre du hackathon Copernicus et Hetic. L'objectif principal était de créer un bot de mailing capable de suivre l'évolution du niveau de la mer à partir des données satellitaires disponibles sur le site [Copernicus Marine](https://marine.copernicus.eu/).

Le projet est structuré en trois parties distinctes :

## 1. Conversion des Données et Data Prep
Le fichier récupéré au format .cn est converti en .csv. De plus, une phase de préparation des données (Data Prep) est effectuée pour mieux répondre à notre problématique.

## 2. Analyse des Risques d'Inondation
Nous avons développé un code qui analyse le niveau d'augmentation de l'eau et détermine s'il y a un risque d'inondation associé.

## 3. Notification par Mail
En fonction des résultats de l'analyse de risque, un bot envoie des notifications par e-mail à des personnes de référence qui prendront en charge les cas identifiés.

## Comment Utiliser le Projet
Clonez ce dépôt sur votre machine locale.
Suivez les instructions dans chaque dossier correspondant à l'une des parties du projet.
Dépendances
Assurez-vous d'installer les dépendances nécessaires en utilisant le gestionnaire de paquets spécifié dans chaque partie du projet.

## Contributeurs
Amel Mezemate

Jean-Philippe N'Toumey Bouadan

Mario

Quentin Lonné