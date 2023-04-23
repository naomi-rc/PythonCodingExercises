class Matrix:  
    def __init__(self, matrix_string):
        self.matrix = matrix_string.splitlines()
        self.rows = list(list(int(value) for value in row.split()) for row in self.matrix) #[[9 8 7], [5 3 2], [6 6 7]]
        #self.columns = list(list(int((value.split())[index-1]) for value in self.matrix)) #[[9 5 6], [8 3 6], [7 2 7]]
        print(self.matrix)

    def row(self, index):
        #return list(int(value) for value in self.matrix[index-1].split())
        return self.rows[index-1]

    def column(self, index):
        #return list(int((value.split())[index-1]) for value in self.matrix)
        return self.columns[index-1]




matrix_string = "9 8 7 \n 5 3 2 \n 6 6 7"
#matrix = Matrix(matrix_string)
#print(matrix.row(1))

a = [1, 2, 3]
for i, v in enumerate(a):
    print(f"{i} - {v}")