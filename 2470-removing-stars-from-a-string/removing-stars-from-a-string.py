class Solution:
    def removeStars(self, s: str) -> str:
        '''
        1. Initialize an empty list called 'stack'
        2. For each character 'ch' in the input string 's':
                a. If 'ch' is not '*':
                - Append 'ch' to 'stack'
                b. Else (if 'ch' is '*'):
                - Pop the last element from 'stack' (remove closest non-star character)
        3. After processing all characters:
                - Join the elements of 'stack' to form the final string
        4. Return or print the final string
        '''
        stack = []

        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()
        
        return ''.join(stack) 