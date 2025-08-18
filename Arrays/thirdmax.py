from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        second_max = 0
        third_max = 0
        distinct_nums = 0
        new_list = list()
        
        for num in nums:
            
            if not new_list.__contains__(num):
                distinct_nums += 1
                new_list.append(num)

            if num > second_max and num < first_max:
                second_max = num
            elif (num > third_max or num <= second_max) and num < first_max:
                third_max = num
        
        print(first_max) 
        print(third_max)
        
        if distinct_nums >= 3:
            return third_max
        else:
            return first_max
    
class SolutionTwo: # THIS ONE WORKED
    def thirdMax(self, nums: List[int]) -> int:

        new_list = list()
        distinct_nums = 0

        for num in nums:
            if not new_list.__contains__(num):
                distinct_nums += 1
                new_list.append(num)
                    
        first_max = max(nums)
        nums = [num for num in nums if num != first_max] # effectively removes all occurances of first_max from the list

        if len(nums) == 0:
            return first_max # This would mean that there was only one unique number
        
        second_max = max(nums)
        nums = [num for num in nums if num != second_max]
    
        if distinct_nums < 3:
            return first_max
    
        third_max = max(nums)
        return third_max
        
