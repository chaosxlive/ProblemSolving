# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big == 0:
                return False
            self.big -= 1
            return True
        if carType == 2:
            if self.medium == 0:
                return False
            self.medium -= 1
            return True
        if carType == 3:
            if self.small == 0:
                return False
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)