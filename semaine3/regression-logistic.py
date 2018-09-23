import numpy as np

"""
	Regression logistic pour quel usage?
	Apprentissate et delais de prediction tres rapide donc
	plus facile a utiliser sur de gros volume de donnees
	Modeles court et large utilisent beaucoup de memoire RAM
	La regression logistique suit une courbe sigmoide tq:
	y = 1 / (1 + exp(-w^T * (x + b)))
	Une courbe sigmoide donne une valeur comprise entre 0 et 1
	La formule de la perte
	-y * log(y') - (1 - y) * log(1 - y')
"""

# DEFINE
nparam = 2

"""
	Fonction de generation de dataset aleatoire pour differents test...
	L'exemple propose est l'etude de l'apparition d'une maladie
	selon deux parametres. Le taux de globules blancs et le taux de
	globule rouge
"""
def dataset_gen():
	"""
		gen random dataset
	"""
	nrow = 5
	mat1 = np.random.randn(nrow, 2) + np.array([-2,-2])
	mat2 = np.random.randn(nrow, 2) + np.array([2,2])
	features = np.vstack([mat1, mat2])
	targets = np.concatenate((np.zeros(nrow), np.zeros(nrow) + 1))
	return features, targets


"""
	Permet de d'initializer les variables theta0, theta1,.. thetaN
"""
def init_variables():
	return np.random.normal(size=nparam), 0

"""
	Calculation de la preactivation
"""
def pre_activation(features, theta, bias):
	return np.dot(features, theta) + bias

"""
	Calculation de l'activation
	Qu'est ce que l'activation?
	C'est le poucentage de certitude d'une affirmation futur
	https://developers.google.com/machine-learning/crash-course/logistic-regression/calculating-a-probability?hl=fr
"""
def activation(pre_act):
	return 1 / (1 + np.exp(-pre_act))

features, targets = dataset_gen()
theta, epsi = init_variables()
pre_act = pre_activation(features, theta, epsi)
print("Pre activation")
print(pre_act)
print("\nActivation")
act = activation(pre_act)
print(act)
