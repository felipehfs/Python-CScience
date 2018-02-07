# Algoritmo: selection sort

def busca_menor(lista):
	""" Busca menor elemento e retorna seu índice """	
	menor = lista[0]
	menor_indice = 0
	for item in range(1, len(lista)):
		if lista[item] < menor:
			menor = lista[item]
			menor_indice = item
	return menor_indice

def selection_sort(lista):
	ordenados = []
	for item in range(len(lista)):
		menor = busca_menor(lista)
		ordenados.append(lista.pop(menor))
	return ordenados

print(selection_sort([5, 4, 7, 9, 4]))
