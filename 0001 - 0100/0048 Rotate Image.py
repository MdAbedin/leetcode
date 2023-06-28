class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)//2):
            for c in range(ceil(len(matrix[0])/2)):
                data = [[r,c,matrix[r][c]], [c,~r,matrix[c][~r]], [~r,~c,matrix[~r][~c]], [~c,r,matrix[~c][r]]]
                for i in range(4): matrix[data[i][0]][data[i][1]] = data[i-1][2]
