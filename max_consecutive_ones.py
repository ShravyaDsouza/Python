from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_s = 0
    curr_s = 0
    for num in nums:
        if num == 1:
            curr_s += 1
        else:
            if curr_s > max_s:
                max_s = curr_s
            curr_s = 0
    return max(max_s, curr_s)
