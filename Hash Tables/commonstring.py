from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_to_index = {value: index for index, value in enumerate(list1)}

        matching_index_sums = {}

        for index, str_val in enumerate(list2):
            if str_val in list1_to_index:
                matching_index_sums[str_val] = index + list1_to_index[str_val]

        # Now that we have all of the matching strings inside the dictionary, we will find the string with the smallest index sum
        min_sum = min(matching_index_sums.values())
        result = [key for key, val in matching_index_sums.items() if val == min_sum]
        return result 