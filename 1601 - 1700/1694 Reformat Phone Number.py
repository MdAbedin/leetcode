class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "")
        number = number.replace("-", "")
        groups = []
        for i in range(0,len(number),3):
            if i == len(number)-4:
                groups.append(number[i:])
                break
            groups.append(number[i:min(i+3,len(number))])
        # print(groups)
        if len(groups[-1]) == 2:
            return "-".join(groups)
        if len(groups[-1]) == 3:
            return "-".join(groups)
        if len(groups[-1]) == 4:
            groups.append(groups[-1][2:])
            groups[-2]=groups[-2][:2]
            return "-".join(groups)
