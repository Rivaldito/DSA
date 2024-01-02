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
        self.head   = new_node
        self.tail   = new_nod
        self.length = 1
    
