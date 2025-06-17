import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement
df = pd.read_csv('Cote match2_corrige.csv')

# Nettoyage cotes (virgules -> points)
for col in ['cote_equipe_1', 'cote_nul', 'cote_equipe_2']:
    df[col] = df[col].str.replace(',', '.').astype(float)

# 1. Aperçu général
print("\n=== Aperçu général ===")
print(df.info())
print("\nValeurs manquantes :")
print(df.isnull().sum())

# 2. Statistiques descriptives
print("\n=== Statistiques descriptives ===")
print(df.describe())

# 3. Analyse de la cible
print("\n=== Répartition des classes ===")
print(df['resultat'].value_counts(normalize=True))
sns.countplot(data=df, x='resultat')
plt.title("Répartition des résultats")
plt.show()

# 4. Visualisation cotes par classe
plt.figure(figsize=(14,6))
for i, col in enumerate(['cote_equipe_1', 'cote_nul', 'cote_equipe_2']):
    plt.subplot(1,3,i+1)
    sns.boxplot(x='resultat', y=col, data=df)
    plt.title(f"Distribution de {col} selon le résultat")
plt.tight_layout()
plt.show()

# 5. Matrice de corrélation
corr = df[['cote_equipe_1', 'cote_nul', 'cote_equipe_2']].corr()
print("\n=== Matrice de corrélation entre cotes ===")
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Corrélations entre cotes")
plt.show()

# 6. Scatter plots entre cotes
sns.pairplot(df, vars=['cote_equipe_1', 'cote_nul', 'cote_equipe_2'], hue='resultat')
plt.suptitle("Pairplot des cotes selon résultat", y=1.02)
plt.show()

# 7. Recherche d’outliers (valeurs extrêmes)
for col in ['cote_equipe_1', 'cote_nul', 'cote_equipe_2']:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    low_bound = q1 - 1.5 * iqr
    up_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < low_bound) | (df[col] > up_bound)]
    print(f"\nOutliers détectés pour {col} : {len(outliers)}")
    if len(outliers) > 0:
        display(outliers[['resultat', col]])

# 8. Features dérivées simples
df['diff_cote_equipe1_2'] = df['cote_equipe_1'] - df['cote_equipe_2']
df['mean_cote'] = df[['cote_equipe_1', 'cote_nul', 'cote_equipe_2']].mean(axis=1)

plt.figure(figsize=(12,5))
sns.boxplot(x='resultat', y='diff_cote_equipe1_2', data=df)
plt.title("Différence cote équipe 1 - équipe 2 par résultat")
plt.show()

plt.figure(figsize=(12,5))
sns.boxplot(x='resultat', y='mean_cote', data=df)
plt.title("Moyenne des cotes par résultat")
plt.show()

# 9. Suggestions pour enrichir les données (à considérer) :
print("""
=== Suggestions pour enrichir les données ===
- Ajouter des stats sur les équipes (classement, forme récente, historique confrontations)
- Ajouter des facteurs contextuels (lieu du match, conditions)
- Ajouter des indicateurs dérivés (différences, ratios, tendance des cotes dans le temps)
- Intégrer des données externes (performance des joueurs, blessures, etc.)
""")