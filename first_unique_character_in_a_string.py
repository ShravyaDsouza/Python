from collections import Counter
def firstUniqChar(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1

input_string = 'leetcode'
print(firstUniqChar(input_string))