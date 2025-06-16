import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Lis le fichier corrigé
df = pd.read_csv("Cote match2_corrige.csv")

# Crée et entraine le LabelEncoder sur la colonne "resultat"
label_encoder = LabelEncoder()
label_encoder.fit(df["resultat"])

# Sauvegarde
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("✅ label_encoder.pkl recréé avec succès à partir de Cote match2_corrige.csv")
