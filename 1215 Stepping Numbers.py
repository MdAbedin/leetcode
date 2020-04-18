class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ans = []
        num_digits = len(str(high))
        
        for i in range(10):
            state = deque()
            cur_num = 0

            state.append([i, 0, False if i == 0 else True])
            cur_num += i * 10**(num_digits-1)
            
            while state:
                if cur_num > high:
                    cur_digit, *_ = state[-1]
                    cur_num -= cur_digit * 10**(num_digits - len(state))
                    state.pop()
                    continue
                if len(state) == num_digits:
                    if cur_num >= low:
                        ans.append(cur_num)
                    cur_digit, *_ = state[-1]
                    cur_num -= cur_digit * 10**(num_digits - len(state))
                    state.pop()
                    continue
                    
                cur_digit, step, is_started = state[-1]
                next_digit = 0
                
                if cur_digit == 0:
                    if step == 10 or (step == 1 and is_started):
                        state.pop()
                        continue
                    
                    next_digit = step if not is_started else 1
                else:
                    if step == 2 or (cur_digit == 9 and step == 1):
                        cur_num -= cur_digit * 10**(num_digits - len(state))
                        state.pop()
                        continue
                    
                    next_digit = cur_digit-1 if step == 0 else cur_digit+1
                
                state[-1][1] += 1
                state.append([next_digit, 0, is_started or next_digit != 0])
                cur_num += next_digit * 10**(num_digits - len(state))
        
        return ans
