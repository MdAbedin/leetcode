class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        return " ".join(min([w2 for w2 in dictionary if w.startswith(w2)],default=w,key=len) for w in sentence.split())
