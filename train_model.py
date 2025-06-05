import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Chargement des données
df = pd.read_csv("Cote match2.csv")

# Nettoyage : conversion des virgules en points si nécessaire
for col in ['cote_equipe_1', 'cote_nul', 'cote_equipe_2']:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# Encodage de la cible
encoder = LabelEncoder()
df['target'] = encoder.fit_transform(df['resultat'])

# Séparation X et y
X = df[['cote_equipe_1', 'cote_nul', 'cote_equipe_2']]
y = df['target']

# Entraînement
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Sauvegarde
joblib.dump(model, 'modele_cotes.pkl')
joblib.dump(encoder, 'label_encoder.pkl')

print("✅ Modèle entraîné et sauvegardé.")