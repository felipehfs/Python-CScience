# Quick sort algorithm

def quick_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0] # Seleciona o pivo 
        # Realiza o fatiamento do array
        menores = [x for x in lista[1:] if x <= pivo] 
        maiores = [y for y in lista[1:] if y > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

assert quick_sort([9, 4,2]) == [2, 4, 9] 
