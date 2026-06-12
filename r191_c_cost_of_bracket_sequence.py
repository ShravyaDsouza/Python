import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    s = list(input())
    ans = [0]*n
    while k > 0:
        count = 0
        find = [False, 0]
        for i in range(n):
            if ans[i] == 1:
                continue
            if s[i] == "(":
                count += 1
            if s[i] == ')':
                if count > 0:
                    count -= 1 
                    if count == 0:
                        find[0] = True
                        find[1] = i
                        break
        if find[0] == False:
            can = False
            for i in range(n):
                if ans[i] == 0 and s[i] == '(':
                    can = True
                if k == 0:
                    break
                if ans[i] == 0 and s[i] == ')' and can:
                    ans[i] = 1
                    k -= 1
            break
        else:
            for i in range(find[1]):
                if k == 0:
                    break
                if ans[i] == 0 and s[i] == '(':
                    ans[i] = 1
                    k -= 1

    print("".join(list(map(str, ans))))

