class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("N")
        ans = (penalty,len(customers))

        for i in range(len(customers)-1,-1,-1):
            penalty += 1 if customers[i] == "Y" else -1
            ans = min(ans,(penalty,i))

        return ans[1]
