MACHINE LEARNING, PREDICTION DU PRIX D'UNE MAISON
====================================================

DESCRIPTION DU PROJET
----------------------------------------------------
Ce projet implémente un modèle de Machine Learning basé sur une régression linéaire afin de prédire le prix d’une maison (données simulées / logiques en France) à partir de plusieurs paramètres :

- surface
- chambres
- salles_de_bain
- age_maison
- garage

Le modèle est exposé via une API REST FastAPI afin d’effectuer des prédictions en envoyant des données au format JSON.


HISTORIQUE DU DEPOT
----------------------------------------------------
- Création du repository : 2024
- Restructuration du projet : Décembre 2025, dans le cadre d’une mise à jour de portfolio et d’une amélioration de l’organisation des dossiers et fichiers.


FICHIERS PRINCIPAUX
----------------------------------------------------
- Serveur Web FastAPI : server.py
- Code Machine Learning (entraînement + sauvegarde modèle) : main.py
- Port du serveur : 8000


INSTALLATION
----------------------------------------------------
1) Cloner le projet
git clone https://github.com/jacobrino/MODELE_PRIX_MAISON.git

2) cd ML-MODEL-PRIX-MAISON

3) Installer les dépendances
pip install -r requirements.txt


LANCER LE SERVEUR WEB FASTAPI (UVICORN)
----------------------------------------------------
Le serveur est lancé avec Uvicorn sur le port 8000 :

uvicorn server:app --reload --host 0.0.0.0 --port 8000

Une fois lancé, l’API est accessible ici :
http://localhost:8000

Documentation automatique (Swagger) :
http://localhost:8000/docs


TESTER L’API AVEC CURL
----------------------------------------------------
Exemple de requête POST vers /predict :

curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{ "surface": 120, "chambres": 3, "salles_de_bain": 2, "age_maison": 5, "garage": 1 }'

Réponse attendue :
Une réponse JSON contenant le prix prédit selon le modèle entraîné.


DOCKER (OPTIONNEL)
----------------------------------------------------
Le dépôt contient un Dockerfile et un docker-compose.yml.

1) Construction de l’image
docker build -t modele-prix-maison .

2) Lancement du conteneur
docker run -p 8000:8000 modele-prix-maison


DATASET ET MODELE
----------------------------------------------------
- dataset_maisons.csv : dataset d’entraînement
- modele_prix_maison.pkl : modèle entraîné exporté


AUTEUR
----------------------------------------------------
**ANDRIANJARA Jacob Rino**

====================================================
