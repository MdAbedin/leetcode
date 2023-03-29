class Solution:

    def maxSatisfaction(self, nums: List[int]) -> int:

        n = sorted((x for x in nums if x < 0),reverse=True)

        nn = sorted(x for x in nums if x >= 0)

        ans = sum((i+1)*num for i,num in enumerate(nn))

        add = sum(nn)

        

        for num in n:

            ans2 = ans + add + num

            

            if ans2 > ans:

                ans = ans2

                add += num

            else:

                break

                

        return ans
