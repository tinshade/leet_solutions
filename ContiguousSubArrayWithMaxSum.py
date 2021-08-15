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

	def maxSubArraySum(self, arr, size):
		max_till_now = arr[0]
		max_ending = 0
		for i in range(size):
			max_ending = max_ending + arr[i]
			if max_ending < 0:
				max_ending = 0
			elif max_till_now < max_ending:
				max_till_now = max_ending

		return max_till_now




s = Solution()
arr = [1,2,3,-2,5]
n = len(arr)
print(s.kadane(arr, n)) #9

arr = [-1,-2,-3,-4]
n = len(arr)
print(s.kadane(arr, n), s.maxSubArraySum(arr, n))