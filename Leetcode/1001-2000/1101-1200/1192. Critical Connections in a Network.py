# https://leetcode.com/problems/critical-connections-in-a-network/

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.routes = [[] for dot in range(n)]

        for connection in connections:
            self.routes[connection[0]] += [connection[1]]
            self.routes[connection[1]] += [connection[0]]

        self.count = 1
        self.visited = set()
        self.time = {}
        self.lowTime = {}

        self.result = []
        self.tarjan(0, -1)

        return self.result

    def tarjan(self, dot, parent):
        self.visited.add(dot)
        self.time[dot] = self.lowTime[dot] = self.count
        self.count += 1

        for child in self.routes[dot]:
            if child == parent:
                continue
            if child in self.visited:
                self.lowTime[dot] = min(self.lowTime[dot], self.time[child])
            else:
                self.tarjan(child, dot)
                self.lowTime[dot] = min(self.lowTime[dot], self.lowTime[child])
                if self.lowTime[child] > self.time[dot]:
                    self.result.append([dot, child])
