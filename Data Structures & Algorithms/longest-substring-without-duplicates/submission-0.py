class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        l = 0 

        for r in range(len(s)): 
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        
            max_length = max(max_length, r - l + 1)
        return max_length
            

        
    '''
        U: Given a string return longest substring without any repeating characters the output should be an int.
        P: 
        have a count var which counts the string without repeating char
        assign lptr, rptr to 0
        loop as rptr grows:
        if the window contains any char seen then move lptr until there is no char in seen
        '''


        