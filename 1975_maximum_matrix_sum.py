class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        sum = 0
        count_n = 0
        min_abs_val = float('inf') 
        
        for row in matrix:
            for val in row:
                sum += abs(val)
                if val < 0:
                    count_n += 1   
                if abs(val) < min_abs_val:
                    min_abs_val = abs(val)
    
        if count_n % 2 != 0:
            return sum - (2 * min_abs_val)
        
        return sum
