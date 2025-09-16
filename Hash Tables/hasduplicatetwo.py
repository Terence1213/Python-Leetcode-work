from typing import List

# This solution works, but it isn't that efficient, because of creating a new list (having the same size of the hash map) with every iteration of the loop.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Normally what we would do is that we loop through the list of numbers, and add them to a hash set which only stores unique values,
        # and if we find a value which already exists within the hash set at any point, then the duplicate exists.

        # Now in our case, we don't want to check through the whole hash set, we want to check through elements not more than k indexes away from the current index.
        # so if we're at index 4, and k = 2, then we want to compare index 4 with indexes 3 and 2 only.

        # What I'm thinking is that with every iteration of the loop, we delete elements which have been passed by the k index marker.
        # so if we're at index 4 and k = 2, then the elements at indexes 0 and 1 are deleted.
        hash_map = {}

        for i, num in enumerate(nums):
            # Deletion done here.
            # Note that I didn't just loop through hash_map.items() since were deleting elements from hash_map, while iteration through it, which would cause issues.
            for number in list(hash_map.keys()):
                if hash_map[number] < i - k: 
                    hash_map.pop(number)
                else:
                    break # If the index is valid, then deletion is complete, 
            
            # This is considering that the deletion is already done, so we don't have to check whether the index of the duplicate is correct.
            if num in hash_map:
                return True
            
            hash_map[num] = i
        
        return False

class SolutionTwo:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # determines the window of numbers at which we can compare duplicates validly.

        for i, num in enumerate(nums):
            if num in window:
                return True
        
            window.add(num)

            # Making sure that the size of the window remains <= k
            if len(window) > k:
                window.remove(nums[i - k]) # So if we're at index 2, and k = 2, we will remove index 0, and remain with elements of indexes 1 and 2.
                # Therefore on the next iteration of the loop, we'll be comparing the 3rd index with the indexes 1 and 2.

        return False