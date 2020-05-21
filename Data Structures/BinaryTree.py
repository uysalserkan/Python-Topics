class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preOrderTraverse(self, start, traversal):
        if start:
            traversal += (str(start.data) + "->")
            traversal = self.preOrderTraverse(start.left, traversal)
            traversal = self.preOrderTraverse(start.right, traversal)
        return traversal

    def inOrderTraverse(self, start, traversal):
        if start:
            traversal = self.inOrderTraverse(start.left, traversal)
            traversal += (str(start.data) + "->")
            traversal = self.inOrderTraverse(start.right, traversal)
        return traversal

    def postOrderTraverse(self, start, traversal):
        if start:
            traversal = self.postOrderTraverse(start.left, traversal)
            traversal = self.postOrderTraverse(start.right, traversal)
            traversal += (str(start.data) + "->")
        return traversal

    def printBinaryTree(self, traversaType):
        if traversaType == "preorder":
            return self.preOrderTraverse(self.root, "")
        elif traversaType == "inorder":
            return self.inOrderTraverse(self.root, "")
        elif traversaType == "postorder":
            return self.postOrderTraverse(self.root, "")
        elif traversaType == "levelorder":
            return self.levelOrderTraverse(self.root)
        elif traversaType == "reverselevelorder":
            return self.reverseLevelOrderTraverse(self.root)
        else:
            raise NameError

    def levelOrderTraverse(self, start):
        from Queue import Queue
        if start is None:
            return

        myQu = Queue()
        myQu.enqueue(start)

        traversal = ""
        while len(myQu) > 0:
            traversal += str(myQu.peek()) + "->"
            deqNode = myQu.dequeue()

            if deqNode.left:
                myQu.enqueue(deqNode.left)
            if deqNode.right:
                myQu.enqueue(deqNode.right)

        return traversal

    def reverseLevelOrderTraverse(self, start):
        if start is None:
            return

        from Queue import Queue
        from Stack import CustomStack

        myQu = Queue()
        mySt = CustomStack()

        myQu.enqueue(start)

        traversal = ""
        while len(myQu) > 0:
            deqNode = myQu.dequeue()
            mySt.push(deqNode)

            if deqNode.right:
                myQu.enqueue(deqNode.right)
            if deqNode.left:
                myQu.enqueue(deqNode.left)

        while len(mySt) > 0:
            StaPopNode = mySt.pop()
            traversal += str(StaPopNode.data) + "->"

        return traversal

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
