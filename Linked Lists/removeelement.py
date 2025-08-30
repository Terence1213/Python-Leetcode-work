class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # If there are for example 3 nodes in a row at the start of the list which have the mathcing value, all of these nodes are removed and the head node is set to the next node without the matching value.
        while head.val == val:
            head = head.next
        
        slow = head
        fast = head.next

        while fast != None:
            if fast.val == val:
                slow.next = slow.next.next # If the fast is currently at the last element , then the slow will just simply become the next tail node
            
            # slow = slow.next
            fast = fast.next

            # This makes sure that if we find a matching value right after the previously matching value, we don't just move the fast pointer over it and forget about it. In that case, we would 
            # NOT update the slow pointer, and we would set the slow pointer to point after the node to delete accordingly. Then since the fast pointer is incremented and we find a node which doesn't
            # have the matching value, we increment the fast by an extra value and then increment the slow pointer.
            # in the case that we're deleting the last element in the list, then there's no value to check for the fast value, so we just continue to the next iteration of the loop (where we WONT loop)
            if fast != None and fast.val != val:
                fast = fast.next
            else:
                continue

            slow = slow.next

        return head
    
class SolutionTwo:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        current = head 
        prev = dummy

        while current != None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = prev.next # We only update the previous pointer if there isn't a deletion. in the case of a deletion, we're going to change the next pointer which the previous pointer will move to, but we won't actually move the pointer, the current pointer will at this time be moving so that 
                # in the next iteration, if there isn't a deletion, the previous pointer will jump to a position before the current and not on the same position as the current
            current = current.next
        
        return dummy.next
