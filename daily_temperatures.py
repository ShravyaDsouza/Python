class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_d_idx = stack.pop()
                ans[prev_d_idx] = i - prev_d_idx
            stack.append(i)
        return ans 
