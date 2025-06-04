class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Define the set of vowels (both lowercase and uppercase)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #This is how a set is defined, using {}
        
        # Step 2: Convert the input string to a list of characters
        chars = list(s)

        # Step 3: Initialize two pointers
        left = 0
        right = len(chars) - 1

        # Step 4: Use two-pointer technique to find vowels and swap them
        while left < right:
            #Move left pointer forward until a vowel is found
            while left < right and chars[left] not in vowels:
                left += 1

            #Move right pointer forward until a vowel is found
            while left < right and chars[right] not in vowels:
                right -= 1

            #Since we have used "not in" above we come to this point only if we get vowels in char, so we can swap

            # Both chars[left] and chars[right] are vowels, so swap them
            chars[left], chars[right] = chars[right], chars[left]

            # Move the pointers inward to continue the search
            left += 1
            right -= 1

        # Step 5: Convert the list back to a string and return the result
        return ''.join(chars)




        



