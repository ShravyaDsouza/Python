from typing import List


def missingNumber(nums: List[int]) -> int:
    ans = len(nums)
    for i in range(len(nums)):
        ans += i - nums[i]

    return ans


print(missingNumber([3, 0, 1]))
