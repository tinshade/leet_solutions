class Solution:
	def reshape(self,mat,r,c):
		result=[]
        result_or=[]
        or_r=len(nums)
        or_c=len(nums[0])
        if or_r*or_c!=r*c:
            return nums
        for i in range(or_r):
            for j in range(or_c):
                result_or.append(nums[i][j])
        for i in range(r):
            result_temp=[]
            for j in range(c):
                result_temp.append(result_or.pop(0))
            result.append(result_temp)
        return result


s = Solution()
mat=[[1,2],[3,4]]
r = 2
c = 4
print(s.reshape(mat,r,c))