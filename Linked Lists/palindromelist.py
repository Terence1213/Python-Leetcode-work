class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        my_list = []

        current = head

        while current != None:
            my_list.append(current.val)
            current = current.next
        
        return my_list == my_list[::-1]  # the [::-1] Reverses the list, so basically we're checking whether the original list is equal to the list itself reversed.