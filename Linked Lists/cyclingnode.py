from typing import List
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find start of cycle
                pointer1 = head
                pointer2 = slow

                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next

                return pointer1  # start of cycle

        return None  # no cycle

class MySolution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Firs things first, we have to make sure that the linked list has at least 2 elements, for it to be able to actually cycle
        if head == None or head.next == None:
            return None

        # Now the next step is checking whether the linked list 
        fast = head
        slow = head

        # We're going to keep on looping as long as the fast pointer isn't None itself, or until we find a node which doens't have a nexty pointer (which shouldn't happen in a cycled linked list)
        while fast != None and fast.next != None:
            fast.next = fast.next.next
            slow.next = slow.next

            # Consiering that the fast pointer is going through the linekd list 2 times faster than the slow pointer, if thaey end up being equal it must be because of a cycle occuring.
            if fast.next == slow.next:
                # Now that we've found the cycle, we must get the starting point of the cycle
                pointer1 = slow
                pointer2 = head

                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next

                return pointer1

        return None # In this case, there was no cycle, indicated by the fact that fast, or fast.next ended up being None