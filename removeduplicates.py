from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = list()
        duplicate_numbers = 0

        for num in nums:
            if not new_list.__contains__(num):
                new_list.append(num)
            else:
                duplicate_numbers += 1
        
        k = len(nums) - duplicate_numbers
        
        nums.clear()
        for num in new_list:
            nums.append(num)
        
        print(nums)
        return k
    
nums = [1, 1, 2]
solution = Solution()
solution.removeDuplicates(nums)