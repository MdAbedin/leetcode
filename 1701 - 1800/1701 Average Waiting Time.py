class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 1
        s = 0
        
        for a,b in customers:
            s += max(t,a)+b-a
            t = max(t+b,a+b)
            
        return s/len(customers)
