class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, mid, end = 1,0,n
        while start<=end:
          mid = (end+start)//2
          if isBadVersion(mid):
            #Decide which half
            if isBadVersion(mid-1):
              end = mid-1
            else:
              return mid
          else:
            start = mid+1

s = Solution()
print(s.)