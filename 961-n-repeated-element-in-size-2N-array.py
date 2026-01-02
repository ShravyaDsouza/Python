def repeatedNTimes(self, nums: List[int]) -> int:
    result = set()
    for num in nums :
        if num in result:
            return num
        result.add(num)
nums = [int(x.strip()) for x in user_input.split(",")]
print(f"Result: {repeatedNTimes(nums)}")
