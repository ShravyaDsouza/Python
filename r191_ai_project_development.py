from typing import List

t = int(input())
while t > 0:
    data = input().split()
    n = int(data[0])
    x = int(data[1])
    y = int(data[2])
    z = int(data[3])

    time_no_ai = (n + (x + y) - 1) // (x + y)
    lines_wrt_during_setup = x * z
    if lines_wrt_during_setup >= n:
        time_w_ai = (n + x - 1) // x
    else:
        rem_lines = n - lines_wrt_during_setup
        boosted_speed = 10 * y + x

        additional_hrs = (rem_lines + boosted_speed - 1) // boosted_speed
        time_w_ai = additional_hrs + z

    print(min(time_no_ai, time_w_ai))
    t -= 1
