from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # Sort by squared distance
    points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
    return points[:k]

print(kClosest([[0,0],[2,3],[4,5]],1))