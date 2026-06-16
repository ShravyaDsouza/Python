t = int(input())


def route(val, x , limit):
    paths = {val: 0}
    curr_no = [val]

    for num in curr_no:
        cost = paths[num]

        # move 1: add 1
        if num < limit:
            d0 = num + 1
            if d0 not in paths:
                paths[d0] = cost + 1
                curr_no.append(d0)

        if num == 0:
            continue

        # move 2: divide by x
        d1 = num // x
        if d1 not in paths:
            paths[d1] = cost + 1
            curr_no.append(d1)

        # move 3: add 1, then divide by x
        d2 = (num + 1) // x
        if d2 not in paths:
            paths[d2] = cost + 2
            curr_no.append(d2)

    return paths


while t > 0:
    n = list(map(int, input().split()))
    a = n[0]
    b = n[1]
    x = n[2]

    if a == b:
        print(0)
    else:
        limit = max(a, b)
        from_a = route(a, x, limit)
        from_b = route(b, x, limit)

        op = float('inf')
        for common in from_a:
            if common in from_b:
                total = from_a[common] + from_b[common]
                if total < op:
                    op = total

        print(op)
    t -= 1
