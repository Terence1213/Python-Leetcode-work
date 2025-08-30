class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TRIED DOING THIS ON MY OWN, DIDN'T WORK
    def oddEvenList(self, head: ListNode) -> ListNode:
        # What I'm thinking is that for every even iteration, we save the current node within a list (array) of nodes, and we set the pointer of the previous node to the next odd node.
        prev = head
        current = head.next

        is_even = True

        node_list = []

        while current != None:

            if is_even:
                node_list.append(current)
                prev.next = current.next
                is_even = False
            else:
                prev = prev.next
                is_even = True
            
            current = current.next
        
        current = node_list[0]
        prev.next = current

        # Now that current is at the node after the last one, we set the current as the first node in the node_list.
        if len(node_list) > 1:
            for index, node in enumerate(node_list):
                if index == len(node_list) - 1:
                    current.next = node

        current = current.next
        current.next = None
        return head

class SolutionTwo:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head              # odd list head
        even = head.next        # even list head
        even_head = even        # keep start of even list

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head    # append even list to end of odd
        return head