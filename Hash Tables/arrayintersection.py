from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        result = []

        # First we loop through the first list and specify the count of each number.
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1 # If the number hasn't been added to the counts hash map yet, then we get a default count value of 0 for that number. (and increment it by one)

        # Now that we've specified the counts for each number in the first list, we have to compare with the second list.
        for num in nums2:
            if counts.get(num, 0) > 0: # If the current number in nums2 exists in counts at this point, then we add it to the result list.
                result.append(num)
                counts[num] -= 1
        
        return result 