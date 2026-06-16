class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0

        digits = list(map(int, str(n)))

        for i, d in enumerate(digits):
            digitSum += d
            squareSum += d ** 2

        return (squareSum - digitSum >= 50)