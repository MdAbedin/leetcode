from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(SortedList)
        self.data2 = {}

        for f,c,r in zip(foods,cuisines,ratings):
            self.data[c].add((-r,f))
            self.data2[f] = (r,c)

    def changeRating(self, food: str, newRating: int) -> None:
        r,c = self.data2[food]
        self.data[c].remove((-r,food))
        self.data[c].add((-newRating,food))
        self.data2[food] = (newRating,c)

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]
