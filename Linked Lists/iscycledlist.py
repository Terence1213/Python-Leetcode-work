from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Edge case: empty list or single node with no cycle
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        # Fast pointer is moving twice with each iteration, while the slow pointer is just moving one. If the list is cycling, then evenutually, the fast pointer must be equal to the slow pointer. 
        # To better visualise, the slow pointer is always moving ONE value, so at some point considering that the fast is moving 2 values it must end up one one of the ONE values which the slow pointer is
        # cycling through.
        # Move pointers until they meet or fast reaches the end
        while slow != fast:
            # If fast reaches the end -> no cycle
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True