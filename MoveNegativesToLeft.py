class Solution:
	def moveToLeft(self,arr,n):
		left = 0
		right = n-1

		while left <= right:
			if arr[right] < 0 and arr[left] > 0:
				arr[right],arr[left] = arr[left],arr[right]
				right -= 1
				left += 1
			elif arr[right] < 0 and arr[left] < 0:
				left+=1
			elif arr[right] > 0 and arr[left] > 0:
				right-=1
			else:
				left += 1
				right -= 1

		return arr



s = Solution()
arr = [-12, 11,-13, -5, 6, -7, 5, -3, 11]
n = len(arr)

print(s.moveToLeft(arr,n))

