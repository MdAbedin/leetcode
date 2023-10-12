class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        m_i = bisect_left(range(1,mountain_arr.length()-1),True,key = lambda i: mountain_arr.get(i) > mountain_arr.get(i+1))+1
        i1 = bisect_left(range(m_i+1),target,key = mountain_arr.get)
        i2 = bisect_left(range(m_i,mountain_arr.length()),-target,key = lambda i: -mountain_arr.get(i))+m_i

        return i1 if mountain_arr.get(i1) == target else (i2 if i2 < mountain_arr.length() and mountain_arr.get(i2) == target else -1)
