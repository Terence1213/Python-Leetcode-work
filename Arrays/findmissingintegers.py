from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        integers = [num for num in range(1, len(nums) + 1) if not nums.__contains__(num)]
        return integers
    
class SolutionTwo:
    def findDissapearedNumbers(self, nums: List[int]) -> List:
        all_nums = set(range(1, len(nums) + 1))
        return list(all_nums - set(nums)) 
        # all_nums - set(nums) will make return a result where all values within all_nums which are also contained within nums are removed, effectively returning the missing numbers from nums.
        # Lesson here is that when we're comparing 2 lists together, a very efficient way of doing so is making use of sets rather than lists.