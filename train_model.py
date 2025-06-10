import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Charger les données
df = pd.read_csv('Cote match2.csv')

# Nettoyer : remplacer les virgules par des points et convertir en float
for col in ['cote_equipe_1', 'cote_nul', 'cote_equipe_2']:
    df[col] = df[col].astype(str).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Supprimer les lignes incomplètes
df.dropna(subset=['cote_equipe_1', 'cote_nul', 'cote_equipe_2', 'resultat'], inplace=True)

# Définir X et y
X = df[['cote_equipe_1', 'cote_nul', 'cote_equipe_2']]
y = df['resultat']

# Séparer en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluer
y_pred = model.predict(X_test)
print("🔍 Précision du modèle :", round(accuracy_score(y_test, y_pred), 2))
print("\n📊 Rapport de classification :\n", classification_report(y_test, y_pred))

# Sauvegarder le modèle
joblib.dump(model, 'modele_cotes.pkl')
print("\n✅ Modèle sauvegardé sous 'modele_cotes.pkl'")
