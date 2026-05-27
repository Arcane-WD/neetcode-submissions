class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = set()
        def bfs(node):
            openl = deque([node])
            while openl:
                cur = openl.popleft()
                vis.add(cur)
                for nei in graph[cur]:
                    if nei not in vis:
                        openl.append(nei)
        connectedComponents = 0
        for i in range(n):
            if i not in vis:
                bfs(i)
                connectedComponents+=1
        return connectedComponents
