class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = {}
        for i in range(n):
            connections[i] = []
        
        for x,y in edges:
            connections[x].append(y)
            connections[y].append(x)

        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for child in connections[node]:
                if child == parent:
                    continue
                if child in visited:
                    return False
                if dfs(child, node) is False:
                    return False
            return True
        validTree = False
        validTree = dfs(0, None)
        return len(visited) == n and validTree
        
        
        