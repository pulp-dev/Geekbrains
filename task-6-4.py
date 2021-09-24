from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def turn(self, direction):
        print(self.name, f'поварачивает {direction}')

    def stop(self):
        print(self.name, 'остановился')

    def go(self):
        print(self.name, 'едет')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('High speed!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('High speed!!!')


class PoliceCar(Car):
    pass


car_1 = TownCar(70, 'blue', 'Ford', False)
car_2 = SportCar(300, 'red', 'ferrari', False)
car_3 = WorkCar(40, 'yellow', 'kamaz', False)
car_4 = PoliceCar(150, 'white', 'skoda', True)

cars = [car_4, car_3, car_2, car_1]
ways = ['направо', "налево"]

for i in cars:
    i.go()
    i.show_speed()
    i.turn(ways[randint(0, 1)])
    i.stop()