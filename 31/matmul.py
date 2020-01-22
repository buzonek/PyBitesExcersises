class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        matrix = [[0 for _ in range(len(other.values[0]))] for _ in range(
            len(self.values))]
        for i in range(len(other.values[0])):
            for j in range(len(self.values)):
                new_value = 0
                for k in range(len(self.values[0])):
                    new_value += self.values[j][k] * other.values[k][i]
                matrix[j][i] = new_value
        return Matrix(matrix)

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        self.values = self.__matmul__(other).values
        return self
