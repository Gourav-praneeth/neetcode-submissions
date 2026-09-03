class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need to get a window size => window = len(s1)
        window = len(s1) # abd 3
        l = 0 
        count_char_s2 = {}
        count_char_s1 = {}

        # adds the frequency of s1 to count_char_s1
        for i in s1:
            if i not in count_char_s1:
                count_char_s1[i] = 1
            else:
                count_char_s1[i] += 1


        for r in range(len(s2)):
            if s2[r] not in count_char_s2:
                count_char_s2[s2[r]] = 1
            else:
                count_char_s2[s2[r]] += 1
            
            if r-l+1 == window:
                if count_char_s1 == count_char_s2:
                    return True
                count_char_s2[s2[l]] -= 1
                
                # Delete char when the value reaches zero
                if count_char_s2[s2[l]] == 0:
                    count_char_s2.pop(s2[l])

                l+=1
                    
        return False

            
