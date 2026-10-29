class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        
        for char in s:
            if char in t:
                t = t.replace(char, "", 1)
        return t