t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    positive_queue_idx = []
    idx_track = []
    ops = []

    while True:
        positive_queue_idx = []
        idx_track = []
        for i in range(n):
            if arr[i] > 0:
                positive_queue_idx.append(i + 1)
                idx_track.append(0)
            else:
                idx_track.append(1)

        if len(positive_queue_idx) == 0:
            break

        target = positive_queue_idx[-1]
        ops.append(target)

        for j in range(target):
            arr[j] = -arr[j]

    print(len(ops))
    if len(ops) > 0:
        print(*(ops))

    t -= 1