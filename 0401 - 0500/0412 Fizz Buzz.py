class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if num%3 == num%5 == 0 else ("Fizz" if num%3 == 0 else ("Buzz" if num%5 == 0 else str(num))) for num in range(1,n+1)]
