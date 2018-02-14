# Percorre a lista e devolve o seu tamanho

def count(lista):
	""" Conta o tamanho de uma lista recursivamente """    
	if lista:
        return 1 + count(lista[1:])
    return 0

print(count([1, 2, 3, 4]))
