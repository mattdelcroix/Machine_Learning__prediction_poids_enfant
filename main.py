import pandas as pd
import numpy as np

# Chargement du dataset comprenant les colonnes age, taille et poids.
df = pd.read_csv("dataSet/data.csv")

# les variables prédictives
X = df[['age', 'taille']]

# la variable cible, le poids
y = df.poids

# on choisit le modèle de régression linéaire de scikit-learn.
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
from sklearn.linear_model import LinearRegression
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
# poids estimé = a * sexe + b * age + du bruit
# Les coefficients a et b sont donnés par reg.coef : [a, b]
print(f" reg coef = {reg.coef_}")
print(f" poids = {np.round(reg.coef_[0],  2)} * sexe + {np.round(reg.coef_[1],  2)} * age  + du bruit")