class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0

        for fast in range(len(t)):
            if slow < len(s) and t[fast] == s[slow]: #slow <len(s) is to handle a special case, the other condition is logic
                slow += 1
        
        if slow == len(s):
            return True
        else:
            return False
        