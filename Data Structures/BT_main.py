from BinaryTree import *

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printBinaryTree("inorder"))
print(tree.printBinaryTree("preorder"))
print(tree.printBinaryTree("postorder"))

print("Level order: " + tree.printBinaryTree("levelorder"))
print("Reverse Level order: " + tree.printBinaryTree("reverselevelorder"))

print("Height of the binary tree: "+str(tree.height(tree.root)))
print("The Size of the Tree is: " + str(tree.size(tree.root)))
