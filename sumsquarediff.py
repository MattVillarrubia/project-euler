/*
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

sumsquare = 1
squaresum = 1
diff = 0
for x in range(2, 101):
	sumsquare += (x ** 2)
	squaresum += x
diff = (squaresum ** 2) - sumsquare
print diff