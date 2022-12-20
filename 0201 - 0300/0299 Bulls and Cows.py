class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(c1==c2 for c1,c2 in zip(secret,guess))
        secret_non_bulls = [c1 for c1,c2 in zip(secret,guess) if c1!=c2]
        guess_non_bulls = [c2 for c1,c2 in zip(secret,guess) if c1!=c2]
        cows = 0

        for c in guess_non_bulls:
            if c in secret_non_bulls:
                cows += 1
                secret_non_bulls.remove(c)

        return f"{bulls}A{cows}B"
