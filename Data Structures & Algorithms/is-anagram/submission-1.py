class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for i in range(len(sorted_s)):
            if sorted_s[i - 1] != sorted_t[i - 1]:
                return False
        return True