from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for each element, we're going to check the elements to the left and the elements to the right, and take the sum of each side.
        # We then check whether these sums are equal, and return the index if true.

        for i in range(0, len(nums)):
            left_sum = 0
            right_sum = 0

            if i != 0:
                # if the index is not 0, then we're going to loop through all indexes left to the current one.
                for x in range(i, -1, -1):
                    left_sum += nums[x]

            if i != len(nums) - 1:
                for x in range(i + 1, len(nums)):
                    right_sum += nums[x]

            if left_sum == right_sum:
                return i  
        
        return -1

class SolutionTwo:
    def pivotIndex(self, nums: List[int]) -> int:
        # So basically from what I understood, we're going to take an initial total sum, starting with a left_sum of 0, and then with each index, we increase the left_sum by the value of the current index.
        left_sum = 0
        total_sum = sum(nums)

        
        for index, number in enumerate(nums):
            right_sum = total_sum - (left_sum + number)
            if left_sum == right_sum:
                return index
            left_sum += number
        
        return -1
            