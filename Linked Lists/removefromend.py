class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Guided with chatgpt
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # We create a dummy because of the possibility that the value of n indicates that we must delete from the head node.
        dummy = ListNode(0, head) # Note that 0 is just the placeholder value, this node won't be actually used or returned at all in the resultant list.
        slow = dummy
        fast = dummy

        # First thing we do is moving the fast pointer n + 1 steps, and then we continue by incrementing both the fast pointer and the slow pointer by 1
        # Note that the n + 1 is so that the slow pointer stops one before the value marked by n (the one we want to actually delete)
        # This is because to delete, we want to set the pointer of the node before the node to delete to the node after the node to delete
        for _ in range(n + 1):
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        # Now that we've got the right node which we need to change the next pointer of, we actually perform the change
        slow.next = slow.next.next

        return dummy.next # Note that we aren't returning the dummy itself, we're returning the node after the dummy, whether that be the original head (if it wasn't deleted) or not (if it was deleted)
    
# Done completely on my own (I just redid what i had just done, in a way of practice)
class SolutionTwo:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # update the fast pointer
        for _ in range(n + 1):
            fast = fast.next
        
        # Now we increment both the fast and the slow until the fast is None
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next