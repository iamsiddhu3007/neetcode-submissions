from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            last = heappop(stones)
            secondlast = heappop(stones)
            if last != secondlast:
                heappush(stones, last - secondlast)
        return -stones[0] if stones else 0

        