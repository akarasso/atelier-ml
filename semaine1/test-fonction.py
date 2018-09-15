#Fonctions

# Ecrivez une fonction qui prend comme arguments une liste 'lst' et un entier 'n'
# et retourne le résultat de n concaténations de 'lst'
# avec elle-même (ex: lst=[1,2,3], n=2 --> [1,2,3,1,2,3])
def lst_concat_n(lst, n):
	for x in range(1, n):
		lst += lst

testlst = [1, 2, 3]
print("List de depart	: " + str(testlst))
lst_concat_n(testlst, 2)
print("Concat(2)	: " + str(testlst))

# Vous voulez rendre le paramètre 'n' optionnel
# et fixer sa valeur à 2 par défaut. Comment faites-vous?
def lst_concat_n(lst, n = 2):
	for x in range(1, n):
		lst += lst
testlst = [1, 2, 3]
print("List de depart	: " + str(testlst))
lst_concat_n(testlst)
print("Concat()	: " + str(testlst))
