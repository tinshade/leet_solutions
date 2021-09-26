class Solution:
	def rotate(self, arr, k):
		while k!=0:
			temp = arr[0]
			arr[0] = arr[-1]
			for i in range(1, len(arr)):
				temp, arr[i] = arr[i], temp
			k-=1
			self.rotate(arr,k)
		return arr

    def pythonic(self, arr, k):
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]


s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3)) #Not working for huge lists
print(s.pythonic([1,2,3,4,5,6,7], 3)) #Works!
