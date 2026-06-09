class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        lowerbound = max(1,n-k)
        upperbound = n+k

        sum = 0
        for i in range(lowerbound,upperbound+1):
            if (n & i) == 0:
                sum+= i

        return sum
