import sys

t = int(input())

for _ in range(t):
    line = input().strip()
    while not line:
        line = input().strip()
    n = int(line)

    b1 = list(range(1, n + 1))

    b2 = list(range(1, n + 1))

    b3 = [n] + list(range(1, n))

    b4 = list(range(1, n + 1))

    ans = b1 + b2 + b3 + b4

    print(*(ans))