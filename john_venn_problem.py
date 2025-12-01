def venn_intersection(a, b):
    # Sort input lists
    a.sort()
    b.sort()

    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            # Avoid duplicates in result
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    if not result:
        return "NULL"
    return " ".join(str(x) for x in result)


def main():
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(venn_intersection(x, y))


if __name__ == "__main__":
    main()
