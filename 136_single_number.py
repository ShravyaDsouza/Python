def singleNumber(nums)->[int]:
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber([22,1,22,4,1]))