from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    ans = nums
    ans = ans + nums
    return ans

print(getConcatenation([1,3,2,1]))