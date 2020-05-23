class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, root, value):
        if root.data < value:
            if root.right:
                self.insert(root.right, value)
            else:
                root.right = Node(value)

        else:
            if root.left:
                self.insert(root.left, value)
            else:
                root.left = Node(value)

    def search(self,root,value):
        if root:
            if root.data == value:
                return True
            elif root.data < value:
                return self.search(root.right,value)
            else:
                return self.search(root.left,value)
    