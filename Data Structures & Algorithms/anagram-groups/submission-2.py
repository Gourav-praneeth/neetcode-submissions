class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for word in strs:
            freq = [0] * 26

            for char in word:
                index = ord(char) - ord('a') 
                freq[index] += 1
            key = tuple(freq)

            if key not in count:
                count[key] = []
            
            count[key].append(word)
        return list(count.values())
        # count = {}
        # for i in range(len(strs)):
        #     sort_str = ''.join(sorted(strs[i]))
        #     if sort_str not in count:
        #         count[sort_str] = []
        #     count[sort_str].append(strs[i])
        # return list(count.values())