from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            heap.append([dist, x, y])
        heapify(heap)
        res = []
        while k > 0:
            point = heappop(heap)
            res.append([point[1], point[2]])
            k-=1
        return res

        
        