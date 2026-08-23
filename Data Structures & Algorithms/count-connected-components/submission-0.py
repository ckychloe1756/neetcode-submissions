class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        
        return res
