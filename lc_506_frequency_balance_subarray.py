class Solution:
    def getLength(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)

        if len(set(nums)) == 1:
            return n

        for start in range(n):
            elem_count = Counter()
            freq_group = Counter()

            for end in range(start,n):
                curr = nums[end]

                prev_freq = elem_count[curr]
                elem_count [curr] +=1
                new_freq = elem_count[curr]

                if prev_freq > 0:
                    freq_group[prev_freq] -=1
                    if freq_group[prev_freq] == 0:
                        del freq_group[prev_freq]

                freq_group[new_freq] +=1
                unq_c = len(elem_count)
                unq_freq_c = len(freq_group)
                curr_len = end - start + 1
                if unq_c == 1 :
                    max_len = max(max_len,curr_len)

                elif unq_freq_c == 2 :
                    freq1 , freq2 = freq_group.keys()
                    low = min(freq1,freq2)
                    high = max(freq1,freq2)

                    if high == 2*low:
                        max_len = max(max_len,curr_len)

        return max_len