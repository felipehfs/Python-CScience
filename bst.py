# Árvore binária de busca

class Node:
	""" Classe que representa o nó da árvore"""
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
		# Se o valor já existir
        if self.value == data:
            return False
		# Caso o valor seja menor que o nó atual
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return True

