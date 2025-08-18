from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        indexes_to_insert = []

        for i in range(0, len(arr)):
            # i is going to be less than the length of the original array subtracted by the amount of zeros which we're going to be inserting.
            # So if we were going to be originally inserting 3 zeros, and we are currently at index 6 from 9, index 6 will be the last index we check before actually adding zeros.
            if arr[i] == 0 and i <= (len(arr) - 1) - len(indexes_to_insert):
                indexes_to_insert.append(i + 1)
                # When determining whether to add this number as an index, we have to also check whether this number will have been removed because of the inserting together with keeping the original array length

            
        zeros_inserted = 0
        while True:

            if len(indexes_to_insert) == 0:
                break
            
            # Note: The zeros_inserted  number is so that we can adjust the index based on the varying size of the list when we insert a zero.
            arr.insert(indexes_to_insert[zeros_inserted] + zeros_inserted, 0)
            arr.pop()
            zeros_inserted += 1
            
            if zeros_inserted == len(indexes_to_insert):
                break