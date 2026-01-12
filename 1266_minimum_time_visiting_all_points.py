class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(len(points)-1):
            curr_pt = points[i]
            next_pt = points[i+1]

            dx = abs(curr_pt[0]-next_pt[0])
            dy = abs(curr_pt[1]-next_pt[1])

            total += max(dx,dy)
        
        return total
