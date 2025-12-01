from collections import Counter

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

result1 = is_anagram("listen", "silent")
print(f"'listen' and 'silent': {result1}")

result2 = is_anagram("hello", "world")
print(f"'hello' and 'world': {result2}")

result3 = is_anagram("a", "aa")
print(f"'a' and 'aa': {result3}")

"""
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True
"""