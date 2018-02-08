class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
   
    def travesing_inorder(self):
        if self.left:
            self.left.travesing_inorder()

        print(self.value)

        if self.right:
            self.right.travesing_inorder()
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
    def display(self):
        if self.root:
            self.root.travesing_inorder()
        else:
            print("Não existem elementos")

tree = Tree()
tree.insert(32)
tree.insert(16)
tree.insert(8)
tree.display()

