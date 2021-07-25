class Solution:
		def checkIfExist(self, arr):
			for i in range(len(arr)):
				double_find = arr[i]*2
				if double_find in arr and arr.index(double_find) != i:
					return True
			return False




s = Solution()
arr1 = [10,2,5,3]
arr2 = [7,1,14,11]
arr3 = [3,1,7,11]
arr4 = [10,2,5,3]
arr5 = [-2,0,21,10,4,5]
print(s.checkIfExist(arr5))