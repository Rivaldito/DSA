from linkedList import LinkedList

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    my_linked_list.append(6)
    print( my_linked_list.find_middle_node().value )