class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for left in range(len(heights)):
            for right in range(left+1, len(heights)):
                area = (right-left)*min(heights[left], heights[right])
                res = max(res, area)
        return res

        