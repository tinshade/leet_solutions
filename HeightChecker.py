class Solution:
    def heightChecker(self, heights):
        if len(heights)<=1:
            return 0
        results = 0
        unsorted_heights = heights
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if unsorted_heights[i] != sorted_heights[i]:
                results += 1
        return results






s = Solution()
arr1 = [1,1,4,2,1,3] #3
arr2 = [5,1,2,3,4] #5
arr3 = [1,2,3,4,5] #0

print(s.heightChecker(arr3))