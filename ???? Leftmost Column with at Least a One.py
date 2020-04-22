# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        num_rows, num_cols = binaryMatrix.dimensions()
        ans_y, ans_x = 0, num_cols-1

        while ans_x >= 0 and ans_y <= num_rows-1:
            if binaryMatrix.get(ans_y, ans_x):
                ans_x -= 1
            else:
                ans_y += 1
                
        return -1 if ans_x == num_cols-1 else ans_x+1
