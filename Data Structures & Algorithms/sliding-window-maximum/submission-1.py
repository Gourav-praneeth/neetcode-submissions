from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        res = []

        for r in range(len(nums)):

            # 1. Remove indexes outside the window
            while queue and queue[0] < r - k + 1:
                queue.popleft()

            # 2. Remove smaller values
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()

            # 3. Add current index
            queue.append(r)

            # 4. Once we have a complete window,
            #    record the maximum
            if r >= k - 1:
                res.append(nums[queue[0]])

        return res