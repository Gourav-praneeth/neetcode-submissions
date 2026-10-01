class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initilise a dic 
        count = {}

        for word in strs:
            key = "".join(sorted(word)) # aet 
            if key not in count:
                count[key] = []

            count[key].append(word)
        return list(count.values())