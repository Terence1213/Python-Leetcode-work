class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = []
        num2 = []

        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next
        
        # Reverse the numbers
        num1 = num1[::-1] 
        num2 = num2[::-1]

        # Convert the array of numbers into one number:
        whole_num1 = 0

        for num in num1:
            whole_num1 = whole_num1 * 10 + num
        
        whole_num2 = 0

        for num in num2:
            whole_num2 = whole_num2 * 10 + num
        
        sum = whole_num1 + whole_num2

        separated_sum = [int(digit) for digit in str(num)]
        separated_sum = separated_sum[::-1]

        head = ListNode(separated_sum[0])
        current = head

        for i in range(1, len(separated_sum)):
            current.next = ListNode(separated_sum[i])
            current = current.next

        return head 

        