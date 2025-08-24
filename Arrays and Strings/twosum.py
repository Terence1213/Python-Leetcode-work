from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for index, number in enumerate(numbers):
            two_sum = 0
            if number > target:
                break
                
            for x in range(index + 1, len(numbers)):
                if numbers[x] > target:
                    break

                two_sum = number + numbers[x]

                if two_sum == target:
                    return [index + 1, x + 1]
        
        # DOESNT WORK

class SolutionTwo:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        
        while left < right:
            two_sum = numbers[left] + numbers[right]
            
            if two_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            
            elif two_sum < target:
                left += 1  # need bigger sum
            
            else:
                right -= 1  # need smaller sum
        

