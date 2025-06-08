class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim the input string
        trimmed = s.strip()
    
        # Step 2: Split the string by spaces (split() handles multiple spaces)
        words = trimmed.split()
    
        # Step 3: Reverse the list of words
        reversed_words = words[::-1] #list[start:stop:step]
    
        # Step 4: Join the reversed list with a single space
        result = ' '.join(reversed_words)
    
        return result

