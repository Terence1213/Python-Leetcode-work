from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")

        new_words = []
        if len(words) > 1:
            for i in range(len(words) - 1, -1, -1):
                if words[i].strip().__contains__(" "):
                    continue
                new_words.append(words[i].strip())
        
        new_string = ""
        for index, word in enumerate(new_words):
            if index < len(new_words) - 1:
                new_string += word + " "
            else:
                new_string += word
        
        return new_string