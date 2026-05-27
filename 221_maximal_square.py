from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_s = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                if dp[i][j] > max_s:
                    max_s = dp[i][j]
    return max_s * max_s
