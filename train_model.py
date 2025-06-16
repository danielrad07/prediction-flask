import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import pickle

# Charger et convertir
df = pd.read_csv("Cote match2_corrige.csv")
for col in ["cote_equipe_1", "cote_nul", "cote_equipe_2"]:
    df[col] = df[col].str.replace(",", ".").astype(float)

X = df[["cote_equipe_1", "cote_nul", "cote_equipe_2"]]
y = df["resultat"]

# Encoder le y
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Entraîner
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y_encoded)

# Sauvegarder
joblib.dump(model, "modele_cotes.pkl")
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("✅ Modèle et LabelEncoder réentraînés et sauvegardés avec succès.")
