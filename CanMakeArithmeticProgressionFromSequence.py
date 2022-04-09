class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        for i in range(1,len(arr)-1):
            if (arr[i]-arr[i-1]) != (arr[i+1] - arr[i]):
                return False
        return True

s = Solution()
print(s.canMakeArithmeticProgression([3,5,1]))
print(s.canMakeArithmeticProgression([1,4,2]))
print(s.canMakeArithmeticProgression([0,0,1]))
        