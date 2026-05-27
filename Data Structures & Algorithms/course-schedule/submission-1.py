class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        for b,a in prerequisites:
            if a not in nodes:
                nodes[a]= []
            nodes[a].append(b)
        def bfs(course):
            vis = set()
            openl = deque([course])
            while openl:
                curr = openl.popleft()
                for nei in nodes[curr]:
                    if nei in vis:
                        return False
                    if nei in nodes:
                        vis.add(nei)    
                        openl.append(nei)
            return True
        print(nodes)
        for i in range(numCourses):
            if i in nodes:
                if not bfs(i):
                    print(i)
                    return False
        return True