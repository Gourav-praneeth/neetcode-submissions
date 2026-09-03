class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_char = {}
        l = 0
        longest_str = 0

        for r in range(len(s)):
            if s[r] not in count_char:
                count_char[s[r]] = 1
            else:
                count_char[s[r]] += 1
            
            frequent_char = max(count_char.values())

            if (r-l+1) - frequent_char > k:
                count_char[s[l]] -= 1
                l += 1
                
            longest_str = max(longest_str, r-l+1)
        return longest_str
        

                