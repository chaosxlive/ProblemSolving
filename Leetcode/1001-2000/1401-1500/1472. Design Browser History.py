# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        self.latest = 0

    def visit(self, url: str) -> None:
        self.current += 1
        if self.current == len(self.history):
            self.history.append(url)
        else:
            self.history[self.current] = url
        self.latest = self.current

    def back(self, steps: int) -> str:
        temp = max(0, self.current - steps)
        self.current = temp
        return self.history[temp]

    def forward(self, steps: int) -> str:
        temp = min(self.latest, self.current + steps)
        self.current = temp
        return self.history[temp]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
