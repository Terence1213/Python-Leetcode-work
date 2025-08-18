from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        matching_values = 0

        # My solution is that I'll completely remove the numbers that are equal to the avlue 
        for i in range(0, len(nums)):
            if nums[i] != val:
                new_list.append(nums[i])
            else:
                matching_values += 1

        k = len(nums) - matching_values

        nums.clear()
        for num in new_list:
            nums.append(num)
        
        print(nums)
        return k

nums = [3, 2, 2, 3]
val = 3

solution = Solution()
print(solution.removeElement(nums, val))