class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for x, y in prerequisites:
            preMap[x].append(y)
        
        out = []
        visited = set()
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            out.append(crs)
            #preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return out



        

        