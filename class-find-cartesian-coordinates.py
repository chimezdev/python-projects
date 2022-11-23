# Cartesian coordinate system
# write a Python class, 'Point' which stores Cartesian coordinates as float numbers
# the objects of this class should be able to evaluate the dist betw 2 given points on d plane
# use the hypot() mthd-this finds the hypotenus of right-ang triangle imported from math module
# its constructor accepts two arguments (x and y respectively), both default to zero;
# all the properties should be private;
# the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates
# the class provides a method called distance_from_xy(x,y), which calculates and returns the distance 
# between the point stored inside the object and the other point given as a pair of floats;
# the class provides a method called distance_from_point(point), which calculates the distance 
# (like the previous method), but the other point's location is given as another Point class object;
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))