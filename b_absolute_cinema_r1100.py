t = int(input())

while t > 0:
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    for i in range(n):
        if arr1[i] > arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]

    a = max(arr1)
    tot = sum(arr2)
    print(a + tot)
    t -= 1
