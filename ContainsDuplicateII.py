class Solution:
    def containsNearybyDuplicate(self, nums, k:int) -> bool:
        hashmap = dict()
        for index, value in enumerate(nums):
            if value in hashmap and (index-hashmap[value]) <= k:
                return True
            hashmap[value] = index
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearybyDuplicate([1,2,3,1], 3)) # True
    print(s.containsNearybyDuplicate([1,0,1,1], 1)) # True
    print(s.containsNearybyDuplicate([1,2,3,1,2,3], 2)) # False

