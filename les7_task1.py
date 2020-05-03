class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_list]))

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix_list)):
            new_line = []
            for j in range(len(self.matrix_list[i])):
                new_line.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            new_matrix.append(new_line)
        return new_matrix
        #return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_matrix]))


matrix1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 5]])
matrix2 = Matrix([[3, 7, 0], [40, 50, 60], [0, 0, 1]])
print(matrix1.__str__())
print(matrix2.__str__())
print(matrix1 + matrix2)
