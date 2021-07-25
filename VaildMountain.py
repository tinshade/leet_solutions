class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        is_downhill = False
        if n<3:
          return False
        for i in range(1,n):
          if arr[i-1]<arr[i]:
            pass
          elif arr[i-1] == arr[i]:
            return False
          elif arr[i-1]>arr[i] and i!=1:
            is_downhill = True
            for j in range(i+1,n):
              if arr[j-1]>arr[j]:
                pass
              else:
                return False
          else:
            return False
        if is_downhill:
          return True
        return False




s = Solution()

arr1 = [2,1]
arr2 = [3,5,5]
arr3 = [0,3,2,1]
arr4 = [2,0,2]
arr5 = [0,1,2,1,2]
arr6 = [0,2,3,4,5,3,2,1,0]
arr7 = [0,1,2,3,4,5,6,7,8,9]
arr8 = [9,8,7,6,5,4,3,2,1,0]

print(s.validMountainArray(arr8))
