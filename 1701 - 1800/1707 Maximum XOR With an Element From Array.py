class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        ans = []
        
        for x,m in queries:
            xb = bin(x)[2:]
            xb = "0"*(40-len(xb)) + xb 
            l,r = 0,bisect_right(nums,m)-1
            if r < 0:
                ans.append(-1)
                continue
            
            rb = bin(nums[r])[2:]
            rb = "0"*(40-len(rb)) + rb 
            i = bin(nums[r])[2:].find("1")
            cur = 0
            
            while r-l > 0 and i < 40:
                if xb[i]=="1":
                    new_r = bisect_right(nums, cur+2**(40-i-1)-1, l, r+1)-1
                    if new_r >= l:
                        r = new_r
                    else:
                        cur += 2**(40-i-1)
                else:
                    new_l = bisect_left(nums, cur+2**(40-i-1), l, r+1)
                    if new_l <= r:
                        l = new_l
                        cur += 2**(40-i-1)
                
                i += 1
            
            ans.append(x^nums[r])
            
        return ans
