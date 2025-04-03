from typing import List

def solve(mat: List[List[int]]) -> List[List[int]] | int:
    missing = []
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                missing.append([i, j])

    def isValid(x, y, val):
        dic = {
            (0, 0): (0, 0), (0, 1): (0, 3), (0, 2): (0, 6),
            (1, 0): (3, 0), (1, 1): (3, 3), (1, 2): (3, 6),
            (2, 0): (6, 0), (2, 1): (6, 3), (2, 2): (6, 6)
        }
        for i in range(9):
            if mat[i][y] == val:
                return False
        for j in range(9):
            if mat[x][j] == val:
                return False
        idx_i, idx_y = x // 3, y // 3
        grid_i, grid_j = dic[(idx_i, idx_y)]
        for i in range(grid_i, grid_i + 3):
            for j in range(grid_j, grid_j + 3):
                if mat[i][j] == val:
                    return False
        return True

    n = len(missing)

    def helper(k):
        if k == n:
            return True
        i, j = missing[k]
        for val in range(1, 10):
            if isValid(i, j, val):
                mat[i][j] = val
                if helper(k + 1):
                    return True
                else:
                    mat[i][j] = 0
        return False

    return mat if helper(0) else -1
