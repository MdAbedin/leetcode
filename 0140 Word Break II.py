class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        sentences = defaultdict(list)
        sentences[len(s)] = [-1]
        places = deque([len(s)])
        
        for i in range(len(s)-1, -1, -1):
            word = ""
            x = i
            added = False
            
            for j in places:
                word += s[x:j]
                x = j
                
                if word in words:
                    if sentences[j]:
                        if not added: added = True
                        sentences[i].append(j)
            
            if added: places.appendleft(i)
                
        ans = []
        bfs = deque(sentences[0])
        sentence = deque()
        i = 0
        seen = set()
        
        while bfs:
            if bfs[-1] in seen:
                last = sentence.pop()
                if bfs[-1] != len(s): i -= len(last)
                seen.remove(bfs[-1])
                bfs.pop()
                continue
                
            cur = bfs[-1]
            seen.add(cur)
            sentence.append(s[i:cur])
            if cur == len(s):
                ans.append(' '.join(sentence))
            else:
                i = cur
                for start in sentences[cur]:
                    bfs.append(start)
        
        return ans
