from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    most_common = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = []
    for item, frequency in most_common[:k]:
        result.append(item)
    return result
nums_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k_value = 2
result = topKFrequent(nums_list, k_value)
print(result)