class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def backtrack(curr_str:str,idx:int,curr_cost:int,last_was_one:bool):
            if idx==n:
                ans.append(curr_str)
                return

            backtrack(curr_str+'0',idx+1,curr_cost,False)

            if not last_was_one and curr_cost + idx<=k:
                backtrack(curr_str+'1',idx+1, curr_cost+idx ,True)

        backtrack("",0,0,False)
        return ans
