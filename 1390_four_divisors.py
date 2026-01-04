import math

class Solution:
    def get_divisors_sum(self, n: int):
        # Every number > 1 has at least [1, n] as divisors
        divisors = {1, n}
        
        # Check up to sqrt(n)
        for r in range(2, int(math.sqrt(n)) + 1):
            if n % r == 0:
                divisors.add(r)
                divisors.add(n // r)
                # Optimization: if we exceed 4 divisors, we can stop early
                if len(divisors) > 4:
                    return 0
        
        # Only return the sum if there are exactly 4 unique divisors
        return sum(divisors) if len(divisors) == 4 else 0

    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        for n in nums:
            total_sum += self.get_divisors_sum(n)
        return total_sum
