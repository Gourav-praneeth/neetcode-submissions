class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def bt_dfs(start,remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            if remaining < 0:
                return

            for i in range(start,len(candidates)):
                current.append(candidates[i])
                bt_dfs(i, remaining - candidates[i])
                current.pop()

        bt_dfs(0,target)
        return result