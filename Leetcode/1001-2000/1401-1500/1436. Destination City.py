# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination = set()
        visited = set()

        for path in paths:
            if path[0] in destination:
                destination.remove(path[0])
            visited.add(path[0])
            if path[1] not in visited:
                destination.add(path[1])
        
        return list(destination)[0]