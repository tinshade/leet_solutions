import functools


class Solution:
    def helper(self, n):
        n = ' '.join(str(n)).split()
        temp = 0
        for each in n:
            temp += int(each) ** 2
        return temp
    def isHappy(self, n: int) -> bool:
        remember = set()
        while self.helper(n) not in remember:
            temp = self.helper(n)
            if temp == 1:
                return True
            remember.add(temp)
            n = temp
        return False

        
        
            