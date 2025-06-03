import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        gcd_len = math.gcd(len(str1),len(str2))

        candidate = str1[:gcd_len]

        #using the // operator (Floor Division)
        #Here, This gives us how many times the candidate needs to be repeated to match the length of str1.
        #If you use /, you get a float (like 3.0), which will cause an error

        if candidate * (len(str1) // len(candidate)) == str1 and \
            candidate * (len(str2) // len(candidate)) == str2: 
            return candidate
        else: 
            return ""


        