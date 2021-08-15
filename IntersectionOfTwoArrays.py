class Solution:
    def intersect(self, nums1, nums2):
        result, intersection = [],{}

        if len(nums2)>len(nums1):
            nums1,nums2 = nums2,nums1  #Ensures nums1 is the larger array
        for i in nums1:
            if i not in intersection:
                intersection[i] = 1
            else:
                intersection[i] += 1
        for i in nums2:
            if i in intersection and intersection[i]:
                intersection[i] -= 1
                result.append(i)
        return result

        
        


nums1, nums2 = [1,2,2,1], [2,2]
s = Solution()
print(s.intersect(nums1, nums2))


nums1, nums2 = [4,9,5], [9,4,9,8,4]
s = Solution()
print(s.intersect(nums1, nums2))

