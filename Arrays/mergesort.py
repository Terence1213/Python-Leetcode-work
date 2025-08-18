from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # m -> Denotes the length of nums1
        # n -> Denotes the length of nums2
        
        # If the first list is completely empty, then we just put the second list in the first list.
        if m == 0:
            nums1_index = m
            nums1[:n] = nums2
        else:
            nums1_index = m - 1

        # Basically, we're going to compare the last element from nums2 to the last element in nums1. If it is greater, then we'll just place it there
        for num in nums2:
            # Every time we perform the check, we start with an initial index which we're checking.
            index = nums1_index
            while True:
                
                # The problem is that we're inserting a 2 before the 1, just because we're at index 0
                # This is so that if for example we have 0, 0, 3 in the nums1 list, and then we have -1 in the nums2 list, it doesn't keep on decrementing the index until it goes below 0, it just gives up at the first index since at that point it is for sure going to be the smallest.
                if index == 0:
                    if num > nums1[index] and m != 0:
                        nums1.insert(index + 1, num) # Places it after the first number, since its bigger.
                    else:
                        nums1.insert(index, num)

                    if nums1[len(nums1) - 1] == 0:
                        nums1.pop()

                    nums1_index += 1
                    break
                
                if num >= nums1[index]:
                    # Before we actually replace the number, we have to move everything else.
                    nums1.insert(index + 1, num)
                    if nums1[len(nums1) - 1] == 0:
                        nums1.pop()
                    
                    nums1_index += 1
                    break
                else:
                    # If the number we're trying to merge into the nums1 list isn't greater than the last element in the list, then we compare with the other numbers, and place the number from nums2 list accordingly
                    index -= 1
        
        print(nums1)
            
n = 3
m = 3
nums1 = [1, 3, 4]
nums2 = [2, 3, 5]

solution = Solution()
solution.merge(nums1, m, nums2, n)
        
        