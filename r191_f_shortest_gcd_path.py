import sys
import math


def get_divisors(x):
    divs = set()
    d = 1
    while d * d <= x:
        if x % d == 0:
            divs.add(d)
            divs.add(x // d)
        d += 1
    return sorted(list(divs))


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = int(input_data[1])
    b = int(input_data[2])

    g = math.gcd(a, b)
    a_prime = a // g
    b_prime = b // g

    fa = get_divisors(a_prime)
    fb = get_divisors(b_prime)

    la = len(fa)
    lb = len(fb)
    is_prime_div = {}

    for i, val in enumerate(fa):
        num_divisors = sum(1 for j in range(i) if val % fa[j] == 0)
        is_prime_div[val] = (num_divisors <= 1)

    for i, val in enumerate(fb):
        num_divisors = sum(1 for j in range(i) if val % fb[j] == 0)
        is_prime_div[val] = (num_divisors <= 1)

    ea = [[] for _ in range(la)]
    pa = [[] for _ in range(la)]
    for i in range(la):
        for j in range(i, la):
            if fa[j] % fa[i] == 0:
                ea[i].append(j)
                if is_prime_div.get(fa[j] // fa[i], False):
                    pa[i].append(j)

    eb = [[] for _ in range(lb)]
    pb = [[] for _ in range(lb)]
    for i in range(lb):
        for j in range(i, lb):
            if fb[j] % fb[i] == 0:
                eb[i].append(j)
                if is_prime_div.get(fb[j] // fb[i], False):
                    pb[i].append(j)

    INF = float('inf')
    dp = [[INF] * lb for _ in range(la)]
    dp[0][0] = 0

    for i in range(la):
        for j in range(lb):
            if dp[i][j] == INF:
                continue

            current_cost = dp[i][j]

            for ei in ea[i]:
                for ej in pb[j]:
                    c = fa[ei] // fa[i]
                    d = fb[ej] // fb[j]
                    cost_increase = max(c, d)
                    if current_cost + cost_increase < dp[ei][ej]:
                        dp[ei][ej] = current_cost + cost_increase

            for ei in pa[i]:
                for ej in eb[j]:
                    c = fa[ei] // fa[i]
                    d = fb[ej] // fb[j]
                    cost_increase = max(c, d)
                    if current_cost + cost_increase < dp[ei][ej]:
                        dp[ei][ej] = current_cost + cost_increase

    print(dp[la - 1][lb - 1])


if __name__ == '__main__':
    solve()