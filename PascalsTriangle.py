class Solution:
	def generate(self, numRows):
		myList = []
		trow = [1]
		y = [0]
		for x in range(max(numRows,0)):
			myList.append(trow)
			trow=[l+r for l,r in zip(trow+y, y+trow)]
		return myList



s = Solution()
numRows = 6
print(s.generate(numRows))