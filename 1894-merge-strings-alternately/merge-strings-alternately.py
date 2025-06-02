class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1),len(word2))

        for i in range(0,min_len):
            result = result + word1[i]
            result = result + word2[i] 
        
        if len(word1) > len(word2):
            result = result + word1[min_len:]
        elif len(word2) > len(word1):
            result = result + word2[min_len:]

        return result
