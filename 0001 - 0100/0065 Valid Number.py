class Solution:
    def isNumber(self, s: str) -> bool:
        def is_decimal(s):
            def is_unsigned_decimal(s):
                if (dot_i := s.find(".")) == -1: return False
                before,after = s[:dot_i],s[dot_i+1:]
                return (before or after) and all(map(str.isdigit,before)) and all(map(str.isdigit,after))

            return (s[:1] in "+-" and is_unsigned_decimal(s[1:])) or is_unsigned_decimal(s)

        def is_integer(s):
            return (s[:1] in "+-" and s[1:].isdigit()) or s.isdigit()

        e_i = s.find("e") if "e" in s else s.find("E")

        if e_i == -1:
            return is_decimal(s) or is_integer(s)
        else:
            before,after = s[:e_i],s[e_i+1:]
            return (is_decimal(before) or is_integer(before)) and is_integer(after)
