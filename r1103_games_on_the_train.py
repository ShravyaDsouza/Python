t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))

    max_h = max(a)
    min_h = min(a)

    k = max_h + 1 - min_h
    print(k)
    t -= 1