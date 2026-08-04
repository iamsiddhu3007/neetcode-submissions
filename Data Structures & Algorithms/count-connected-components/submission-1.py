class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = {}
        for i in range(n):
            connections[i] = []
        for x, y in edges:
            connections[x].append(y)
            connections[y].append(x)
        
        visited = set()
        res = 0
        def dfs(node):
            visited.add(node)
            for child in connections[node]:
                # if child == parent:
                #     continue
                if child in visited:
                    continue
                if child not in visited:
                    dfs(child)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
        