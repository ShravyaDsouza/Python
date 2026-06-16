import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    output = []

    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx + 1: idx + 1 + n]]
        idx += 1 + n

        valid_segments = [[None] * n for _ in range(n)]

        for i in range(n):
            seen = set()
            min_v = float('inf')
            max_v = float('-inf')
            for j in range(i, n):
                if a[j] in seen:
                    break  # Duplicates are not allowed in consecutive sequences
                seen.add(a[j])

                if a[j] < min_v: min_v = a[j]
                if a[j] > max_v: max_v = a[j]

                # Check consecutive property
                if max_v - min_v == j - i:
                    valid_segments[i][j] = (min_v, max_v)

        max_L = 0

        # Look for two non-overlapping matching segments
        for i in range(n):
            for j in range(i, n):
                if valid_segments[i][j] is None:
                    continue

                min1, max1 = valid_segments[i][j]
                L = j - i + 1

                # We only look for larger lengths than what we've already found
                if L <= max_L:
                    continue

                # Look for a second non-overlapping window of length L
                match_found = False
                for k in range(n - L + 1):
                    m = k + L - 1

                    # Ensure the two segments do not overlap
                    if not (m < i or k > j):
                        continue

                    if valid_segments[k][m] is None:
                        continue

                    min2, max2 = valid_segments[k][m]

                    # Check if they form a single seamless continuous range together
                    if (max1 + 1 == min2) or (max2 + 1 == min1):
                        match_found = True
                        break

                if match_found:
                    max_L = max(max_L, L)

        output.append(str(max_L))

    print('\n'.join(output))


if __name__ == '__main__':
    solve()