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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
    def find_middle_node(self):
        
        slow = self.head
        fast = self.head.next

        if slow == None or fast == None:
            return None

        while fast is not None:

            slow = slow.next
            fast = fast.next
            if fast == None:
                return slow
            else:
                fast = fast.next
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head

        if self.head == None:
            return False
        while (slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False

    def partition_list(self, x):

        if self.head == None:
            return None
        
        temp = self.head

        while temp:
            if temp.value < x

            temp = temp.next
            pass

        

        pass    





def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow