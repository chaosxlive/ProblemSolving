# https://leetcode.com/problems/design-a-food-rating-system/

from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodItems = {}
        self.foodToCuisine = {}
        self.sortedFoods = defaultdict(lambda: SortedList(key=lambda y: (-y[0], y[1])))

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            item = [rating, food]
            self.foodToCuisine[food] = cuisine
            self.foodItems[food] = item
            self.sortedFoods[cuisine].add(item)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        item = self.foodItems[food]
        self.sortedFoods[cuisine].discard(item)
        item[0] = newRating
        self.sortedFoods[cuisine].add(item)

    def highestRated(self, cuisine: str) -> str:
        return self.sortedFoods[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
