import pandas as pd

# Lis ton fichier CSV en précisant l'encodage latin1 pour corriger les caractères
df = pd.read_csv("Cote match2.csv", encoding="latin1")

# Remplace les caractères mal encodés dans la colonne resultat
df["resultat"] = df["resultat"].str.replace("Ã©", "é")

# Sauvegarde dans un nouveau fichier propre
df.to_csv("Cote match2_corrige.csv", index=False)

print("✅ Fichier corrigé et sauvegardé sous Cote match2_corrige.csv")
