
## 🎯 Objectif du projet

Analyse approfondie des **projections démographiques des seniors** et de la **perte d'autonomie** en France sur 50 ans (2021-2070), basée sur les données officielles de l'**INSEE**.

Ce projet explore l'évolution de la population senior, les impacts du vieillissement, et les besoins futurs en termes de prise en charge de la dépendance.

---

## 📁 Dataset

**Source** : [data.gouv.fr - Projections de population seniors](https://www.data.gouv.fr/api/1/datasets/r/2f136424-d448-4403-adda-6cac5b86978a)


**Caractéristiques** :
- 📊 **30 300 lignes** de données
- 📅 **50 années** de projections (2021-2070)
- 🗺️ **101 départements** français
- 👥 **3 tranches d'âge** : 60-74 ans, 75-84 ans, 85+
- ⚧️ **2 sexes** : Hommes et Femmes

**Colonnes principales** :
- `DEP` : Code département
- `ANNEE` : Année de projection
- `SEXE` : 1 = Homme, 2 = Femme
- `TRAGE` : Tranche d'âge (60-74, 75-84, 85+)
- `vol_seniors` : Volume total de seniors
- `vol_seniors_perte_autonomie` : Seniors en perte d'autonomie
- `vol_seniors_perte_autonomie_severe` : Seniors en perte d'autonomie sévère
- `esp_vie_60_ans` / `esp_vie_75_ans` : Espérance de vie à 60 et 75 ans
- Et d'autres indicateurs sur les ménages et institutions


## 🚀 Installation et utilisation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/ShayyNwE/Python_DATA
cd projet-seniors-france
```

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv

# Activer l'environnement
# Sur Windows :
venv\Scripts\activate

# Sur Mac/Linux :
source venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Télécharger le dataset

Télécharge le fichier CSV

### 5️⃣ Lancer l'analyse

```bash
python main.py
```

Les graphiques interactifs s'ouvriront automatiquement dans ton navigateur ! 📈

---
