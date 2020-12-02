class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.new_one = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))
        return self.new_one

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


matrix_1 = Matrix([[31, 32], [37, 43], [51, 86]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_1 + matrix_2, '\n')
matrix_3 = Matrix([[1, 2, 3], [3, 4, 3], [5, 6, 3]])
matrix_4 = Matrix([[1, 2, 2], [3, 4, 2], [5, 6, 2]])
print(matrix_3 + matrix_4, '\n')
matrix_5 = Matrix([[1, 2, 4, 3], [5, 6, 3, 5]])
matrix_6 = Matrix([[1, 2, 2, 6], [3, 5, 6, 2]])
print(matrix_5 + matrix_6, '\n')
