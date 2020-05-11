def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        
        for subset in powerset(arr):
            total_len = sum(len(string) for string in subset)
            num_chars = len(set(chain.from_iterable(subset)))
            
            ans = max(ans, total_len if total_len == num_chars else 0)
            
        return ans
