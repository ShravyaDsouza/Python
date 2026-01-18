class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rows = [[0] * (n + 1) for _ in range(m)]
        cols = [[0] * n for _ in range(m + 1)]
        d1 = [[0] * (n + 1) for _ in range(m + 1)] 
        d2 = [[0] * (n + 2) for _ in range(m + 1)] 

        for r in range(m):
            for c in range(n):
                rows[r][c+1] = rows[r][c] + grid[r][c]
                cols[r+1][c] = cols[r][c] + grid[r][c]
                d1[r+1][c+1] = d1[r][c] + grid[r][c]
                d2[r+1][c+1] = d2[r][c+2] + grid[r][c] 

        def is_magic(r, c, k):
            target = rows[r][c + k] - rows[r][c]
            
            for i in range(r + 1, r + k):
                if rows[i][c + k] - rows[i][c] != target: return False
                
            for j in range(c, c + k):
                if cols[r + k][j] - cols[r][j] != target: return False
                
            if d1[r + k][c + k] - d1[r][c] != target: return False
            
            if d2[r + k][c + 1] - d2[r][c + k + 1] != target: return False
            
            return True

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1
