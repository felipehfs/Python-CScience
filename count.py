def count(lista):
    if lista:
        return 1 + count(lista[1:])
    return 0

print(count([1, 2, 3, 4]))
