class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head 
        
        return new_head
    
class SolutionTwo:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If we reach a point where the node doesn't have a next pointer node, or is empty within itself (None) then there's nothing to swap with, so we just return this current node and end the recursive loop.
        if head == None or head.next == None:
            return head
        
        new_head = head.next
        head.next = self.swapPairs(new_head.next) # Makes it so that the old head's next (which is now going to be the node after the next head), points to the next node, which was the previous next pointer of the new_head.
        new_head.next = head

        return new_head

class SolutionPractice:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head