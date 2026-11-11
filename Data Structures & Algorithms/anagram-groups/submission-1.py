class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sortedstr = "".join(sorted(s))
            if sortedstr in res:
                res[sortedstr].append(s)
            else:
                res[sortedstr] = [s]
        out = []
        for s in res:
            out.append(res[s])
        return out

        