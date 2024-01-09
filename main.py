from linkedList import LinkedList
from linkedList import find_kth_from_end

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)


    k = 2
    result = find_kth_from_end(my_linked_list, k)

    print(result.value)  # Output: 4