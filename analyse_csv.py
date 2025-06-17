import pandas as pd

# Charger ton CSV
df = pd.read_csv("Cote match2_corrige.csv")

# Convertir les cotes en float
for col in ["cote_equipe_1", "cote_nul", "cote_equipe_2"]:
    df[col] = df[col].str.replace(",", ".").astype(float)

# Afficher un aperçu
print("Aperçu des données :")
print(df.head())

# Statistiques des cotes (maintenant correctes)
print("\nStatistiques des cotes :")
print(df[["cote_equipe_1", "cote_nul", "cote_equipe_2"]].describe())

# Répartition des résultats
print("\nRépartition des résultats :")
print(df["resultat"].value_counts())

# Vérifier les types
print("\nTypes des colonnes :")
print(df.dtypes)
