class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def solve(nums,needs):
            if len(nums) == 2*n-1: return nums

            if len(nums) in needs:
                num = needs.pop(len(nums))
                nums.append(num)

                ans = solve(nums,needs)
                if ans != None: return ans
                
                nums.pop()
                needs[len(nums)] = num

                return

            for num in range(n,0,-1):
                if num in nums or (num != 1 and len(nums)+num in needs): continue

                if num != 1: needs[len(nums)+num] = num
                nums.append(num)

                ans = solve(nums,needs)
                if ans != None: return ans
                
                nums.pop()
                if num != 1: needs.pop(len(nums)+num)

        return solve([],{})
