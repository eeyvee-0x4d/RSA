#!/usr/bin/env python3

import argparse
import math

# check if two numbers is a coprime
def is_coprime(e, totient_n):

	if math.gcd(e, totient_n) == 1:
		return True
	else:
		return False

def encrypt(plain_text='Hello World', e=7, n=221):

	cipher_text = ""
	string = []

	for char in plain_text:
		# cipher_text += chr(pow(ord(char), e, n))
		string.append(chr(pow(ord(char), e, n)))
		
	cipher_text.join(string)
	print(string)
	print(cipher_text)

def main():

	p = 17
	q = 13
	n = p * q

	print("P: {0} Q: {1} N: {2}".format(p, q, n))

	totient_n = (p - 1) * (q - 1)

	print("Totient: {0}".format(totient_n))

	e = 0

	# ask user unti right input
	while(e < 1  or e > totient_n and is_coprime(e, totient_n)):
		print("Select e from 1 to {0}: ".format(totient_n))
		e = int(input())

	# determine the d
	d = pow(e, -1, totient_n)

	print("Public key:\ne: {0} \nn: {1}".format(e, n))
	print("Private key:\nd: {0} \nn: {1}".format(d, n))

	encrypt('Hello World!', e, n)

		
if __name__ == '__main__':
	main()
