class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str1_to_str2 = {}

        if len(s) != len(t):
            return False

        for index, character in enumerate(s):
            # If we've already encountered this character, then we have to make sure that the mapping has stayed the same.
            if character in str1_to_str2:
                if t[index] != str1_to_str2[character]:
                    return False
            else:
                # We also have to account for the scenario where we have for example egr and add, where g and r are mapping to the same character. 
                # Therefore we have to check for already existing values, not only keys (so all keys, AND all values must be unique)
                # At this point, if we didn't find a repeated key from the first string but there's a repeated key in the second string, the strings aren't isomorphic.
                if t[index] in str1_to_str2.values():
                    return False
                
                # In other cases, where we have a unique character, we simply add the character mapping to the map.
                str1_to_str2[character] = t[index]
            
        return True
            