#!/usr/bin/env python3

import argparse
import math

# check if two numbers is a coprime
def is_coprime(e, totient_n):

	if math.gcd(e, totient_n) == 1:
		return True
	else:
		return False


def main():

	p = 13
	q = 17
	n = p * q

	totient_n = (p - 1) * (q - 1)

	e = 0

	while(e < 1  or e > totient_n and is_coprime(e, totient_n)):
		print("Select e from 1 to {0}: ".format(totient_n))
		e = int(input())
		
if __name__ == '__main__':
	main()
