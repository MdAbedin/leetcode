class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        doubles = ceil(log((Y-1)//X+1,2))

        if doubles == 0:
            return X-Y
        
        diff_bin = bin(X*2**doubles - Y)[2:]
        
        return doubles + diff_bin[-1*doubles:].count('1') + reduce(lambda a,b: a + 2**(len(diff_bin)-b[0]-1-doubles)*int(b[1]), enumerate(diff_bin[:-1*doubles]), 0)
