/*
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

n = 0
num = 1
prime = 0
while n < 6:
	for x in xrange(1, n / 2):
		count = 0
		if n % x == 0:
			count += 1
		if count == 1:
			prime = num
			n += 1
		num += 1
print prime