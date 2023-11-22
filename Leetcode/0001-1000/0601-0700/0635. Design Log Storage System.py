# https://leetcode.com/problems/design-log-storage-system/

class LogSystem:

    def __init__(self):
        self.container = []

    def put(self, id: int, timestamp: str) -> None:
        self.container.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        scale = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }[granularity]
        startPart = start[:scale]
        endPart = end[:scale]
        return list(map(lambda x: x[0], filter(lambda x: startPart <= x[1][:scale] <= endPart, self.container)))

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
