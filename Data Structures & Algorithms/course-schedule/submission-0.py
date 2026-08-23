class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return completed == numCourses