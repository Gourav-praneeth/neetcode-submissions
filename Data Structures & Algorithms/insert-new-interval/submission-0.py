class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
         
        result = []

        for i, current in enumerate(intervals):
            # current interval is before newInterval
            if current[1] < newInterval[0]:
                result.append(current)
            # current interval is after newInterval
            elif current[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval[0] = min(current[0], newInterval[0])
                newInterval[1] = max(current[1], newInterval[1])
        result.append(newInterval)
        return result