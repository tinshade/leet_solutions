class Solution:
	def cyclicRotateOne(self, arr, n):
		arr.insert(0,arr.pop())
		return arr




s = Solution()
print(s.cyclicRotateOne([1,2,3], 3))