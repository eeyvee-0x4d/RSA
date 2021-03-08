#!/usr/bin/env python3

# Author Al Vincent Musa
# Python program that uses the RSA agorithm to encrypt or decrypt your super duper secret message

import argparse
import math

# parses the commanline arguments
def parse_the_args():

	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description='''
    ____  _____ ___ 
   / __ \/ ___//   |	
  / /_/ /\__ \/ /| |	
 / _, _/___/ / ___ |
/_/ |_|/____/_/  |_|

Top notch military grade encryption algorithm for your super duper ultra mega secret message.
		'''
	)
	group = parser.add_mutually_exclusive_group()

	parser.add_argument("-p", help='Set the prime number p', type=int)
	parser.add_argument('-q', help='Set the prime number q', type=int)
	parser.add_argument('-i', '--input', help='Input text')

	group.add_argument('--encrypt', help='Use encrytion method', action='store_true')
	group.add_argument('--decrypt', help='Use decryption method', action='store_true')

	args = parser.parse_args()
	
	if args.p == None or args.q == None:
		pass
	# elif args.p < 100000000000000 or args.q < 100000000000000:
	# 	print('[ERROR] Minimum value for p and q must be 15 digits.\n Program will exit...')
	# 	exit()

	if args.input == None:
			print('[ERROR] Input is missing. Program will exit...')
			exit()

	p = 17 # default values
	q = 13 # default values
	
	if args.p == None:
		print('[NOTE] No P was provided. Will use default values.')
	else:
		p = args.p

	if args.q == None:
		print('[NOTE] No Q was provided. Will use default values.')
	else:
		q = args.q

	print('\n')

	rsa_go_brrr(p, q, args.input, args.encrypt, args.decrypt)

# check if two numbers is a coprime
def is_coprime(e, totient_n):

	return math.gcd(e, totient_n) == 1
		
# do the encryption
def encrypt(plain_text, e, n):

	cipher_text = ""

	for char in plain_text:
		cipher_text += chr(pow(ord(char), e, n))

	return cipher_text

# do the decryption
def decrypt(cipher_text, d, n):
	
	plain_text = ''

	for char in cipher_text:
		plain_text += chr(pow(ord(char), d, n))

	return plain_text

# Use RSA algorithm
def rsa_go_brrr(p=17, q=13, input_text='', encrypt_flag=False, decrypt_flag=False):
	
	n = p * q

	print("P: {0} Q: {1} N: {2}".format(p, q, n))

	totient_n = (p - 1) * (q - 1)

	print("Totient: {0}".format(totient_n))

	e = 0

	while True:
		print("Select e from 1 to {0}: ".format(totient_n))
		e = int(input())

		if e < 1 or e > 192:
			print("\nERROR: e must be in the range of {} and {}".format(e, totient_n))
		elif not is_coprime(e, totient_n):
			print("\n[ERROR] e must be a coprime with {}".format(totient_n))
		else:
			break

	# # determine the d
	d = pow(e, -1, totient_n)

	print("Public key:\ne: {0} \nn: {1}".format(e, n))
	print("Private key:\nd: {0} \nn: {1}".format(d, n))

	if encrypt_flag:
		cipher_text = encrypt(input_text, e, n)
		print('Encrypting...')
		print('Cipher text: {}'.format(cipher_text))
		print('[NOTE] Some of the characters would be converted into unprintable ASCII characters. \nAs a work around the cipher text will be saved in a cipher.txt file in their escape literal form. \nUse that string as input for decryption.')
		f = open('cipher.txt', 'w', encoding="utf-8")
		f.write(cipher_text)
		f.close()
	elif decrypt_flag:
		plain_text = decrypt(input_text, d, n)
		print('Decrypting...')
		print('Plain text: {}'.format(plain_text))
		f = open('plain.txt', 'w', encoding="utf-8")
		f.write(plain_text)
		f.close()

def main():
	parse_the_args()
		
if __name__ == '__main__':
	main()

#          ▄              ▄    
#         ▌▒█           ▄▀▒▌   
#         ▌▒▒█        ▄▀▒▒▒▐   
#        ▐▄█▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐   
#      ▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐   
#    ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌   
#   ▐▒▒▒▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▌  
#   ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐  
#  ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌ 
#  ▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌ 
# ▌▒▒▒▄██▄▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▐ 
# ▐▒▒▐▄█▄█▌▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
# ▐▒▒▐▀▐▀▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▐ 
#  ▌▒▒▀▄▄▄▄▄▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▌ 
#  ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▒▄▒▒▐  
#   ▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▄▒▒▒▒▌  
#     ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀   
#       ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀     
#          ▀▀▀▀▀▀▀▀▀▀▀▀        