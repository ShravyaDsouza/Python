from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    ans = []
    sorted_nums = sorted(nums)
    num_to_count = {}
    for idx, num in enumerate(sorted_nums):
        if num not in num_to_count:
            num_to_count[num] = idx

    for num in nums:
        ans.append(num_to_count[num])

    return ans
