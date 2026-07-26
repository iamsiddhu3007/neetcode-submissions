class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set(nums)
        # return len(nums) != len(nums_set)
        myDict = {}
        for num in nums:
            if num not in myDict:
                myDict[num] = 0
            else:
                myDict[num] += 1
                return True
        return False