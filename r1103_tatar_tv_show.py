t = int(input())

while t > 0:
    ip = list(map(int, input().split()))
    n = ip[0]
    k = ip[1]

    str = input()

    bin = [0] * k

    for i in range(n):
        if str[i] == '1':
            bin[i % k] += 1

    flag = True

    for cnt in bin:
        if cnt % 2 != 0:
            flag = False
            break

    if flag == True:
        print("Yes")
    else:
        print("No")
    t -= 1
