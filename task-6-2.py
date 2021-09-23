class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_weigh(self, mass, thinnest):
        return self.length * self.width * mass * thinnest


road_1 = Road(20, 5000)
print(road_1.get_weigh(25, 5), 'kg')