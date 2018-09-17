#Boucles

# Avec une boucle 'while', imprimez chaque element de la liste C jusqu'a l'element nul
def print_lst(lst):
	i = 0
	while i < len(lst):
		print(lst[i])
		i += 1
testlst = [1, 2, 3, 4]
print("Affichage de la liste : " + str(testlst))
print_lst(testlst)

# Calculez, avec une boucle 'for', le nombre d'entiers pairs presents dans la liste A
def get_nb_even(lst):
	even = 0
	for x in range(0, len(lst)):
		if lst[x] % 2 == 0:
			even += 1
	return (even)

testlst = [1, 2, 3, 4]
print("List ref : " + str(testlst))
print("Nombre de chiffre pair : " + str(get_nb_even(testlst)))

# Reecrivez l'expression suivante avec une boucle 'for' sur plusieurs lignes
# C = [element for element in A if element %2 == 0]
A = [1, 2, 3, 4]
C = []
for element in A:
	if element % 2 == 0:
		C.append(element)
print("List ref : " + str(A))
print("List res : " + str(C))
