class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0,0
        chars = set()
        maxLen = 0
        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                maxLen = max(maxLen, j-i+1)
                j+=1
            else:
                chars.remove(s[i])
                i+=1
        return maxLen
            


        