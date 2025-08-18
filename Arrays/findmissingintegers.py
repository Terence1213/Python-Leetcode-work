from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        integers = [num for num in range(1, len(nums) + 1) if not nums.__contains__(num)]
        for num in nums:
            if integers.__contains__(num):
                integers.remove(num)
        
        return integers