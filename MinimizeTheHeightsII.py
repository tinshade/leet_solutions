#UNSOLVED
#https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
class Solution:
	def getMinDiff(self, arr, n, k):
		if (n == 1): 
			return 0
		arr.sort()
		ans = arr[-1] - arr[0]
		small = arr[0] + k  
		big = arr[-1] - k    
		if (small > big): 
			small, big = big, small  
	  
		for i in range(1, n-1):
			subtract = arr[i] - k  
			add = arr[i] + k
			if (subtract >= small or add <= big): 
				continue
			if (big - subtract <= add - small): 
				small = subtract  
			else: 
				big = add  
		return min(ans, big - small)









s = Solution()
k, n, arr = 2,4,[1,5,8,10] #5
print(s.getMinDiff(arr, n, k))

k,n,arr = 3,5,[3, 9, 12, 16, 20] #11
print(s.getMinDiff(arr, n, k))

k,n,arr = 5,10,[2,6,3,4,7,2,10,3,2,1] #7
print(s.getMinDiff(arr, n, k))