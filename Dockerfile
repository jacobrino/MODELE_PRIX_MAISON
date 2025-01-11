# 1️⃣ Utiliser une image Python légère
FROM python:3.10-slim

# 2️⃣ Définir le répertoire de travail
WORKDIR /app

# 3️⃣ Copier uniquement les fichiers nécessaires
COPY requirements.txt .
COPY server.py .
COPY dataset_maisons.csv .
COPY modele_prix_maison.pkl .


# 4️⃣ Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Exposer le port 8000 pour FastAPI
EXPOSE 8000

# 6️⃣ Commande pour lancer le serveur FastAPI
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
