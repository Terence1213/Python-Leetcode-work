from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = [[] for _ in nums]

        for num in nums:
            # generate a hash key for indexing, and place the number / key accordingly in the hash_set
            hash_num = num % len(nums)
            
            if len(hash_set[hash_num]) == 0:
                hash_set[hash_num].append(num)
            else:
                # we check whether in the current bucket, there exists the same exact value:
                for key in hash_set[hash_num]:
                    if key == num:
                        return True

                    hash_set[hash_num].append(num)
        
        return False