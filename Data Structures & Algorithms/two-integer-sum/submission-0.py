class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mydict:
                return [mydict[diff], i]
            mydict[num] = i
        return []

        