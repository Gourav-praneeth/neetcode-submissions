class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_join = ''

        for char in s:
            if char.isalnum():
                s_join += char.lower()

        l = 0
        r = len(s_join) - 1

        while l < r:
            if s_join[l] == s_join[r]:
                r -= 1
                l += 1
            else:
                return False
        return True
        