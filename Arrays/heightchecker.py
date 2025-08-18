from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # We have to check whether the heights are completely ascending.
        # The way im going to do this is first create a new list which is sorted, and then compare it to the old list
        sorted_heights = list(heights)
        k = 0
        
        # Now we sort the heights:
        swap = True
        while swap == True:
            swap = False

            for i in range(0, len(sorted_heights) - 1):
                if sorted_heights[i] > sorted_heights[i + 1]:
                    temp = sorted_heights[i + 1]
                    sorted_heights[i + 1] = sorted_heights[i]
                    sorted_heights[i] = temp
                    swap = True
        
        for i in range(0, len(sorted_heights)):
            if sorted_heights[i] != heights[i]:
                k += 1
        
        return k

heights = [1,1,4,2,1,3]
solution = Solution()
solution.heightChecker(heights)

class SolutionTwo: 
    def heightChecker(self, heights: List[int]) -> int:

        sorted_heights = sorted(heights)
        k = 0
        
        for i in range(0, len(sorted_heights)):
            if sorted_heights[i] != heights[i]:
                k += 1
        
        return k