from math import *
class Point():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return sqrt((self.x - point.x) * (self.x - point.x) + (self.y - point.y) * (self.y - point.y))

    def angle_to(self, point):
        #funktionier in 1 von 4 Fällen
        return degrees(atan((self.y - point.y)/(self.x - point.x)))
"""

p = Point(0, 0)
q = Point(1, 1)
print(p.distance_to(q))
print(p.angle_to(q))
"""
