from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict(Counter(nums))
        heap = []
        for key in counts:
            heap.append((-counts[key], key))
        heapify(heap)
        res = []
        while k > 0:
            res.append(heappop(heap)[1])
            k-=1
        return res

        
        