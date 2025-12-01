from typing import List
def two_sum (nums: List[int], target: int) -> List[int]:
    pair_idx = {}
    for i,num in enumerate(nums):
        if target - num in pair_idx:
            return [i,pair_idx[target-num]]
        pair_idx[num] = i

nums_list = [3, 2, 4]
target_value = 6
result = two_sum(nums_list, target_value)
print(result)