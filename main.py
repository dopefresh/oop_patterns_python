class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    def __checkValue(x):
        return isinstance(x, int) or isinstance(x, float)

    def __setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
    
    def __getCoords(self):
        return self.__x, self.__y
    
    def __getCoordX(self):
        return self.__x

    def __setCoordX(self, x):
        self.__x = x

    coordX = property(__getCoordX, __setCoordX)

pt = Point(1, 2)
pt.coordX = 100
print(5 - pt.coordX)
