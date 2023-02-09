class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideas = set(ideas)
        counts = defaultdict(Counter)
        ans = 0

        for idea in ideas:
            for letter in ascii_lowercase:
                swapped = letter+idea[1:]

                if swapped not in ideas:
                    ans += 2*counts[letter][idea[0]]
                    counts[idea[0]][letter] += 1

        return ans
