from math import floor

def rotate_matrix(matrix):
    layer_count = floor(len(matrix)/2)
    matrix_levels = len(matrix)
    for layer in range(layer_count):
        first = layer
        last = matrix_levels - 1 - layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last - offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print (rotate_matrix(input_matrix))