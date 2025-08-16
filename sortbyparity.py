from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_nums = list()
        even_nums = list()

        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
        
        nums.clear()

        for num in even_nums:
            