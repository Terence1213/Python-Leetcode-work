from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list(nums)

        # We will square each number in this new list
        for i in range(0, len(new_list)):
            new_list[i] = new_list[i] * new_list[i]
        
        # Now we have to perform the sorting since numbers can change.
        swap = True
        while swap == True:
            swap = False

            for i in range(0, len(new_list) - 1):
                if new_list[i] > new_list[i + 1]:
                    temp = new_list[i]
                    new_list[i] = new_list[i + 1]
                    new_list[i + 1] = temp
                    swap = True
        
        return new_list
    
nums = [-4,-1,0,3,10]
solution = Solution()
solution.sortedSquares(nums)

class SolutionTwo:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list()

        # Basically, we're going to check which number from the left / right is bigger, add that number to the list, and then adjust the pointers
        left_pointer = 0
        right_pointer = len(nums) - 1

        if left_pointer == right_pointer:
            new_list.append(nums[0] ** 2)
            return new_list # This indicates that there's only one number in the list, so we just return the original list squared.
        
        while True:
            if abs(nums[left_pointer]) > abs(nums[right_pointer]):
                new_list.append(nums[left_pointer] ** 2)
                left_pointer += 1
            else:
                new_list.append(nums[right_pointer] ** 2) 
                right_pointer -= 1
        
            if left_pointer == right_pointer:
                new_list.append(nums[left_pointer] ** 2)
                break # If the left pointer is now equal to or greater than the right pointer, it means that we would be comparing 
        
        new_list.reverse()
        return new_list
    
nums = [-4,-1,0,3,10]
solution = SolutionTwo()
print(solution.sortedSquares(nums))