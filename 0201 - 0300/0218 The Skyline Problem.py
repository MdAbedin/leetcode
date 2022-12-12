class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort()
        endpoints = sorted([[buildings[i][j], i] for i in range(len(buildings)) for j in range(2)])
        ans = []
        pq = []
        cur_height = 0
        
        for x,i in endpoints:
            if x == buildings[i][0]:
                heappush(pq, [-buildings[i][2], buildings[i][1]])
                
            while pq and pq[0][1] <= x:
                heappop(pq)
                
            if not pq:
                if ans[-1][1] != 0:
                    ans.append([x,0])
                    cur_height = 0
            else:
                if -pq[0][0] != cur_height:
                    cur_height = -pq[0][0]
                    
                    if not ans or ans[-1][0] < x:
                        ans.append([x,cur_height])
                    else:
                        if cur_height > ans[-1][1]:
                            if ans[-1][1] == 0 and cur_height == ans[-2][1]:
                                ans.pop()
                            else:
                                ans[-1][1] = cur_height
                                
                                if len(ans) >= 2 and ans[-2][1] == cur_height:
                                    ans.pop()
        return ans
