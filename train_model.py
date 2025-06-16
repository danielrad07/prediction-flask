import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import pickle

# Lis les données corrigées
df = pd.read_csv("Cote match2_corrige.csv")

# Charge le label encoder
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Prépare les données
X = df[["cote_1", "cote_n", "cote_2"]]
y = label_encoder.transform(df["resultat"])

# Entraîne le modèle RandomForest
model = RandomForestClassifier()
model.fit(X, y)

# Sauvegarde le modèle
joblib.dump(model, "modele_cotes.pkl")

print("✅ Modèle RandomForest entraîné et sauvegardé avec succès dans modele_cotes.pkl")
