class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        connections = {}
        for i in range(1, n+1):
            connections[i] = []
        
        def dfs(a, b, visited):
            if a == b:
                return True
            visited.add(a)
            for nei in connections[a]:
                if nei not in visited and dfs(nei, b, visited):
                    return True
            return False


        for (a, b) in edges:
            if a in connections and b in connections and dfs(a, b, set()):
                return [a,b]
            connections[a].append(b)
            connections[b].append(a)
        return []
        