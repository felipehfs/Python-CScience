# Função que encontra o maior valor recursivamente
def maximum_array(array):

	if len(array) == 0:
		return 

	# caso base, caso o tamanho seja igual a um retorna o primeiro elemento
	if len(array) == 1:
		return array[0]
	
	# encontra o menor elemento das duas porçoes
	lmax = maximum_array(array[:len(array) / 2])
	rmax = maximum_array(array[len(array) / 2:])

	# Retorna o maior
	if lmax >= rmax:
		return lmax
	else:
		return rmax

A = [7, 9, 1, 2, 4, 6, 3]
B = [9, 5, 6,2, 7, 3, 1, 200]

print(maximum_array(A))
print(maximum_array(B))
