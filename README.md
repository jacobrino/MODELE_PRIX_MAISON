LIEN GITHUB: https://github.com/jacobrino/MODELE_PRIX_MAISON.git

PORT DU SERVEUR WEB: 8000
FICHIER DU SERVEUR WEB : server.py
FICHIER CONTENANT LE CODE DU MACHINE LEARNING: main.py

POUR TESTER L'API ON PEUT UTILISER LA COMMANDE CURL
"
curl -X POST http://localhost:8000/predict   -H "Content-Type: application/json"   -d '{
    "surface": 120,
    "chambres": 3,
    "salles_de_bain": 2,
    "age_maison": 5,
    "garage": 1
  }'
"

  POUR LANCER LE SERVEUR WEB FAST API ON A UTILISE LE DAEMON UVICORN
  uvicorn server:app --reload --host 0.0.0.0 --port 8000


"
…or push an existing repository from the command line

git remote add origin https://github.com/jacobrino/MODELE_PRIX_MAISON.git
git branch -M main
git push -u origin main
"
"
…or create a new repository on the command line

echo "# MODELE_PRIX_MAISON" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jacobrino/MODELE_PRIX_MAISON.git
git push -u origin main
"


