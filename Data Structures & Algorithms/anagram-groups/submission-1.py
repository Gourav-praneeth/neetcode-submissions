class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = {}
        for i in range(len(strs)):
            sort_str = ''.join(sorted(strs[i]))
            if sort_str not in count:
                count[sort_str] = []
            count[sort_str].append(strs[i])
        return list(count.values())

            

