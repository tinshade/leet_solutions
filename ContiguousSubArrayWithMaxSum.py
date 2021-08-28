class Solution:
	def kadane(self, arr, size):
		current, overall = 0, arr[0]
		for i in range(size):
			current += arr[i]
			if overall < current:
				overall = current
			if current < 0:
				current = 0

		return overall




s = Solution()
arr = [1,2,3,-2,5]
n = len(arr)
print(s.kadane(arr, n)) #9


arr = [-2,-1]
n = len(arr)
print(s.kadane(arr, n)) #-1
