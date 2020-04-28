class Road:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def asphalt_mass(self, mass_for_sqr_meter, thickness):
        return self.__length * self.__width * mass_for_sqr_meter * thickness


road = Road(20, 5000)
print(road.asphalt_mass(25, 5))
