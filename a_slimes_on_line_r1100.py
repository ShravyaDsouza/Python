t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    min_val = min(arr)

    ans = (max_val - min_val + 1) // 2

    print(ans)
    t -= 1
