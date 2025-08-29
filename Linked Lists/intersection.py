class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # What we have to do is increment pointerA and pointerB, if the next value ends up being None, then for ONE time, we will set the pointer to the head of the other letter, and continue incrementing
        # The way this works is that if list A has a total of m nodes, and list B has a total of n nodes, we're making sure that both pointerA and pointerB are travelling m + n (or n + m) nodes, ensuring that 
        # at some point, IF the lists do intersect the 2 pointers A and B will have the same node reference value.
        if headA == None or headB == None:
            return None
        
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            # The way this works is that we increment the pointer as long as they aren't Null. If they are null, then we set the pointer to headB. 
            # The reason this doesn't end up in an infinte loop is that if the pointers don't intersect, considering that the pointers will both be travelling m + n, at the end, both pointers will
            # find the end of their own lists at the same exact time, hence they will both be set to None at the same time and hence leading to the loop to stop iterating because of the condition.
            pointer_a = pointer_a.next if pointer_a != None else headB 
            pointer_b = pointer_b.next if pointer_b != None else headA
        
        return pointer_a # If at no point was a matching pointaer_a found to a pointer_b, then there was no intersection, so we return None