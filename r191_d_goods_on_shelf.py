import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))
    out = []

    for _ in range(t):
        n = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]

        unique_sorted = sorted(list(set(a)))
        m = len(unique_sorted)
        val_to_id = {val: i for i, val in enumerate(unique_sorted)}

        a = [val_to_id[x] for x in a]

        cnt = [0] * m
        pos = [[] for _ in range(m)]

        first_idx = a[0]
        cnt[first_idx] += 1
        pos[first_idx].append(0)

        ans = True
        for i in range(1, n):
            if a[i] == a[i - 1]:
                continue

            idx_prev = a[i - 1]
            pos[idx_prev].append(i - 1)
            pos[idx_prev].append(i)

            idx_curr = a[i]
            pos[idx_curr].append(i - 1)
            pos[idx_curr].append(i)

            cnt[idx_curr] += 1
            if cnt[idx_curr] > 3:
                ans = False
                break

        if not ans:
            out.append("NO")
            continue

        found_solution = False
        has_fractured_type = False

        for i in range(n):
            idx = a[i]
            if cnt[idx] <= 1:
                continue

            has_fractured_type = True
            candidates = list(set(pos[idx]))
            num_cand = len(candidates)

            for x_idx in range(num_cand):
                for y_idx in range(x_idx + 1, num_cand):
                    x = candidates[x_idx]
                    y = candidates[y_idx]

                    a[x], a[y] = a[y], a[x]

                    actual_blocks = 1
                    for k in range(1, n):
                        if a[k] != a[k - 1]:
                            actual_blocks += 1

                    if actual_blocks == m:
                        found_solution = True
                        break

                    a[x], a[y] = a[y], a[x]

                if found_solution:
                    break

            if not found_solution:
                ans = False
            break

        if has_fractured_type:
            out.append("YES" if found_solution else "NO")
        else:
            out.append("YES")

    print('\n'.join(out))


if __name__ == '__main__':
    solve()