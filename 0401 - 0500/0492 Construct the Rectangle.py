class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return [[area//w,w] for w in range(1,int(sqrt(area))+2) if area%w == 0 and area//w >= w][-1]
