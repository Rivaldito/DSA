from linkedList import LinkedList

if __name__ == "__main__":

    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.print_list()

    print("[]")
    my_linked_list.prepend(4)

    my_linked_list.print_list()

    print("[1]")
    print(my_linked_list.get(1))

    print("[2]")

    print(my_linked_list.pop_first())
    my_linked_list.print_list()

    #print(my_linked_list.get(1))