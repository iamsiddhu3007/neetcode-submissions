from heapq import *
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)

        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt != 0:
                    queue.append((cnt, time+n))
            if queue and queue[0][1] == time:
                heappush(maxHeap, queue.popleft()[0])
        return time


        