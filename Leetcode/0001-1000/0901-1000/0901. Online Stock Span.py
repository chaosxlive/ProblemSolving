# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        ptr = len(self.stocks) - 1
        while ptr >= 0 and self.stocks[ptr][0] <= price:
            ptr -= self.stocks[ptr][1]
        self.stocks.append((price, len(self.stocks) - ptr))
        return self.stocks[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
