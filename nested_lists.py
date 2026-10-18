# A nested list is esentially a list  that contain other lists as its elements. 
# This powerful structure allows us to represent complete data,such as grids,tables,
# or matrices within python.

# consider a simple 3*3 matrix.Each inner list represent a row in the matrix.

matrix = [
    [4, 8, 1],
    [9, 7, 2],
    [5, 6, 0]
]

print(matrix[0][0],end=" ")  # output : 4
print(matrix[0][1],end=" ")  # output : 8
print(matrix[0][2],end=" ")  # output : 1
print(matrix[1][0],end=" ")  # output : 9
print(matrix[1][1],end=" ")  # output : 7
print(matrix[1][2],end=" ")  # output : 2
print(matrix[2][0],end=" ")  # output : 5
print(matrix[2][1],end=" ")  # output : 6
print(matrix[2][2])          # output : 0

print(matrix[0])  #Accesing a zero row  '[4, 8, 1]'
print(matrix[1][2]) #Accesing a first row in second column  '2'
print(matrix[2][1]) #Accesing a second row in first column '6'

