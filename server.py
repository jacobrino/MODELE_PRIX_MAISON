from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Chargement du modèle
model = joblib.load('modele_prix_maison.pkl')

# Initialisation de FastAPI
app = FastAPI()

# Définition des données attendues
# Parameters
class HouseData(BaseModel):
    surface: float
    chambres: int
    salles_de_bain: int
    age_maison: int
    garage: int

# Endpoint pour la prédiction
@app.post("/predict")
async def predict_price(data: HouseData):
    print('ici request')
    try:
        input_data = pd.DataFrame({
            'Surface': [data.surface],
            'Chambres': [data.chambres],
            'Salles_de_bain': [data.salles_de_bain],
            'Age_maison': [data.age_maison],
            'Garage': [data.garage]
        })
        prediction = model.predict(input_data)[0]
        return {"prix_previsionnel": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Commande pour lancer le serveur :
# uvicorn server_fastapi:app --reload --host 0.0.0.0 --port 8000
