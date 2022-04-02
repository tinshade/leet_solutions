class Solution:
    def average(self, salary):
        return float((sum(salary) - (max(salary)+min(salary)))/(len(salary)-2))



s = Solution()
salary = [4000,3000,1000,2000]
print(s.average(salary))