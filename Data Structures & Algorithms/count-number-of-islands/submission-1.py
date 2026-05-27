class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # vis = set()
        def bfs(i,j):
            openl = deque([(i,j)])
            while openl:
                x,y = openl.popleft()
                dirs = [[0,1],[0,-1],[-1,0],[1,0]]
                for dx, dy in dirs:
                    X,Y = x+dx, y+dy
                    if 0<=X<len(grid) and 0<=Y<len(grid[0]) and grid[X][Y]=="1":
                        openl.append((X,Y))
                        grid[X][Y] = '#'
        isles=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i,j)
                    isles+=1
        return isles
