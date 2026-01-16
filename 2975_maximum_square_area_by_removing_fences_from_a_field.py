class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        
        def get_all_distances(fences):
            fences.sort()
            distances = set()
            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    distances.add(fences[j] - fences[i])
            return distances
        
        h_gaps = get_all_distances(hFences)
        v_gaps = get_all_distances(vFences)
        
        max_side = -1
        common_gaps = h_gaps.intersection(v_gaps)
        
        if common_gaps:
            max_side = max(common_gaps)
            
        if max_side == -1:
            return -1
        
        return (max_side * max_side) % (10**9 + 7)
