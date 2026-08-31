class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum, curr = 0,0
        while curr<len(nums):
            currSum+=nums[curr]
            maxSum = max(maxSum, currSum)
            if currSum<0:
                currSum = 0
            curr+=1
        return maxSum



        