# Função efetua a soma recursiva dos elementos do array
def soma(lista):
	""" Soma recursiva dos elementos da lista"""
	if len(lista) == 0:
		return 0
	else:
		return lista[0] + soma(lista[1:])
 
print(soma([4, 6, 5]))
