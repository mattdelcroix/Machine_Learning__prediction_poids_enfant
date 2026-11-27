import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

# Chargement du dataset comprenant les colonnes age, taille et poids.
df = pd.read_csv(Path(__file__).parent / "dataSet" / "data.csv")

# les variables prédictives
X = df[['age', 'taille']]

# la variable cible, le poids
y = df.poids

# on choisit le modèle de régression linéaire de scikit-learn.
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
reg = LinearRegression()

# on entraîne ce modèle sur les données avec la méthode fit
reg.fit(X, y)

# et on obtient directement un score
# Le score représente la performance du modèle sur les données du dataSet. 
# Il s'agit du coefficient de détermination R^2, qui mesure les variations de la variable cible. 
# R^2 vas de 0 (mauvaise performance) à 1 (bonne performance).
print(f"R^2 : {np.round(reg.score(X, y), 3)}")

# ainsi que les coefficients a,b,c de la régression linéaire
# Comme il s'agit d'une régression linéaire, le modèle que nosu venons d'entraîner s'exprime comme suit : 
# poids estimé = a * age + b * taille + ordonnée à l'origine
# Les coefficients a et b sont donnés par reg.coef : [a, b]
print(f" reg coef = {reg.coef_}")
print(f" poids = {np.round(reg.coef_[0], 2)} * age + {np.round(reg.coef_[1], 2)} * taille + {np.round(reg.intercept_, 2)}")

# prediction du poids pour un enfant agé de 150 mois et de taille 170 cm
prediction = reg.predict(pd.DataFrame({
    'age': [150],
    'taille': [170]
}))

print("Poids prédit :", prediction[0])

#Evaluation du modèle avec les métriques MSE, MAE et MAPE

y_pred = reg.predict(X)
# MSE : moyenne des erreurs au carré, exprimée en kg² ; les grandes erreurs sont davantage pénalisées.
# Plus le MSE est proche de 0, plus les prédictions sont proches des poids réels.
mse = mean_squared_error(y, y_pred)
print(f"MSE (erreur quadratique moyenne, en kg² ; plus bas = mieux) : {mse:.2f}")

# MAE : moyenne des écarts absolus entre poids prédit et réel, exprimée en kg.
# Ici, elle indique en moyenne de combien de kilos les prédictions s'écartent des valeurs réelles.
mae = mean_absolute_error(y, y_pred)
print(f"MAE (erreur absolue moyenne, en kg ; plus bas = mieux) : {mae:.2f} kg")

# MAPE : moyenne des erreurs absolues rapportées au poids réel, exprimée en pourcentage.
# Par exemple, 0.09 correspond à environ 9 % d'erreur moyenne ; plus bas = mieux.
mape = mean_absolute_percentage_error(y, y_pred)
print(f"MAPE (erreur absolue moyenne en pourcentage ; plus bas = mieux) : {mape:.1%}")

#Ajout d'un nouveau prédicteur : sexe
X = df[['sexe','age', 'taille']]
reg.fit(X,y)
print(f"R^2 : {np.round(reg.score(X, y), 3)}")
print(f" reg coef = {reg.coef_}")
print(
    f" poids = {np.round(reg.coef_[0], 2)} * sexe "
    f"+ {np.round(reg.coef_[1], 2)} * age "
    f"+ {np.round(reg.coef_[2], 2)} * taille "
    f"+ {np.round(reg.intercept_, 2)}"
)

# prediction du poids pour un garçon agé de 150 mois et de taille 170 cm
prediction = reg.predict(pd.DataFrame({
    'sexe': [0],
    'age': [150],
    'taille': [170]
}))

print("Poids prédit :", prediction[0])