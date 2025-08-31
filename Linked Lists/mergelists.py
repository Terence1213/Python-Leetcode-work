class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        current = head
        
        while list1 != None and list2 != None:
            if list1 != None and list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            elif list2 != None and list2.val <= list1.val:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Considering that we're stopping the loop at the point where ONE of the lists reach their end, the other list may have not reached its end so we have to make sure that 
        # we attach the rest of the other list.
        if list1 != None:
            current.next = list1
        elif list2 != None:
            current.next = list2
            
        return head

