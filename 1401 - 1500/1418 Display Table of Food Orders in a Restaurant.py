class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        maps = defaultdict(lambda: defaultdict(int))
        
        for order in orders:
            name, table, food = order
            
            foods.add(food)
            maps[int(table)][food] += 1
            
        ans = []
        foods = sorted(list(foods))
        ans.append(["Table"] + foods)
        
        for table in sorted(maps.keys()):
            row = [str(table)] + [str(maps[table][food]) for food in foods]
            ans.append(row)

        return ans
