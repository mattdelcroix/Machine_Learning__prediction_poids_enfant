# Prédiction du poids d'un enfant / Child Weight Prediction

## Français

### Présentation

Ce projet illustre l'utilisation d'une régression linéaire avec Python, pandas,
NumPy et scikit-learn pour estimer le poids d'un enfant à partir de son âge et
de sa taille. Le script compare également un modèle utilisant ces deux variables
à un modèle qui inclut le sexe, encodé numériquement dans le jeu de données.

Le fichier `dataSet/data.csv` doit contenir les colonnes `sexe`, `age`,
`taille` et `poids`. L'âge est exprimé en mois, la taille en centimètres et le
poids en kilogrammes.

### Exécution

Installez les dépendances `pandas`, `numpy` et `scikit-learn`, puis exécutez
depuis la racine du projet :

```bash
python main.py
```

Le script affiche les coefficients des modèles, une prédiction d'exemple et,
pour le premier modèle, le R² ainsi que les erreurs MSE, MAE et MAPE.

### Étapes générales d'entraînement d'un modèle

Entraîner un modèle consiste généralement à enchaîner les étapes suivantes :

1. **Charger les données** depuis un fichier ou une autre source.
2. **Transformer ou améliorer les données** : nettoyer les valeurs manquantes,
   corriger les formats et préparer les variables nécessaires au modèle.
3. **Scinder les données** en ensembles d'entraînement et de test, ou en
   ensembles d'entraînement, de validation et de test. L'entraînement sert à
   ajuster le modèle ; la validation aide à choisir une configuration ; le test
   fournit une évaluation finale sur des données non utilisées pour ces choix.
4. **Entraîner plusieurs configurations**, lorsque le modèle possède des
   paramètres à régler, en ajustant chaque version sur les données
   d'entraînement.
5. **Calculer et comparer les scores** de chaque version, idéalement sur les
   données de validation, puis évaluer la version retenue sur le jeu de test.

### Ce que fait actuellement le script

Le script charge le CSV, entraîne deux régressions linéaires et produit une
prédiction pour un profil d'exemple. Il n'effectue pas encore de séparation
entraînement/test ni de recherche de configurations : les scores et les
métriques du premier modèle sont calculés sur les mêmes données qui ont servi à
l'entraîner. Ils décrivent donc son ajustement au jeu de données, mais ne
mesurent pas de façon indépendante ses performances sur de nouvelles données.

Les principales métriques affichées sont :

- **R²** : part de la variation du poids expliquée par le modèle ; plus proche
  de 1 indique généralement un meilleur ajustement.
- **MSE** : moyenne des erreurs au carré, en kg² ; les grandes erreurs sont
  davantage pénalisées. Une valeur plus faible est préférable.
- **MAE** : moyenne des écarts absolus entre poids prédit et réel, en kg.
- **MAPE** : moyenne des erreurs absolues relatives, affichée en pourcentage.
  Une valeur de 9 % correspond à environ 9 % d'erreur absolue moyenne relative.

Cette démonstration ne remplace pas une évaluation médicale ou une estimation
clinique.

## English

### Overview

This project demonstrates linear regression with Python, pandas, NumPy, and
scikit-learn to estimate a child's weight from age and height. The script also
compares those two predictors with a model that includes sex, which is encoded
numerically in the dataset.

The `dataSet/data.csv` file must contain the columns `sexe`, `age`, `taille`,
and `poids`. Age is measured in months, height in centimeters, and weight in
kilograms.

### Run

Install the `pandas`, `numpy`, and `scikit-learn` dependencies, then run this
command from the project root:

```bash
python main.py
```

The script prints the model coefficients, an example prediction, and, for the
first model, R² and the MSE, MAE, and MAPE metrics.

### General model-training workflow

Training a model generally involves the following steps:

1. **Load the data** from a file or another source.
2. **Transform or improve the data**: clean missing values, fix formats, and
   prepare the features required by the model.
3. **Split the data** into training and test sets, or into training,
   validation, and test sets. Training data fits the model; validation data
   helps select a configuration; test data provides a final evaluation on data
   not used for those choices.
4. **Train multiple configurations**, when the model has parameters to tune,
   fitting each version on the training data.
5. **Calculate and compare scores** for each version, ideally on validation
   data, then evaluate the selected version on the test set.

### What the script currently does

The script loads the CSV, trains two linear regression models, and predicts the
weight for an example profile. It does not yet split the data into training and
test sets or search across configurations: the first model's scores and metrics
are calculated on the same data used to train it. They describe its fit to the
dataset, but do not independently measure performance on new data.

The main reported metrics are:

- **R²**: the proportion of weight variation explained by the model; a value
  closer to 1 generally indicates a better fit.
- **MSE**: the mean squared error, in kg²; larger errors are penalized more.
  Lower values are preferable.
- **MAE**: the mean absolute difference between predicted and actual weight, in
  kilograms.
- **MAPE**: the mean absolute percentage error. A value of 9% means the average
  absolute relative error is about 9%.

This demonstration is not a substitute for medical evaluation or clinical
estimation.
