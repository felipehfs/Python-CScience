class Node:

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
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def add(self, v):
		new_node = Node(v)
		if self.tail:
			self.tail.set_next(new_node)
			self.tail = new_node
		else:
			self.tail = new_node
			self.head = new_node
		self.size += 1

	def remove(self, d):
		previous = None
		current = self.head
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
		current = self.head
		while current:
			yield current.get_value()
			current = current.get_next()
		
c = List()
c.add(40)
c.add(54)
c.add(32)


for item in c.to_list():
	print(item)
