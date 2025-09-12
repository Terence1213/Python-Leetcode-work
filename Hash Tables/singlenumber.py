from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = [[] for _ in nums]

        for num in nums:
            # Generate hash index
            hash_num = num % len(nums)

            # if the number already exists, then remove it, if the number doesn't exist, then add it.
            if num in hash_set[hash_num]:
                hash_set[hash_num].remove(num)
            else:
                hash_set[hash_num].append(num)
        
        for bucket in hash_set:
            if len(bucket) == 1:
                return bucket[0]