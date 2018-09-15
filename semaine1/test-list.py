#Manipulation de listes

# Créez une liste A contenant les entiers suivants: 1, 3, 2, 7, 4, 10, 46
a = [1, 3, 2, 7, 4, 10, 46]

# Affichez les 3 premiers éléments de la liste A - en une ligne de code
# print(str(a[0]) + " " + str(a[1]) + " " + str(a[2]))
print(str(a)[1:8])

# Créez une liste B qui contient seulement les 3e, 4e et 5e éléments de A .
# Votre ligne de code ne devrait contenir que 8 caractères (sans compter les espaces)
b = a[3:6]
print("Apres un slice de 'a', 'b' contient : " + str(b))

# Concaténez les listes A et B pour former la liste C
c = a + b
print("La liste 'c' contient : " + str(c))

# Ajoutez le nombre 5 à la liste A
a.append(5)
print("Apres un append(5), 'a' contient : " + str(a))

# Ajoutez un élément nul à la liste C
# None equivalent de null en python...
c.append(None)
print("Apres un append(None), 'c' contient : " + str(c))
