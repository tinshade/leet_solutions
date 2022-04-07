class Solution:
    def quick_sort(self, data) -> list:
        if len(data) < 2:
            return data
        
        pivot = data.pop()
        greater : list[int] = [] # Elements greater than pivot 
        lesser : list[int] = [] # Elements lesser than pivot
        for each in data:
            if each > pivot:
                greater.append(each)
            else:
                lesser.append(each)
        
        return self.quick_sort(lesser) + [pivot] + self.quick_sort(greater) # Merging and re-sotring recursively with pivot in the middle
    
    
    def helper(self, stones) -> list:
        if len(stones) > 1:
            if (stones[-1] == stones[-2]):
                del stones[-1]
                del stones[-1]
            elif (stones[-1] > stones[-2]):
                stones[-1] = stones[-1] - stones[-2]
                del stones[-2]
            else:
                stones[-2] = stones[-2] - stones[-1]
                del stones[-1]
        return stones


    def lastStoneWeight(self, stones) -> int:
        try:
            stones = self.quick_sort(stones) # Initial sorting
            while len(stones) > 1:
                stones = self.quick_sort(self.helper(stones))
            return stones[0]
        except IndexError:
            return 0

s = Solution()
print(s.lastStoneWeight([1])) #1
print(s.lastStoneWeight([2,7,4,1,8,1])) #1
print(s.lastStoneWeight([4,8])) #4
print(s.lastStoneWeight([2,2])) #0
print(s.lastStoneWeight([10,4,2,10])) #2