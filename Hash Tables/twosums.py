from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num # This number is practically the number which we need apart from the current number (num) which we're checking through for us to get the total sum required by the target.

            # So what we're going to do is see if from the numbers we've checked already, the number we're looking for exists.
            # This way, we're checking through all different possibilities of combinations. 
            if complement in num_to_index: # as a key
                # In this case, we've found a matching number, so we return the 2 indexes.
                return [num_to_index[complement], i]

            num_to_index[num] = i
        
        return None # If code reaches this point and we stil haven't returned 2 indexes