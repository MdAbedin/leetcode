class Solution:
    def __init__(self):
        self.file = []
        self.i = 0

    def read(self, buf: List[str], n: int) -> int:
        chars_read = len(self.file)-self.i
        buf2 = [None]*4

        while chars_read < n:
            cur_chars_read = read4(buf2)
            self.file += buf2[:cur_chars_read]
            chars_read += cur_chars_read
            if cur_chars_read < 4: break

        buf[:] = self.file[self.i:self.i+n]
        self.i = min(self.i+n,len(self.file))

        return min(chars_read,n)
