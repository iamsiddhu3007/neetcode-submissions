class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        res = 0
        chars = set()
        while j < len(s):
            while s[j] in chars:
                chars.remove(s[i])
                i+=1
            chars.add(s[j])
            res = max(res, j-i+1)
            j+=1
        return res

            


        