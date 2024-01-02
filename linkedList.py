class Node:
    """
    Node class

    Define every item on the linked list

    Attributes:
        value:  The item of the list in that node
        Next:   The next hope to the element to the linked list 
    """
    def __init__(self,value):
        """
        Constructore of the node
        """
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node    = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.tail = new_node 
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
        return True
