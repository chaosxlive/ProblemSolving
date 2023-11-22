# https://leetcode.com/problems/seat-reservation-manager/

import heapq


class SeatManager:

    def __init__(self, n: int):
        self.availableSeats = [i for i in range(1, n + 1)]
        heapq.heapify(self.availableSeats)

    def reserve(self) -> int:
        return heapq.heappop(self.availableSeats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.availableSeats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
