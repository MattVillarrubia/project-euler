# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10     # without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from # 1 to 20?

smallMult = 1
for i in range(1, 21):
	smallMult = smallMult * i
for j in range(1, 21):
	if smallMult % (j ** 2) == 0:
		smallMult = smallMult / j
print smallMult