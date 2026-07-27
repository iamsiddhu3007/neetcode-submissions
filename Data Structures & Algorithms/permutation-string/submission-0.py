class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for char in s1:
            if char in s1Count:
                s1Count[char] += 1
            else:
                s1Count[char] = 1
        
        if len(s1)>len(s2):
            return False
        
        s2Count = {}
        left=0
        for right in range(len(s2)):
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]
                left += 1

            if s2Count == s1Count:
                return True

        return False