class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        return rev if -(2**31)-1 < rev < 2**31 else 0

solution = Solution()
result = solution.reverse(9)
print(result)
