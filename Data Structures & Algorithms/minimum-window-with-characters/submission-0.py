class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        sub_str = 0
        min_window = len(s) + 1

        count_t = {}
        curr_window = {}

        has = 0

        for char in t:
            if char not in count_t:
                count_t[char] = 1
            else:
                count_t[char] += 1

        need = len(count_t) 

        for r in range(len(s)):
            if s[r] not in curr_window:
                curr_window[s[r]] = 1
            else:
                curr_window[s[r]] += 1
            
            if s[r] in count_t and curr_window[s[r]] == count_t[s[r]]:
                has += 1

            while has == need:
                window = r - l + 1
                if window < min_window:
                    min_window = window
                    sub_str = l

                curr_window[s[l]] -= 1

                if s[l] in count_t and curr_window[s[l]] < count_t[s[l]]:
                    has -= 1

                l += 1

        if min_window == len(s)+1:
            return ""         

        return s[sub_str:sub_str + min_window]
            



        '''
        {
        x:1
        y:1
        z:1
        }
        if count_t.keys() <= count_s.keys():
        '''