from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float("inf")

        for right in range(n):
            current_sum += nums[right]

            # shrink window while sum >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len

# DIDNT WORK :(
class SolutionTwo:
    def minSubArrayLen(self, target:int, nums: List[int]) -> int:
        right_pointer = 0
        left_pointer = 0
        current_sum = 0
        min_length = float("inf")

        n = len(nums)

        while right_pointer < n:
            current_sum += nums[right_pointer]
            right_pointer += 1

            while current_sum >= target:
                min_length = min(min_length, right_pointer - left_pointer + 1)
                current_sum -= nums[left_pointer]
                left_pointer += 1
        
        if min_length == float("inf"):
            return 0

        return min_length