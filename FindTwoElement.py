from collections import Counter
class Solution:
	def findTwoElement(self,arr, n):
		# if n < 2:
		# 	return 
		# temp_arr = Counter(arr)
		# temp_arr= [k for k, v in temp_arr.items() if v > 1]
		# arr = list(set(sorted(arr)))
		# for i in range(1,n+1):
		# 	if i != arr[i-1]:
		# 		return temp_arr[0], i

		repeat,missing = 0,0
        for i in range(size):
    		if arr[abs(arr[i])-1] > 0:
    			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    		else:
    		    repeat = abs(arr[i])
    			
    	for i in range(size):
    		if arr[i]>0:
    			missing = i+1
    	return [repeat,missing]



s = Solution()
arr=[1,3,3]
print(s.findTwoElement(arr, len(arr)))

arr=[2,2]
print(s.findTwoElement(arr, len(arr)))

arr=[13,33,43,16,25,19,23,31,29,35,10,2,32,11,47,15,34,46,30,26,41,18,5,17,37,39,6,4,20,27,9,3,8,40,24,44,14,36,7,38,12,1,42,12,28,22,45]
print(s.findTwoElement(arr, len(arr)))

arr=[13]
print(s.findTwoElement(arr, len(arr)))