class Solution:
    def read(self, buf, n):
        chars_read = 0
        buf2 = [None]*4

        while chars_read < n:
            cur_chars_read = read4(buf2)
            use = min(n-chars_read,cur_chars_read)
            buf[chars_read:chars_read+use] = buf2[:use]
            chars_read += use
            
            if cur_chars_read < 4: break

        return chars_read
