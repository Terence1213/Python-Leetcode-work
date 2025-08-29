
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        current_pointer = head.next
        head.next = None
        previous_pointer = head

        while current_pointer != None:
            next_pointer = current_pointer.next # We set the next pointer so that we don't lose it after setting the current pointer to the previous node.
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer # After using the previous node to set the current node's pointer accortdingly, we now set the new previous pointer to the current pointer for the next iteration.
            current_pointer = next_pointer
        
        # now if we've reached the point where current_pointer is None, then the previous_pointer should be holding the head node.
        return previous_pointer