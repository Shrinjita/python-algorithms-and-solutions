def find_path(matrix, N):
    path = [[0 for _ in range(N)] for _ in range(N)]
    if not find_path_util(matrix, 0, 0, path, N):
        return -1
    return path
def find_path_util(matrix, x, y, path, N):
    if x == N-1 and y == N-1 and matrix[x][y] == 1:
        path[x][y] = 1
        return True
    if is_safe(matrix, x, y, N):
        path[x][y] = 1
        if find_path_util(matrix, x + 1, y, path, N):
            return True 
        if find_path_util(matrix, x, y + 1, path, N):
            return True
        path[x][y] = 0
        return False
    return False
def is_safe(matrix, x, y, N):
    return 0 <= x < N and 0 <= y < N and matrix[x][y] == 1
def main():
    input_data = input().split()
    N = int(input_data[0])
    matrix_elements = list(map(int, input_data[1:]))
    matrix = []
    for i in range(N):
        matrix.append(matrix_elements[i * N:(i + 1) * N])
    result = find_path(matrix, N)
    if result == -1:
        print(result)
    else:
        for row in result:
            print(" ".join(map(str, row)))
if __name__ == "__main__":
    main()
