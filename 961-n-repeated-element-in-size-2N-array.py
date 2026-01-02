from typing import List

def repeatedNTimes(nums: List[int]) -> int:
    result = set()
    for num in nums:
        if num in result:
            return num
        result.add(num)

nums = [int(x) for x in input("Enter numbers: ").split(",")]
print(f"Result: {repeatedNTimes(nums)}")
