
def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for row in range(rows_a):
            for col in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[row][k] * b[k][col]
                result_matrix[row][col] = sum
        return result_matrix
    else:
        print("error! the columns of the first matrix must be equal with the rows of the second matrix")
        return None


if __name__ == "__main__":
    a = [[1,0,0],
        [0,1,0],
        [0,0,1]]
    b = [[1],
        [2],
        [1]]
    e = matrix_multiplication(a,b)
    print(e)