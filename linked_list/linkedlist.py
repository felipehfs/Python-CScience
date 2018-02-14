# Uma simples lista encadeada

class Node:
	""" Node class representa o menor atomo da lista"""
	def __init__(self, node=None):
		self.head = node
		self.next = None

	def set_next(self, node):
		self.next = node

	def set_value(self, value):
		self.head = value

	def get_value(self):
		return self.head
	
	def get_next(self):
		return self.next

class List(object):
	""" A Classe List implementa a lista encadeada """
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def add(self, v):
		new_node = Node(v)
		# Se a cauda existir
		if self.tail:
			self.tail.set_next(new_node)
			self.tail = new_node
		else:
			self.tail = new_node
			self.head = new_node
		self.size += 1
		return True

	def remove(self, d):
		""" Remove algum elemento se estiver na lista"""
		previous = None
		current = self.head
		# Percorre a lista em busca do elemento
		while current:
			if current.get_value() == d:
				if previous:
					previous.set_next(current.get_next())
				else:
					self.head = current.get_next()
				self.size -= 1
				return True

			previous = current
			current = current.get_next()

	def to_list(self):
		""" Retorna um generator com todos os valores """
		current = self.head
		while current:
			yield current.get_value()
			current = current.get_next()
