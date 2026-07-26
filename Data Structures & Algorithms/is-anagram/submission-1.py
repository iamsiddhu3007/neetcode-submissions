class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        def createDict(string):
            out = {}
            for char in string:
                if char not in out:
                    out[char] = 1
                else:
                    out[char] += 1
            return out
        return createDict(s) == createDict(t)
        