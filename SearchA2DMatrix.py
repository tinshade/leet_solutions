class Solution:
	def searchMatrix(self, matrix, target):
		'''
			Binary search implementation
		'''
		rows = len(matrix)
		if not rows:
			return False
		cols = len(matrix[0])
		start,mid,end = 0,0,rows-1
		while start<end:
			#[1,2,3,4,5,6]
			#0+ 5-0/2 = 2 [3 is mid]
			mid = start + (end-start)//2
			#Last column element of middle row
			if matrix[mid][cols-1] < target: 
				start = mid+1 #Move start pointer towards mid
			elif matrix[mid][0] > target:
				end = mid-1 #Move end pointer towards mid
			else:
				start = mid # last element was more than target, first element was less than target #IDEAL
				break
		temp,start = start,0
		end = cols-1
		while start<=end:
			mid = start+(end-start)//2
			if matrix[temp][mid] < target:
				start = mid+1
			elif matrix[temp][mid] > target:
				end = mid-1
			else:
				return True
		return False
			

	def flatten_binary(self,matrix, target):
		'''
			Flatten the matrix into single list, already sorted by definition
		'''
		flat_mat = [num for row in matrix for num in row]
		# binary search
		left, right = 0, len(flat_mat)-1
		while left <= right:
			mid = left + (right - left) //2
			if flat_mat[mid] == target:
				return True
			elif flat_mat[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
				
		return False


	def naive(self, matrix,target):
		'''
			Naive solution
		'''
		for each in matrix:
			if target in matrix:
				return True
		return False




s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s.searchMatrix(matrix, target)) #True
print(s.flatten_binary(matrix, target)) #True
print(s.naive(matrix, target)) #True
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(s.searchMatrix(matrix, target)) #False
print(s.flatten_binary(matrix, target)) #False
print(s.naive(matrix, target)) #False