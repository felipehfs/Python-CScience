class Node(object):
	""" Representa uma arvore binária """
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value <= self.data:
			if not self.left:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if not self.right:
				self.right = Node(value)
			else:
				self.right.insert(value)

	def pre_order(self):

		if self.left:
			self.left.pre_order()

		print(self.data)

		if self.right:
			self.right.pre_order()

	def contains(self, value):
		if value == self.data:
			return True
		elif value <= self.data:
			if not self.left:
				return False
			else:
				return self.left.contains(value)
		else:
			if not self.right:
				return False
			else:
				return self.right.contains(value)

	def find(self, value):
		if value == self.data:
			return self.data
		elif value <= self.data:
			if not self.left:
				return None
			else:
				return self.left.find(value)
		else:
			if not self.right:
				return None
			else:
				return self.right.find(value)

a = Node(30)
a.insert(3)
a.insert(6)
a.pre_order()

print(a.contains(3))
print(a.find(30))
