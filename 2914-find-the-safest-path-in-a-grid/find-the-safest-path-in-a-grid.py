from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # ─── PHASE 1: Multi-source BFS to build distance map ───
        
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        # add all thieves to queue first
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        # BFS outward from all thieves
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # ─── PHASE 2: Binary search on safeness value ───
        
        def canReach(minSafe):
            # can we go from (0,0) to (n-1,n-1) 
            # only stepping on cells with dist >= minSafe?
            if dist[0][0] < minSafe or dist[n-1][n-1] < minSafe:
                return False
            
            visited = [[False] * n for _ in range(n)]
            queue = deque()
            queue.append((0, 0))
            visited[0][0] = True
            
            while queue:
                r, c = queue.popleft()
                if r == n-1 and c == n-1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < n 
                        and not visited[nr][nc] 
                        and dist[nr][nc] >= minSafe):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
        
        # binary search between 0 and n
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                lo = mid + 1   # try higher safeness
            else:
                hi = mid - 1   # try lower safeness
        
        return hi