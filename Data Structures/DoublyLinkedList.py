class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def printDoublyList(self):
        cur = self.head
        while cur:
            print("Data: "+cur.data)
            cur = cur.next

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def addAfter(self, key, data):

        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                afterNode = cur.next
                cur.next = new_node
                new_node.next = afterNode
                new_node.prev = cur
                afterNode.prev = new_node
                return
            cur = cur.next

    def addBefore(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next

    def deleteNode(self, key):
        """ 
        ? We have 4 case for deletion a node
        * Only node
        * Head node
        * Intersect
        * Last Node
        """

        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    afterNode = cur.next
                    cur.next = None
                    afterNode.prev = None
                    cur = None
                    self.head = afterNode
                    return
            elif cur.data == key:
                if cur.next:
                    afterNode = cur.next
                    prev = cur.prev
                    prev.next = afterNode
                    afterNode.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
                cur = cur.next

    def reverseDoubly(self, key):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def dublicateRemove(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                afterNode = cur.next
                self.deleteNode(cur)
                cur = afterNode

    def pairsWithSum(self, value):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == value:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs
