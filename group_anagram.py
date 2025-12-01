from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(input_strings)
print(result)