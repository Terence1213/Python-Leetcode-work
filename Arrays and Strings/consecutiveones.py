from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1

                if current_ones > max_ones:
                    max_ones = current_ones
            elif num == 0:
                current_ones = 0
        
        return max_ones
            