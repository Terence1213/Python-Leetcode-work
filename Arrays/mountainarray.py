from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # There should be one increasing point and one decreasing point.
        increasing = 0
        decreasing = 0
        increasing_status = False
        decreasing_status = False
        increasing_first = False

        for i in range(0, len(arr) - 1):
            # The way I'm going to do it is that if increasing is currently false, then we set it to true and increment increasing by one.
            # If increasing is already set as true, then we don't increment increasing by one since it was already previously increasing.
            if arr[i] < arr[i + 1] and increasing_status == False:
                if decreasing_status == False:
                    increasing_first = True

                increasing_status = True
                decreasing_status = False
                increasing += 1
            elif arr[i] > arr[i + 1] and decreasing_status == False:
                if increasing_status == False:
                    increasing_first = False

                decreasing_status = True
                increasing_status = False
                decreasing += 1
            elif arr[i] == arr[i + 1]:
                return False
        
        # Apart from checking that there's exactly one decreasing point and one increasing point, we also have to make sure that the first turning point is an increasing point.
        if decreasing == 1 and increasing == 1 and increasing_first == True:
            return True
        
        return False
    