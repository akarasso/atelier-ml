#Opérations sur matrices avec numpy
# https://docs.scipy.org/doc/numpy-1.13.0/reference/

import numpy
import time

# Transformer les listes A et B en tableaux numpy a et b
A = [3,6,9]
B = [12,15,18]
print("A : " + str(A))
print("B : " + str(B))
a = numpy.array(A)
b = numpy.array(B)

# Concaténez-les pour former un tableau c (a, b --> c)
# array([[1, 2],
#	[3, 4],
#	[5, 6]])
# >>> np.concatenate((a, b.T), axis=1)
#	array([[1, 2, 5],
#	[3, 4, 6]])

c = numpy.concatenate((a,b))
print("c = Concatenate a and b")
print(c)

# Divisez tous les éléments de c par 3 (sans utiliser de boucle)
c = numpy.divide(c, 3)
print("Divide C by 3")
print(c)

M = numpy.random.randint(10, size=(10,10))
N = numpy.random.randint(10, size=(10,10))
print("Matrice M")
print(M)
print("Matrice N")
print(N)

# Aditionnez les deux matrices
print("Result M + N:")
print(numpy.add(M, N))

# Calculez le produit matriciel de M et N.
# Vérifiez votre opération en calculant les premières cellules à la main
print("Result M * N:")
start_time = time.time()
print(numpy.multiply(M, N))
print("--- %s seconds ---" % (time.time() - start_time))

# Bonus: Écrivez vous-mêmes une fonction de produit matriciel, avec des boucles imbriquées
def mat_mult(mat1, mat2):
	new_mat = numpy.zeros(mat1.shape)
	for l in range(0, mat1.shape[0]):
		for x in range(0, mat1.shape[1]):
			new_mat[l][x] = mat1[l][x] * mat2[l][x]
	return new_mat

print("My mult:")
start_time = time.time()
print(mat_mult(M, N))
print("--- %s seconds ---" % (time.time() - start_time))
