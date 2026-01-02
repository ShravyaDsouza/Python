from typing import List
def plusOne(digits: List[int]) -> List[int]:
        t = len(digits)-1
        while t>= 0 :
            if digits[t] < 9 :
                digits[t]+=1
                return digits
            digits[t] = 0
            t -=1
        digits.insert(0,1)
        return digits
digits = [int(x) for x in input("Enter numbers: ").split(",")]
print(f"Result: {plusOne(digits)}")
