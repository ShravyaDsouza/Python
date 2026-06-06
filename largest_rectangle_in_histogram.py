class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [0]*n
        nse = [0]*n

        stack1 = []
        for i in range(n):
            while stack1 and heights[stack1[-1]]>=heights[i]:
                stack1.pop()
            pse[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
        
        stack2 = []
        for i in range(n-1,-1,-1):
            while stack2 and heights[stack2[-1]]>=heights[i]:
                stack2.pop()
            nse[i] = stack2[-1] if stack2 else n
            stack2.append(i)

        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            current_area = heights[i] * width
            max_area = max(max_area, current_area)
            
        return max_area
      
