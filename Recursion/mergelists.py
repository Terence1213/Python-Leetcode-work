class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2 # If we reach the end of list1, then we return the rest of list 2
        if list2 == None:
            return list1 # If we reach the end of list2, we return the rest of list1
        
        if list1.val < list2.val:
            # If the value of the current list1 is smaller than the currentlist2, then we must continue the merged list from list1's next value
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 
        else:
            # if list2 is smaller than or equal to list1's value, then we're going to continue from list2.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
class PracticeSolution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
    
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2