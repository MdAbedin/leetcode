class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        for word in words:
            if not lines or lines[-1][1]+len(word)+1 > maxWidth:
                lines.append([[word],len(word)])
            else:
                lines[-1][0].append(word)
                lines[-1][1] += len(word)+1

        ans = []

        for words,_ in lines[:-1]:
            if len(words) == 1:
                ans.append(words[0].ljust(maxWidth," "))
            else:
                length = sum(map(len,words))
                line = []

                for i in range(len(words)-1):
                    line.append(words[i])
                    line.append(" "*((maxWidth - length)//(len(words)-1) + (1 if i < (maxWidth - length) % (len(words)-1) else 0)))

                line.append(words[-1])
                ans.append("".join(line))

        ans.append(" ".join(lines[-1][0]).ljust(maxWidth," "))

        return ans
