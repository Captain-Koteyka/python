from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ('Red', 'Yellow', 'Green')

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(3)


traffic_light = TrafficLight()
traffic_light.running()
