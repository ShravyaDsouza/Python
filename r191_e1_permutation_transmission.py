import math
import sys

t = int(input())

while t > 0:
    n = int(input())

    L = 0
    while (1 << L) < (n + 1):
        L += 1

    strs = []
    for _ in range(L):
        strs.append(input())

    counts_with_idx = []
    for i in range(L):
        c = strs[i].count('1')
        counts_with_idx.append((c, i))

    counts_with_idx.sort(key=lambda x: x[0], reverse=True)

    rebuilt_vals = [0] * n
    for bit_position in range(L):
        s_idx = counts_with_idx[bit_position][1]
        s = strs[s_idx]

        for j in range(n):
            if s[j] == '1':
                rebuilt_vals[j] |= (1 << bit_position)

    rebuilt_vals.sort()
    is_permutation_valid = True
    for i in range(n):
        if rebuilt_vals[i] != i + 1:
            is_permutation_valid = False
            break

    if is_permutation_valid:
        freq_of_counts = {}
        for c, _ in counts_with_idx:
            freq_of_counts[c] = freq_of_counts.get(c, 0) + 1

        total_ways = 1
        for count_value, occur in freq_of_counts.items():
            total_ways *= math.factorial(occur)

        print(total_ways)
    else:
        print(0)

    t -= 1
