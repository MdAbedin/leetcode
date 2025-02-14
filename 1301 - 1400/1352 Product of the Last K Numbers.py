class ProductOfNumbers:
    def __init__(self):
        self.pp = [1]
        self.zeros = [0]

    def add(self, num: int) -> None:
        self.pp.append(self.pp[-1]*(1 if num == 0 else num))
        self.zeros.append(self.zeros[-1]+(num == 0))

    def getProduct(self, k: int) -> int:
        return self.pp[-1] // self.pp[-k-1] if self.zeros[-1]-self.zeros[-k-1] == 0 else 0
