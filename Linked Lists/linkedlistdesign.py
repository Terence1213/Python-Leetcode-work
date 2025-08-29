

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Every node we add must have a unique ID.
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        
        if index < 0 or index >= self.size:
            return -1
        
        current_node = self.head
        for _ in range(0, index):
            current_node = current_node.next

        return current_node.value


    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.size += 1
            return

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        current_node = self.head

        for i in range(0, index):
            if i == index - 1:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                current_node = current_node.next
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return # invalid index
        
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for i in range(0, index - 1):
                current_node = current_node.next
            
            current_node.next = current_node.next.next

        self.size -= 1