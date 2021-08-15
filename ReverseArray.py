class Solution:
	def reverseArray(self, arr):
		start, end = 0, len(arr)-1
		if end == 1:
			return arr
		while start < end:
			arr[start], arr[end] = arr[end], arr[start]
			start += 1
			end -= 1
		return arr

s = Solution()
arr = [1,2,3,4,5,6]
print(s.reverseArray(arr))
