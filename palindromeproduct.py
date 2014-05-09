# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the     # product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

digits = 3
product = 0
palindrome = 0
largestPalindrome = 0
for x in xrange((10 ** (digits - 1)), (10 ** digits)):
	for y in xrange((10 ** (digits - 1)), (10 ** digits)):
		product = x * y
		if str(product) == str(product)[::-1]:
			palindrome = product
			if palindrome> largestPalindrome:
				largestPalindrome = palindrome
print largestPalindrome