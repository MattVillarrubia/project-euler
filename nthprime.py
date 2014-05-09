# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th # prime is 13.
#
# What is the 10 001st prime number?

import time

n = 10001

primeCount = 0	
num = -1
nthPrime = 1

if (n == 1):
	nthPrime = 2

else:
	while (primeCount <  n):
		num += 2
		prime = True
		for x in xrange(2, int(num ** .5) + 1):
			if (num % x == 0):
				prime = False
				break
		if (prime == True):
			primeCount += 1
nthPrime = num
print nthPrime