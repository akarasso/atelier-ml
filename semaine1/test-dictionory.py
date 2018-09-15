#Dictionnaires et tuples

# Créez un tuple qui associe votre login à votre âge
tupleInfo = (['hoax', 28])
print("Mon login:" + tupleInfo[0])
print("Mon age:" + str(tupleInfo[1]))

# Initialisez un dictionnaire à deux entrées qui associe le login de chacun de vos voisins à leur âge
dict = {
	'login1': 24,
	'login2':26
}

# Récupérez l'âge de l'un d'entre eux à partir du dictionnaire
print(dict['login1'])

# Ajoutez une entrée avec votre propre login
dict[tupleInfo[0]] = tupleInfo[1]
print("Hoax dictionary content:" + str(dict['hoax']))
