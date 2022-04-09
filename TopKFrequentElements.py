import heapq

class Solution:
    # Solve using Max Heap[k log n]
    def topKFrequentHeap(self, nums, k) -> list:
        counter = dict()
        heap = list()
        results = list()

        #Implementing counter
        for each in nums:
            if each in counter:
                counter[each] +=1
            else:
                counter[each] = 1
        
        # Converting into a tuple and adding to the list
        for key, value in counter.items():
            heap.append((-value, key)) #Max heap with negatives on count
        
        # Making a heap out of the list
        heapq.heapify(heap)

        #Getting the top k elements
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results




    # Bucket Sort with count as indices and list of values as values [O(n)]
    def topKFrequent(self, nums, k) -> list:
        counter = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for each in nums:
            counter[each] = 1 + counter.get(each,0)
        for key,value in counter.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result



s = Solution()
print(s.topKFrequentHeap([1,1,1,2,2,3], 2))
print(s.topKFrequentHeap([1,2], 2))


print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([1,2], 2))
