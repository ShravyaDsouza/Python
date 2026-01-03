from functools import lru_cache
import sys

# Increase recursion depth for larger values of n
sys.setrecursionlimit(5000)

def numOfWays(n: int) -> int:
    MOD = 10**9 + 7

    @lru_cache(None)
    def solve(i, prev1, prev2, prev3):
        # Base case: if we've filled all n rows
        if i == n:
            return 1
        
        ans = 0
        # Try all colors (1, 2, 3) for the three slots in the current row
        for col1 in range(1, 4):
            if col1 == prev1:
                continue
            for col2 in range(1, 4):
                if col2 == col1 or col2 == prev2:                # col2 cannot be same as its neighbor (col1) or the one above it (prev2)
                    continue
                for col3 in range(1, 4):                         # col3 cannot be same as its neighbor (col2) or the one above it (prev3)
                    if col3 == col2 or col3 == prev3:
                        continue
                    
                    ans = (ans + solve(i + 1, col1, col2, col3)) % MOD
        return ans

    # Start the recursion from row 0 with no previous colors (0, 0, 0)
    return solve(0, 0, 0, 0)

n_val = int(input("Enter n: "))
result = numOfWays(n_val)
print(f"Result: {result}")
