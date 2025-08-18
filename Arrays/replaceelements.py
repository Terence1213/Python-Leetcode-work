from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = list()

        for i in range(0, len(arr)):

            if i == len(arr) - 1:
                new_arr.append(-1)
                break

            biggest_num = 0
            for x in range(i + 1, len(arr)):
                if arr[x] > biggest_num:
                    biggest_num = arr[x]
            
            new_arr.append(biggest_num)
        
        return new_arr

class SolutionTwo:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current) # If the current number is bigger than the max that we've had so far, then we update the max so far for the next numbers which we'll be checking.
        
        return arr
            