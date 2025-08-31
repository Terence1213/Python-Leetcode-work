class ListNode():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if self.head == None or index < 0 or index >= self.size:
            return -1 # Linked list is empty, or index is out of bounds.
        
        # If we want to get an item from a doubly linked list, we traverse through the list as we would do with a normal linked list.
        current = self.head

        for _ in range(0, index):
            current = current.next
        
        return current.val
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head == None:
            self.head = new_node
        else:
            # If the list wasn't previously empty, we have to update the pointers of the head.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next != None:
                last_node = last_node.next
            
            new_node.prev = last_node
            last_node.next = new_node

        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)

        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head

            for _ in range(0, index):
                current = current.next

            # We have to update the previous pointer's next pointer to the new node, 
            prev = current.prev 
            current.prev.next = new_node
            current.prev = new_node
            new_node.next = current
            new_node.prev = prev # Had to make a temporary variable since we're losing the prev node when we're setting current.prev to the new node.

            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return

        if index >= self.size or index < 0:
            return
        
        if index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            current = self.head

            for _ in range(0, index):
                current = current.next

            if index == self.size - 1:
                current.prev.next = current.next # current.next is going to be None. (making the previous node the new tail node)
            else: 
                current.prev.next = current.next
                current.next.prev = current.prev
        
        self.size -= 1
