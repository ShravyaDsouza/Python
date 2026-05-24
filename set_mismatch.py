from typing import List


def findErrorNums(self, nums: List[int]) -> List[int]:
    seen = set()
    duplicate, missing = -1, -1
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)

    for i in range(1, len(nums) + 1):
        if i not in seen:
            missing = i

    return [duplicate, missing]
