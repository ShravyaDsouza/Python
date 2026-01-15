class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_gap(bars):
            # hint 1:we treat horizontal and vertical bars independent
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            
            # hint 2:find the longest sequence of consecutive integers
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    current_consecutive = 1
                max_consecutive = max(max_consecutive, current_consecutive)
            
            # the gap size is consecutive bars + 1
            return max_consecutive + 1

        # calculate max gap for both dimensions
        max_h = get_max_gap(hBars)
        max_v = get_max_gap(vBars)
        
        # hint 3 & 4:the side of the square is the smaller of the two gaps
        side = min(max_h, max_v)
        return side * side
