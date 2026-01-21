class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue

            for i in range(31):
                if ((n >> i) & 1) == 1 and ((n >> (i + 1)) & 1) == 0:
                    ans.append(n ^ (1 << i))
                    break
        return ans
