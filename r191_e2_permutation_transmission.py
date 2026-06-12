import sys
import math


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))
    out = []

    for _ in range(t):
        n = int(next(iterator))

        l = 0
        while (1 << l) < (n + 1):
            l += 1

        strings = [next(iterator) for _ in range(l)]

        counts_with_idx = [(strings[i].count('1'), i) for i in range(l)]

        counts_with_idx.sort(key=lambda x: x[0], reverse=True)

        ordered_strings = [strings[x[1]] for x in counts_with_idx]

        rebuilt_columns = list(zip(*ordered_strings))

        rebuilt_ints = []
        for col in rebuilt_columns:
            val = 0
            for bit_pos, char in enumerate(col):
                if char == '1':
                    val |= (1 << bit_pos)
            rebuilt_ints.append(val)

        rebuilt_ints.sort()

        is_permutation_valid = True
        for i in range(n):
            if rebuilt_ints[i] != i + 1:
                is_permutation_valid = False
                break

        if is_permutation_valid:
            freq_of_counts = {}
            for c, _ in counts_with_idx:
                freq_of_counts[c] = freq_of_counts.get(c, 0) + 1

            total_ways = 1
            for count_value, occurrences in freq_of_counts.items():
                total_ways *= math.factorial(occurrences)

            out.append(str(total_ways))
        else:
            out.append("0")

    print('\n'.join(out))


if __name__ == '__main__':
    solve()