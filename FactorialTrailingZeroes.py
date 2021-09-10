class Solution:
    def trailingZeroes(self, n: int) -> int:
      count = 0
      while n >= 5:
        n//=5
        count += n
        print(n, count)
      return count



s = Solution()
print(s.trailingZeroes(1000)) #249