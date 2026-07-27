class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        ###brute force
        res = 0
        for left in range(len(heights)):
            for right in range(left+1, len(heights)):
                area = (right-left)*min(heights[left], heights[right])
                res = max(res, area)
        return res
        '''
        left, right = 0, len(heights)-1
        maxWater = float('-inf')
        while left<right:
            area = (right-left)*min(heights[left], heights[right])
            maxWater = max(maxWater, area)
            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater

        