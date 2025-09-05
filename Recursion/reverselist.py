class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
            
        new_head = self.reverseList(head.next)
        
        head.next.next = head # This makes it so that if 2 was pointing towards 3, it gets the next (3), and makes the next of 3 point to 2
        head.next = None # This makes it so 2 doesn't point to 3 anymore.
        # This head.next also ensures that the first element in the list, considering that now its going to be the tail after reversing, is going to be pointing to nothing.
        
        return new_head # The way that this part works is that once you get to the end of the linked list
        # meaning that you return head, that is returning the new head, so for the rest of the recursions you will keep returning the same new_head

class RevisionSolution:
    def rerverseList(self, node: ListNode) -> ListNode:
        if node == None or node.next == None:
            return node
    
        new_head = self.reverseList(node.next)

        node.next.next = node
        node.next = None

        return new_head
        
