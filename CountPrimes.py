class Solution:
	def countPrimes(self, n):
		primes = [True for i in range(n)]
		i = 2
		while(i*i < n):
			if(primes[i] == True):
				for p in range(i*i, n, i):
					primes[p] = False
			i += 1

		counter = 0
		for i in range(2, len(primes)):
			if primes[i]:
				counter += 1
		return counter


s = Solution()
print(s.countPrimes(0)) #0
print(s.countPrimes(1)) #0
print(s.countPrimes(2)) #0
print(s.countPrimes(3)) #1
print(s.countPrimes(10)) #4
print(s.countPrimes(90)) #24
print(s.countPrimes(100)) #25
				

