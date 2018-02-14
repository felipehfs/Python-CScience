# Algoritmo - Binary Search
# 2018 -Felipe Henrique

def busca_binaria(lista, busca):
	""" 
		Busca binária tem uma complexidade de algoritmo O(log n)
	"""
	inicio = 0
	fim = len(lista)
	while inicio <= fim:
		meio = (inicio + fim) // 2
		if busca == lista[meio]:
			return lista[meio]
		else:
			if busca > lista[meio]:
				inicio = meio + 1
			elif busca < lista[meio]:
				fim = meio - 1
	return None

