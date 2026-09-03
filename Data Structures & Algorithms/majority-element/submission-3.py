class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        largest = max(count.values())

        for num in count:
            if count[num] == largest:
                return num
        