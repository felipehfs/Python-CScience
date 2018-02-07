
class Node:
    """ Arvores binárias """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data > value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif self.data < value:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            self.data = data

    def contains(self, value):
        if self.data == value:
            return True
        elif self.data <= value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def preorder(self):
        if self.left:
            self.left.preorder()

        print(self.data)

        if self.right:
            self.right.preorder()

    def lookup(self):

root = Node(3)
root.insert(10)
root.insert(1)
root.preorder()