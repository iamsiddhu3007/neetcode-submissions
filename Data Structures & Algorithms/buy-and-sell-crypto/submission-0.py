class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i < j:
                    maxp = max(maxp, prices[j]- prices[i])
                else:
                    continue
        return maxp
        