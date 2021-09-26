data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

another_data = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        for i in self.data:
            print(*i)

    def __add__(self, other):
        new_data = []
        new_line = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                new_line.append(self.data[i][j] + other.data[i][j])
            new_data.append(new_line)
            new_line = []
        new_matrix = Matrix(new_data)
        return new_matrix


matrix_1 = Matrix(data)
matrix_2 = Matrix(another_data)
print((matrix_1 + matrix_2).__str__())
