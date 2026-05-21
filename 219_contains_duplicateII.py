from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen={}
    for i,num in enumerate(nums):
        if num in seen and i-seen[num] <= k:
            return True
        seen[num] = i

    return False

containsNearbyDuplicate([1,2,3,1,2,3],2)