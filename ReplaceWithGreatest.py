class Solution:
    def replaceElements(self, arr):
      curr_max = -1
      for i in range(len(arr)-1,-1,-1):
        temp_max = max(curr_max, arr[i])
        arr[i] = curr_max
        curr_max = temp_max
      return arr





s = Solution()
arr1 = [17,18,5,4,6,1] #[18,6,6,6,1,-1]
arr2 = [400] #[-1]

print(s.replaceElements(arr1))