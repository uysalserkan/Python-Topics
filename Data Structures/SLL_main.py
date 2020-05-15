from SingleLinkedList import *


def main():
    myList = LinkedList()
    myList.append("S")
    myList.append("E")
    myList.append("R")
    myList.prepend("N")
    myList.prepend("A")
    myList.prepend("K")
    customNode = Node("S")
    myList.insert_after_node(customNode, "X")
    myList.delete_Node("K")
    myList.delete_node_at_pos(2)
    myList.swap_nodes("N", "E")
    myList.printList()
    myList.recursive_reverse()
    myList.printList()
    myList.reverse()
    myList.printList()
    print("My list lenght: " + str(myList.list_len()))

    mySecondList = LinkedList()
    mySecondList.append("U")
    mySecondList.append("Y")
    mySecondList.append("S")
    mySecondList.append("A")
    mySecondList.append("L")

    myList.merge_sorted(mySecondList)
    myList.printList()  # it will be normal merge, because latters


if __name__ == "__main__":
    main()
