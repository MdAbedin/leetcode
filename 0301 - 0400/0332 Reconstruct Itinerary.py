class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets,reverse=True): targets[a].append(b)
        
        route = []
        
        def visit(airport):
            while targets[airport]: visit(targets[airport].pop())
            route.append(airport)
            
        visit("JFK")
        
        return route[::-1]
