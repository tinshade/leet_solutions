class Solution:
    def maximumCount(self, nums) -> int:
        pos, neg = 0, 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                neg += 1
        
        return max(pos,neg)




if __name__ == "__main__":
    s=Solution()
    print(s.maximumCount([-2,-1,-1,1,2,3])) # 3
    print(s.maximumCount([-3,-2,-1,0,0,1,2])) # 3
    print(s.maximumCount([5,20,66,1314])) # 4