class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        n = len(bottomLeft)
        
        for i in range(n):
            for j in range(i + 1, n): 
                x_start = max(bottomLeft[i][0], bottomLeft[j][0])
                x_end = min(topRight[i][0], topRight[j][0])
                
                y_start = max(bottomLeft[i][1], bottomLeft[j][1])
                y_end = min(topRight[i][1], topRight[j][1])

                if x_start < x_end and y_start < y_end:
                    width = x_end - x_start
                    height = y_end - y_start
                    
                    curr_side = min(width, height)
                    max_side = max(max_side, curr_side)
        
        return max_side * max_side
