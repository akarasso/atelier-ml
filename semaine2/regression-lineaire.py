# import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données du fichier
data = pd.read_csv("database/ex1data1.csv")
data.plot()

# Visualiser les données
# plt.show()

# Découpez vos données en deux vecteurs X et y et transformerz-les en array numpy
X = np.array(data['population'])
Y = np.array(data['profit'])

#Calcul d'une première prédictio

# Initialisez theta en un vecteur de deux valeurs à zéro
theta = np.zeros(2)

# Écrivez une fonction predict qui prend en argument une population (x)
# ainsi que les parametres theta et prédit le profit (y) associé
# Donc X('population') est un predicteur
# Y (a savoir le profit dans l'exemple est une variable explique)
# pour savoir si un modele est utilisable par la regression simple,
# on peut calculer son coefficient de correlation
# yi = a + b * xi + epsi
# yi => la variable explique
# a => const qui est l'augementation de la variable yi en l'absence de xi
# b => coeff d'augmentation de la variable yi quand xi augmente de 1
# xi => valeur de la variable predicteur
# epsi => residu aleatoire, les epsi de deux xi different n'ont aucun lien!
print("Estimation des parametre : ")
print("Variance X:" + str(np.var(X)))
print("Variance Y:" + str(np.var(Y)))
print("Moyenne X:" + str(np.average(X)))
print("Moyenne Y:" + str(np.average(Y)))
covxy = np.cov(X, Y, None, True)[0][1]
b = (covxy) / np.var(X);
print("On en deduit que b vaut : " + str(b))
a = np.average(Y) - np.average(X) * b
print("La variable alpha vaut alors : " + str(a))
print("Determination de la variance de b")
print("V[b] = Variance du residu epsilon / Nombre d'entre dans la database * Variance X")
print("Plus la variance de X est grande et plus la variance de b diminue,")
print("donc l'intervalle de confiance est plus grand.")
print("V[a] = (Variance du residu epsilon / Nombre d'entre dans la database) \
 * ( 1 + (Moyenne X) * (Moyenne X) / Variance X)")
print("Si ma moyenne est trop grande, j'aurais donc des difficultees a savoir \
ce qu'il se passe lorsque X est a 0");
theta[0] = b
theta[1] = a
def predict(X, theta):
    y = theta[0] * X + theta[1]
    return (y)
value = 500
print("Prediction sur une population de " + str(value) + " : " + str(predict(value, theta)))
