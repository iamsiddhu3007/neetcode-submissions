class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {}
        for i in range(numCourses):
            prereqMap[i] = []
        
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if prereqMap[crs] == []:
                return True
            visitSet.add(crs)
            for prereq in prereqMap[crs]:
                if not dfs(prereq):
                    return False
            visitSet.remove(crs)
            prereqMap[crs] = [] # optional
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                




        