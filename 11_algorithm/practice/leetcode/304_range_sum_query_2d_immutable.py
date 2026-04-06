from typing import List


# class NumMatrix:
#
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         res = 0
#         for i in range(row1, row2 + 1):
#             for j in range(col1, col2 + 1):
#                 res += self.matrix[i][j]
#         return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_length = len(matrix)
        col_length = len(matrix[0])
        if not row_length or not col_length:
            return
        self.pre_matrix = [[0] * (col_length + 1) for _ in range(row_length + 1)]
        for i in range(1, row_length + 1):
            for j in range(1, col_length + 1):
                self.pre_matrix[i][j] = self.pre_matrix[i - 1][j] + self.pre_matrix[i][j - 1] + \
                                        matrix[i - 1][j - 1] - self.pre_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_matrix[row2 + 1][col2 + 1] - self.pre_matrix[row1][col2 + 1] - \
               self.pre_matrix[row2 + 1][col1] + self.pre_matrix[row1][col1]


if __name__ == '__main__':
    # ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    # [[[[-4, -5]]], [0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 1]]
    matrix = NumMatrix([[-4, -5]])
    print(matrix.sumRegion(*[0, 0, 0, 0]))
