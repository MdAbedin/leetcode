class StockPrice:

    def __init__(self):
        self.latest_time = -1
        self.latest_price = None
        self.price = {}
        self.min_pq = []
        self.max_pq = []

    def update(self, timestamp: int, price: int) -> None:
        self.price[timestamp] = price
        
        if timestamp >= self.latest_time:
            self.latest_time = timestamp
            self.latest_price = price

        heappush(self.min_pq, [price, timestamp])
        while self.price[self.min_pq[0][1]] != self.min_pq[0][0]:
            heappop(self.min_pq)
            
        heappush(self.max_pq, [-price, timestamp])
        while self.price[self.max_pq[0][1]] != -self.max_pq[0][0]:
            heappop(self.max_pq)

    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        return -self.max_pq[0][0]

    def minimum(self) -> int:
        return self.min_pq[0][0]
