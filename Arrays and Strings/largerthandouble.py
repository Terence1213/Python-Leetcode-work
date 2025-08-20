from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        max_index = -1

        for index, num in enumerate(nums):
            if max_num == num:
                max_index = index
            elif max_num < (num * 2):
                return -1

        return max_index