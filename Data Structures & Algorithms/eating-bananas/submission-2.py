class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while speed < max(piles)+1:
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile/speed)
        #     if hours<=h:
        #         return speed
        #     speed+=1
        left, right = 1, max(piles)
        res = right
        while left<=right:
            mid = (left+right)//2
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        return res

