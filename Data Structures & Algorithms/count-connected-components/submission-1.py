class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for child in graph[node]:
                dfs(child)
            return True
        
        count = 0
        for node in range(n):
            if dfs(node):
                count += 1
        
        return count
