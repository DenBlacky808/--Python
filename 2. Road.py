class Road:
    ASF = 25
    LAYERS = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        return self.__length * self.__width * self.ASF * self.LAYERS


new_road = Road(5000, 20)
print(new_road.calc())
