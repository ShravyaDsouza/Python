from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    num_set = set(nums)
    ans = []

    for i in range(1, len(nums) + 1):
        if i not in num_set:
            ans.append(i)

    return ans
