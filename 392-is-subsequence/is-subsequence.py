class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0

        for fast in range(len(t)):
            if slow < len(s) and t[fast] == s[slow]: 
                slow += 1
        
        if slow == len(s):
            return True
        else:
            return False
        