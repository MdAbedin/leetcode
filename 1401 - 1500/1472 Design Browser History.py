class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.length = 1
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1

        if self.i == len(self.history):
            self.history.append(url)
        else:
            self.history[self.i] = url

        self.length = self.i+1

    def back(self, steps: int) -> str:
        self.i = max(0, self.i-steps)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.length-1, self.i+steps)
        return self.history[self.i]
