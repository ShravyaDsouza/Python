class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        stack = []
        prev_time = 0

        for log in logs :
            f_id , event , tstamp = log.split(":")
            f_id , tstamp = int(f_id) , int(tstamp)

            if event == "start":
                if stack:
                    ans[stack[-1]] += tstamp - prev_time
                stack.append(f_id)
                prev_time = tstamp
            
            else:
                popped_id = stack.pop()
                ans[popped_id] += tstamp - prev_time + 1
                prev_time = tstamp + 1
                
        return ans
