class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in targetDict:
                return [targetDict[diff], i]
            targetDict[num] = i