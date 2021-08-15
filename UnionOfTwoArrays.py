class Solution:
	def getUnion(self,a,n,b,m):
		return len(set(a+b))

s = Solution()
a = [1,2,3]
n = len(a)
b = [3,4,5]
m = len(b)

print(s.getUnion(a,n,b,m))