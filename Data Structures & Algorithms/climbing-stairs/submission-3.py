class Solution:
    def climbStairs(self, n: int) -> int:
        localSum = {}
        def dfs(num):
            if num == n:
                return 1
            if num > n:
                return 0
            if num in localSum:
                return localSum[num]
            currSum = dfs(num + 1) + dfs(num + 2)
            localSum[num] = currSum
            return currSum
        return dfs(0)
            
        