import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib

# --- Chargement des données ---
df = pd.read_csv('Cote match2_corrige.csv')

# Remplacer les virgules par des points et convertir en float quand c'est possible
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.replace(',', '.')
        df[col] = pd.to_numeric(df[col], errors='ignore')

target_col = 'resultat'

# Séparation features / cible
X = df.drop(columns=[target_col])
y = df[target_col]

# Encodage des labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split stratifié
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.25, random_state=42, stratify=y_encoded)

# Standardisation des features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Définition des modèles
xgb = XGBClassifier(eval_metric='mlogloss', random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# VotingClassifier avec XGB et RF
ensemble = VotingClassifier(
    estimators=[('xgb', xgb), ('rf', rf)],
    voting='soft'
)

# Entraînement
ensemble.fit(X_train_scaled, y_train)

# Prédiction et rapport
y_pred = ensemble.predict(X_test_scaled)
print("📊 Rapport classification sur test set :")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Sauvegarde des objets
joblib.dump(ensemble, 'modele_ensemble.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("✅ Modèle, scaler et label encoder sauvegardés.")