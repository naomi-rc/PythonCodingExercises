class Matrix:  
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')

    def row(self, index):
        return list(int(value) for value in self.matrix[index-1].split())

    def column(self, index):
        return list(int((value.split())[index-1]) for value in self.matrix)