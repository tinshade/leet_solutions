class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = str(bin(x)).split('b')[1]
        for each in n:
            if each == '1':
                count += 1
        return count
