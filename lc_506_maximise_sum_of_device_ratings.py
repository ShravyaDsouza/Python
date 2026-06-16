from typing import List


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m = len(units)
        n = len(units[0])

        if m == 1:
            return min(units[0])

        if n == 1:
            return sum(device[0] for device in units)

        for device in units:
            device.sort()

        all_smallest_elements = [device[0] for device in units]
        global_min = min(all_smallest_elements)

        sum_of_second_minm = 0
        for device in units:
            if n > 1:
                sum_of_second_minm += device[1]
            else:
                sum_of_second_minm += 0

        max_r = 0

        for dump_idx in range(m):
            curr_sum = sum_of_second_minm
            if n > 1:
                curr_sum -= units[dump_idx][1]

            dump_device_rating = min(units[dump_idx][0], global_min)

            curr_sum += dump_device_rating

            max_r = max(max_r, curr_sum)

        return max_r