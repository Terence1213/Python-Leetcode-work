from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = [char for char in a]
        num2 = [char for char in b]
        result_num = []
        carry = '0'

        # Now we have to make sure that the 2 lists are of the same length, if not, we have to add zeros to the left of the number.
        if len(num1) != len(num2):
            if len(num1) < len(num2):
                # Add zeros to num1:
                for i in range(0, len(num2) - len(num1)):
                    num1.insert(0, '0')
            else:
                # Add zeros to num2:
                for i in range(0, len(num1) - len(num2)):
                    num2.insert(0, '0')
        
        # Now we perform addition.
        for i in range(len(num1) - 1, -1, -1):
            if num1[i] == '1' and num2[i] == '1':
                if carry == '1':
                    result_num.insert(0, '1')
                else:
                    result_num.insert(0, '0')
                
                carry = '1'
            elif (num1[i] == '1' and num2[i] == '0') or (num1[i] == '0' and num2[i] == '1'):
                if carry == '1':
                    result_num.insert(0, '0')
                    carry = '1'
                else:
                    result_num.insert(0, '1')
            elif num1[i] == '0' and num2[i] == '0':
                if carry == '1':
                    result_num.insert(0, '1')
                    carry = '0'
                else:
                    result_num.insert(0, '0')
        
        # in case of overflows, if we've finished looping through the length of the numbers and the carry is still set as 1, then we will insert a 1 to the result.
        if carry == '1':
            carry = '0'
            result_num.insert(0, '1')
        
        result = "".join(result_num)
        return result
    
# (Note that this solution went from beating 53% of solutions in terms of memory usage with the previous solution, to 42% with the new solution)
# Solution which is slightly more efficient, replacing the inserting (which is very unefficient since we have to shift all elements within the list to the right when inserting) with appending and then reversing the list at the end.
class SolutionTwo:
    def addBinary(self, a: str, b: str) -> str:
        num1 = [char for char in a]
        num2 = [char for char in b]
        result_num = []
        carry = '0'

        # Now we have to make sure that the 2 lists are of the same length, if not, we have to add zeros to the left of the number.
        if len(num1) != len(num2):
            if len(num1) < len(num2):
                # Add zeros to num1:
                for i in range(0, len(num2) - len(num1)):
                    num1.insert(0, '0')
            else:
                # Add zeros to num2:
                for i in range(0, len(num1) - len(num2)):
                    num2.insert(0, '0')
        
        # Now we perform addition.
        for i in range(len(num1) - 1, -1, -1):
            if num1[i] == '1' and num2[i] == '1':
                if carry == '1':
                    result_num.append('1')
                else:
                    result_num.append('0')
                
                carry = '1'
            elif (num1[i] == '1' and num2[i] == '0') or (num1[i] == '0' and num2[i] == '1'):
                if carry == '1':
                    result_num.append('0')
                    carry = '1'
                else:
                    result_num.append('1')
            elif num1[i] == '0' and num2[i] == '0':
                if carry == '1':
                    result_num.append('1')
                    carry = '0'
                else:
                    result_num.append('0')
        
        # in case of overflows, if we've finished looping through the length of the numbers and the carry is still set as 1, then we will insert a 1 to the result.
        if carry == '1':
            carry = '0'
            result_num.append('1')
        
        result_num.reverse()
        result = "".join(result_num)
        return result