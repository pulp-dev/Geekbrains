import time


class TrafficLight:
    __color = 'red'

    def running(self):
        i = 0
        while i == 0:
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
            print(self.__color)
            time.sleep(5)
            self.__color = 'red'


tl = TrafficLight()
TrafficLight.running(tl)
