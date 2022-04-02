class Solution:
	def countOdds(self, low, high) -> int:
		if (low % 2 == 0 and high % 2 == 0):
			return (high - low) // 2
		else:
			return ((high - low) // 2) + 1



s = Solution()
print(s.countOdds(0,10))