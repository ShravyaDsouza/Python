from typing import List

def moveZeroes(nums: List[int]) -> List[int]:
    insert_pos = 0

    # Move all non-zero elements to the front
    for x in nums:
        if x != 0:
            nums[insert_pos] = x
            insert_pos += 1

    # Fill the rest with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums

print(moveZeroes([0,0,9,6,2,0,0,1]))