import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Génération d'un dataset réaliste pour la France
def generate_dataset(n_samples=1000):
    np.random.seed(42)
    surface = np.random.randint(20, 300, n_samples)  # Superficie entre 20m² et 300m²
    chambres = np.random.randint(1, 8, n_samples)    # Nombre de chambres entre 1 et 7
    salles_de_bain = np.random.randint(1, 4, n_samples)  # Salles de bain entre 1 et 3
    age_maison = np.random.randint(0, 100, n_samples)  # Âge de la maison entre 0 et 100 ans
    garage = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])  # Présence de garage (0: Non, 1: Oui)

    # Prix basé sur les caractéristiques réalistes pour la France
    prix_m2 = np.random.choice([3000, 5000, 7000, 10000], n_samples, p=[0.3, 0.4, 0.2, 0.1])
    prix = (surface * prix_m2) + (chambres * 15000) + (salles_de_bain * 10000) - (age_maison * 500)
    prix += np.where(garage == 1, 15000, 0)
    prix = prix + np.random.normal(0, 15000, n_samples).astype(int)  # Bruit aléatoire avec conversion en int

    df = pd.DataFrame({
        'Surface': surface,
        'Chambres': chambres,
        'Salles_de_bain': salles_de_bain,
        'Age_maison': age_maison,
        'Garage': garage,
        'Prix': prix
    })
    return df

# Entraînement du modèle
def train_model(df,show_graphic):
    X = df.drop('Prix', axis=1)
    y = df['Prix']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

    if show_graphic:
        # Graphique des prix réels vs prédits
        plt.scatter(y_test, predictions)
        plt.xlabel("Prix Réel (€)")
        plt.ylabel("Prix Prédit (€)")
        plt.title("Prix Réel vs Prix Prédit")
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
        plt.show()
    
    return model

# Sauvegarde du modèle
def save_model(model, filename='modele_prix_maison.pkl'):
    joblib.dump(model, filename)
    print(f"Modèle sauvegardé sous {filename}.")

# Chargement du modèle
def load_model(filename):
    model = joblib.load(filename)
    print(f"Modèle chargé depuis {filename}.")
    return model

# Prédiction avec des valeurs personnalisées
def predict_price(model, surface, chambres, salles_de_bain, age_maison, garage):
    data = pd.DataFrame({
        'Surface': [surface],
        'Chambres': [chambres],
        'Salles_de_bain': [salles_de_bain],
        'Age_maison': [age_maison],
        'Garage': [garage]
    })
    predicted_price = model.predict(data)[0]
    print(f"Prix prédit pour les paramètres donnés: {predicted_price:.2f}€")
    return predicted_price


# # Génération du dataset
dataset = generate_dataset(1000)
dataset.to_csv('dataset_maisons.csv', index=False)

dataset = pd.read_csv('/var/www/html/INSI/dataset_maisons.csv')

# # Entraînement du modèle
# model = train_model(dataset,show_graphic=False)
# print("Modèle entraîné avec succès.")

# # Sauvegarde du modèle
# save_model(model)

# Chargement du modèle
loaded_model = load_model('modele_prix_maison.pkl')

# # # Test de prédiction
predict_price(loaded_model, surface=100, chambres=1, salles_de_bain=0, age_maison=1, garage=0)
