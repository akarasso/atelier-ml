#Dictionnaires et tuples

# Creez un tuple qui associe votre login a votre âge
tupleInfo = (['hoax', 28])
print("Mon login:" + tupleInfo[0])
print("Mon age:" + str(tupleInfo[1]))

# Initialisez un dictionnaire a deux entrees qui associe le login de chacun de vos voisins a leur âge
dict = {
	'login1': 24,
	'login2':26
}

# Recuperez l'âge de l'un d'entre eux a partir du dictionnaire
print(dict['login1'])

# Ajoutez une entree avec votre propre login
dict[tupleInfo[0]] = tupleInfo[1]
print("Hoax dictionary content:" + str(dict['hoax']))
