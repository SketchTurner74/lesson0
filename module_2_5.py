# "Матрица воплоти"
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            row.append(value)
    return matrix


result_1 = get_matrix(3, 4, 14)
result_2 = get_matrix(6, 2, 9)
result_3 = get_matrix(7, 4, 42)
print(result_1)
print(result_2)
print(result_3)