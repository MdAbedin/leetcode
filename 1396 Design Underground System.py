class UndergroundSystem:

    def __init__(self):
        self.starts = {}
        self.stats = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starts[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.starts[id]
        self.stats[start_station,stationName][0] += t - start_time
        self.stats[start_station,stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stats[startStation,endStation][0] / self.stats[startStation,endStation][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
