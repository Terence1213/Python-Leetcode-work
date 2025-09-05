class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Do the rotate procedure for k amount of times

        if head == None or head.next == None: # There is no way of us rotating if the list is empty or only has one element.
            return
        
        for _ in range(0, k):
            
            slow = head
            fast = head.next

            while fast.next != None:
                slow = slow.next
                fast = fast.next
            
            slow.next = None
            fast.next = head
            head = fast 

        
        return head 

# Optimal solution O(n) -> Chatgpt
class SolutionTwo:
    def rotateRight(head, k):
        if not head or not head.next:
            return head

        # Step 1: find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: connect tail to head (circular list)
        tail.next = head

        # Step 3: find new head
        k = k % length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # break the cycle

        return new_head