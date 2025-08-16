from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # For each number, we're going to check if 2 times itself equals to any other number in the list.

        for index, num in enumerate(arr):
            for other_index, other_num in enumerate(arr):
                if num == other_num * 2 and index != other_index:
                    return True

        return False