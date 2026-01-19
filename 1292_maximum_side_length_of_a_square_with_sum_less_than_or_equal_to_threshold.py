class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        max_len = 0
        m , n = len(mat) , len(mat[0])

        prefix = [[0] * (n+1) for _ in range(m+1)]
        for i in range (1,m+1):
            for j in range (1,n+1):
                prefix [i][j] = mat[i-1][j-1] + prefix[i-1][j]+ prefix[i][j-1] - prefix[i-1][j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = max_len+1

                if i >= k and j >= k:
                    current_sum = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
                    if current_sum <= threshold:
                        max_len = k

        return max_len
