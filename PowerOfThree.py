class Solution:
		def isPowerOfThree(self, n: int) -> bool:
			res,i=0,0
			while True:
				res = 3**i
				if res <= n:
					if res == n:
						return True
					i+=1
				else:
					return False