from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0, k):
            # We need to move the last element to the element at the start.
            temp = nums[len(nums) - 1]
            nums.pop()
            nums.insert(0, temp)
            