class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ MY Explanation etc. """
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def printList(self):
        cur = self.head
        while cur:
            print("Data: "+str(cur.data))
            cur = cur.next
            if cur == self.head:
                break

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def __len__(self):
        cur = self.head
        counter = 0
        while cur:
            counter += 1
            if cur == self.head:
                break
        return counter

    def split_circular_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size / 2
        counter = 0
        prev = None
        cur = self.head

        while cur and counter < mid:
            counter += 1
            prev = cur
            cur = cur.next

        prev.next = self.head

        split_circular_list = CircularLinkedList()
        while cur.next != self.head:
            split_circular_list.append(cur.data)
            cur = cur.next
        split_circular_list.append(cur.data)

        self.printList()
        print("\n")
        split_circular_list.printList()

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:
            counter = 1
            while counter != step:
                cur = cur.next
                counter += 1
            print("Killed: "+str(cur.data))
            self.remove_node(cur)
            cur = cur.next
