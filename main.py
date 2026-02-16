# ============================================================================
# PROJET PYTHON ORIENTÉ DATA - PROJECTIONS DES SENIORS EN FRANCE
# Dataset : Projections de population seniors et perte d'autonomie (2021-2070)
# ============================================================================

import pandas as pd
import plotly.express as px

# Chargement des données
print("Chargement des données en cours...")
df = pd.read_csv('data/epp4_sc_central_hyp_intermediaire.csv', sep=';')
print("✅ Données chargées et préparées.")
print(f"📊 {len(df)} lignes, {len(df.columns)} colonnes\n")

# ============================================================================
# NIVEAU 1 : AFFICHAGE ET FILTRAGE SIMPLE
# ============================================================================

print("=" * 80)
print("NIVEAU 1 : AFFICHAGE ET FILTRAGE SIMPLE")
print("=" * 80)

# 1. Afficher toutes les colonnes du dataset
print("\n1. Afficher toutes les colonnes disponibles")
print(df.columns.to_list())

# 2. Afficher tous les départements
print("\n2. Afficher tous les départements uniques")
print(df['DEP'].unique())

# 3. Afficher toutes les années
print("\n3. Afficher toutes les années disponibles")
print(sorted(df['ANNEE'].unique()))

# 4. Afficher toutes les tranches d'âge
print("\n4. Afficher toutes les tranches d'âge")
print(df['TRAGE'].unique())


# ============================================================================
# NIVEAU 2 : REQUÊTES CIBLÉES (FILTRAGE AVEC CONDITIONS)
# ============================================================================

print("\n" + "=" * 80)
print("NIVEAU 2 : REQUÊTES CIBLÉES")
print("=" * 80)

# 1. Quel est le nombre de seniors dans le département 75 (Paris) en 2021 ?
print("\n1. Nombre de seniors à Paris (75) en 2021")
result = df[(df['DEP'] == '75') & (df['ANNEE'] == 2021)]['vol_seniors'].sum()
print(f"Réponse : {result:,.0f} seniors")

# Ou de manière plus détaillée :
paris_2021 = df.loc[(df['DEP'] == '75') & (df['ANNEE'] == 2021), 'vol_seniors']
print(f"Détail : {paris_2021.sum():,.0f} seniors")

# 2. Quelle est l'espérance de vie à 60 ans pour les hommes (SEXE=1) en 2050 ?
print("\n2. Espérance de vie à 60 ans pour les hommes en 2050")
esp_vie_h = df.loc[(df['SEXE'] == 1) & (df['ANNEE'] == 2050), 'esp_vie_60_ans'].iloc[0]
print(f"Réponse : {esp_vie_h:.2f} ans")

# 3. Combien de seniors de 85+ ans y aura-t-il dans le département 13 (Bouches-du-Rhône) en 2040 ?
print("\n3. Seniors de 85+ ans dans le département 13 en 2040")
seniors_85 = df.loc[(df['DEP'] == '13') & (df['ANNEE'] == 2040) & (df['TRAGE'] == '85+'), 'vol_seniors'].sum()
print(f"Réponse : {seniors_85:,.0f} seniors")

# 4. Quel est le nombre de seniors en perte d'autonomie sévère en institution dans le département 69 en 2030 ?
print("\n4. Seniors en perte d'autonomie sévère en institution (dép. 69, 2030)")
pa_severe = df.loc[(df['DEP'] == '69') & (df['ANNEE'] == 2030), 'vol_seniors_perte_autonomie_severe_institution'].sum()
print(f"Réponse : {pa_severe:,.0f} personnes")


# ============================================================================
# NIVEAU 3 : AGRÉGATIONS (GROUPBY, SUM, MEAN)
# ============================================================================

print("\n" + "=" * 80)
print("NIVEAU 3 : AGRÉGATIONS")
print("=" * 80)

# 1. Quel est le nombre total de seniors par année ?
print("\n1. Nombre total de seniors par année")
seniors_par_annee = df.groupby('ANNEE')['vol_seniors'].sum()
print(seniors_par_annee.head(10))

# 2. Quel est le nombre total de seniors par département en 2021 ?
print("\n2. Nombre total de seniors par département en 2021")
seniors_par_dep_2021 = df[df['ANNEE'] == 2021].groupby('DEP')['vol_seniors'].sum()
print(seniors_par_dep_2021.head(10))

# 3. Quelle est la répartition des seniors par tranche d'âge en 2021 ?
print("\n3. Répartition des seniors par tranche d'âge en 2021")
seniors_par_age_2021 = df[df['ANNEE'] == 2021].groupby('TRAGE')['vol_seniors'].sum()
print(seniors_par_age_2021)

# 4. Quel est le nombre moyen de seniors en perte d'autonomie par département en 2025 ?
print("\n4. Nombre moyen de seniors en perte d'autonomie par département (2025)")
moy_pa_2025 = df[df['ANNEE'] == 2025].groupby('DEP')['vol_seniors_perte_autonomie'].mean()
print(f"Moyenne : {moy_pa_2025.mean():,.0f} personnes par département")

# 5. Quel est le nombre total de seniors par sexe en 2030 ?
print("\n5. Nombre total de seniors par sexe en 2030")
seniors_par_sexe_2030 = df[df['ANNEE'] == 2030].groupby('SEXE')['vol_seniors'].sum()
print("Hommes (1) :", f"{seniors_par_sexe_2030[1]:,.0f}")
print("Femmes (2) :", f"{seniors_par_sexe_2030[2]:,.0f}")


# ============================================================================
# NIVEAU 4 : FILTRES AVANCÉS (CONDITIONS MULTIPLES)
# ============================================================================

print("\n" + "=" * 80)
print("NIVEAU 4 : FILTRES AVANCÉS")
print("=" * 80)

# 1. Quels départements auront plus de 100 000 seniors en 2050 ?
print("\n1. Départements avec plus de 100 000 seniors en 2050")
dep_2050 = df[df['ANNEE'] == 2050].groupby('DEP')['vol_seniors'].sum()
dep_plus_100k = dep_2050[dep_2050 > 100000]
print(f"{len(dep_plus_100k)} départements concernés :")
print(dep_plus_100k.sort_values(ascending=False).head(10))

# 2. Quels départements auront plus de 10 000 seniors de 85+ ans en 2060 ?
print("\n2. Départements avec plus de 10 000 seniors de 85+ en 2060")
dep_85_2060 = df[(df['ANNEE'] == 2060) & (df['TRAGE'] == '85+')].groupby('DEP')['vol_seniors'].sum()
dep_85_plus_10k = dep_85_2060[dep_85_2060 > 10000]
print(f"{len(dep_85_plus_10k)} départements concernés")
print(dep_85_plus_10k.sort_values(ascending=False))

# 3. Dans quels départements l'espérance de vie à 60 ans des femmes dépassera 30 ans en 2070 ?
print("\n3. Départements où espérance de vie femmes à 60 ans > 30 ans (2070)")
esp_vie_f_2070 = df[(df['ANNEE'] == 2070) & (df['SEXE'] == 2)]
dep_esp_vie_30 = esp_vie_f_2070[esp_vie_f_2070['esp_vie_60_ans'] > 30]['DEP'].unique()
print(f"{len(dep_esp_vie_30)} départements")
print(list(dep_esp_vie_30))


# ============================================================================
# NIVEAU 5 : TRIS ET CLASSEMENTS (SORT, HEAD, TAIL)
# ============================================================================

print("\n" + "=" * 80)
print("NIVEAU 5 : TRIS ET CLASSEMENTS")
print("=" * 80)

# 1. Quelle est l'année avec le plus de seniors projetés ?
print("\n1. Année avec le plus de seniors")
seniors_par_annee = df.groupby('ANNEE')['vol_seniors'].sum()
annee_max = seniors_par_annee.idxmax()
print(f"Réponse : {annee_max} avec {seniors_par_annee.max():,.0f} seniors")

# 2. Quels sont les 5 départements avec le plus de seniors en 2040 ?
print("\n2. Top 5 des départements avec le plus de seniors en 2040")
top5_2040 = df[df['ANNEE'] == 2040].groupby('DEP')['vol_seniors'].sum().sort_values(ascending=False).head(5)
print(top5_2040)

# 3. Quels sont les 3 départements avec le moins de seniors en perte d'autonomie en 2025 ?
print("\n3. Top 3 des départements avec le moins de seniors en perte d'autonomie (2025)")
bottom3_pa_2025 = df[df['ANNEE'] == 2025].groupby('DEP')['vol_seniors_perte_autonomie'].sum().sort_values().head(3)
print(bottom3_pa_2025)

# 4. Quels sont les 10 départements où l'espérance de vie à 60 ans est la plus élevée en 2050 ?
print("\n4. Top 10 départements avec la meilleure espérance de vie à 60 ans (2050)")
esp_vie_2050 = df[df['ANNEE'] == 2050].groupby('DEP')['esp_vie_60_ans'].mean().sort_values(ascending=False).head(10)
print(esp_vie_2050)


# ============================================================================
# NIVEAU 6 : VISUALISATIONS AVEC PLOTLY
# ============================================================================

print("\n" + "=" * 80)
print("NIVEAU 6 : VISUALISATIONS")
print("=" * 80)

# 1. Évolution du nombre total de seniors en France (2021-2070)
print("\n1. Création du graphique : Évolution des seniors en France")
evolution_seniors = df.groupby('ANNEE')['vol_seniors'].sum().reset_index()
fig1 = px.line(
    evolution_seniors,
    x='ANNEE',
    y='vol_seniors',
    title='Évolution du nombre total de seniors en France (2021-2070)',
    labels={'vol_seniors': 'Nombre de seniors', 'ANNEE': 'Année'}
)
fig1.show()  
print("✅ Graphique 1 créé")

# 2. Répartition des seniors par tranche d'âge en 2021 (Pie Chart)
print("\n2. Création du graphique : Répartition par âge en 2021")
repartition_age_2021 = df[df['ANNEE'] == 2021].groupby('TRAGE')['vol_seniors'].sum().reset_index()
fig2 = px.pie(
    repartition_age_2021,
    values='vol_seniors',
    names='TRAGE',
    title='Répartition des seniors par tranche d\'âge en 2021'
)
fig2.show()  
print("✅ Graphique 2 créé")

# 3. Top 10 des départements avec le plus de seniors en 2050
print("\n3. Création du graphique : Top 10 départements en 2050")
top10_dep_2050 = df[df['ANNEE'] == 2050].groupby('DEP')['vol_seniors'].sum().sort_values(ascending=False).head(10).reset_index()
fig3 = px.bar(
    top10_dep_2050,
    x='DEP',
    y='vol_seniors',
    title='Top 10 des départements avec le plus de seniors en 2050',
    labels={'vol_seniors': 'Nombre de seniors', 'DEP': 'Département'}
)
fig3.show()  
print("✅ Graphique 3 créé")

# 4. Évolution de la perte d'autonomie en France
print("\n4. Création du graphique : Évolution perte d'autonomie")
evolution_pa = df.groupby('ANNEE')[['vol_seniors', 'vol_seniors_perte_autonomie', 'vol_seniors_perte_autonomie_severe']].sum().reset_index()
fig4 = px.line(
    evolution_pa,
    x='ANNEE',
    y=['vol_seniors', 'vol_seniors_perte_autonomie', 'vol_seniors_perte_autonomie_severe'],
    title='Évolution des seniors et de la perte d\'autonomie en France',
    labels={'value': 'Nombre de personnes', 'variable': 'Catégorie', 'ANNEE': 'Année'}
)
fig4.show()  

# 5. Comparaison Hommes vs Femmes - Évolution
print("\n5. Création du graphique : Comparaison Hommes/Femmes")
evolution_sexe = df.groupby(['ANNEE', 'SEXE'])['vol_seniors'].sum().reset_index()
evolution_sexe['SEXE_label'] = evolution_sexe['SEXE'].map({1: 'Hommes', 2: 'Femmes'})
fig5 = px.line(
    evolution_sexe,
    x='ANNEE',
    y='vol_seniors',
    color='SEXE_label',
    title='Évolution des seniors par sexe (2021-2070)',
    labels={'vol_seniors': 'Nombre de seniors', 'ANNEE': 'Année', 'SEXE_label': 'Sexe'}
)
fig5.show()  
print("✅ Graphique 5 créé")

# 6. Corrélation : Seniors vs Perte d'autonomie (2050)
print("\n6. Création du graphique : Corrélation seniors/perte autonomie")
corr_2050 = df[df['ANNEE'] == 2050].groupby('DEP')[['vol_seniors', 'vol_seniors_perte_autonomie']].sum().reset_index()
fig6 = px.scatter(
    corr_2050,
    x='vol_seniors',
    y='vol_seniors_perte_autonomie',
    hover_name='DEP',
    title='Corrélation : Nombre de seniors vs Seniors en perte d\'autonomie (2050)',
    labels={'vol_seniors': 'Nombre total de seniors', 'vol_seniors_perte_autonomie': 'Seniors en perte d\'autonomie'}
)
fig6.show()  
print("✅ Graphique 6 créé")


# ============================================================================
# BONUS : ANALYSES AVANCÉES
# ============================================================================

print("\n" + "=" * 80)
print("BONUS : ANALYSES AVANCÉES")
print("=" * 80)

# 1. Calcul du taux de perte d'autonomie par département en 2040
print("\n1. Taux de perte d'autonomie par département (2040)")
df_2040 = df[df['ANNEE'] == 2040].groupby('DEP')[['vol_seniors', 'vol_seniors_perte_autonomie']].sum()
df_2040['taux_pa'] = (df_2040['vol_seniors_perte_autonomie'] / df_2040['vol_seniors'] * 100)
print("Top 5 des départements avec le taux de PA le plus élevé :")
print(df_2040['taux_pa'].sort_values(ascending=False).head(5))

# 2. Évolution du taux de seniors de 85+ ans
print("\n2. Évolution de la proportion de 85+ ans")
prop_85 = df[df['TRAGE'] == '85+'].groupby('ANNEE')['vol_seniors'].sum()
total_seniors = df.groupby('ANNEE')['vol_seniors'].sum()
taux_85 = (prop_85 / total_seniors * 100)
print(f"2021 : {taux_85[2021]:.2f}%")
print(f"2050 : {taux_85[2050]:.2f}%")
print(f"2070 : {taux_85[2070]:.2f}%")

# 3. Projection : Combien de seniors en perte d'autonomie en plus entre 2021 et 2050 ?
print("\n3. Augmentation des seniors en perte d'autonomie (2021-2050)")
pa_2021 = df[df['ANNEE'] == 2021]['vol_seniors_perte_autonomie'].sum()
pa_2050 = df[df['ANNEE'] == 2050]['vol_seniors_perte_autonomie'].sum()
augmentation = pa_2050 - pa_2021
pct_augmentation = (augmentation / pa_2021 * 100)
print(f"2021 : {pa_2021:,.0f} personnes")
print(f"2050 : {pa_2050:,.0f} personnes")
print(f"Augmentation : +{augmentation:,.0f} personnes (+{pct_augmentation:.1f}%)")


print("\n" + "=" * 80)
print("✅ PROJET TERMINÉ !")
print("=" * 80)