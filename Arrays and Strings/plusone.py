from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # We must append the numbers onto a string then convert it into an integer.
        string_value = ""
        for num in digits:
            string_value += str(num)
        
        value = int(string_value)
        value += 1

        # Convert the string number back to a list
        string_value = str(value)

        new_list = []

        for char in string_value:
            new_list.append(int(char))

        return new_list
    

