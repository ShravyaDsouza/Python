from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            # No overlap, add new interval
            merged.append([start, end])
        else:
            # Overlap, merge with last interval
            merged[-1][1] = max(merged[-1][1], end)

    return merged
