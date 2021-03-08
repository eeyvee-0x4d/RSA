#!/usr/bin/env python3

# Author Al Vincent Musa
# Python program that uses the RSA agorithm to encrypt or decrypt your super duper secret message

import argparse
import math

from math import sqrt
from itertools import count, islice

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# parses the commanline arguments
def parse_the_args():

	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=f'''
{bcolors.WARNING}
	         ▄              ▄    
	        ▌▒█           ▄▀▒▌   such algorithm
	        ▌▒▒█        ▄▀▒▒▒▐   
	       ▐▄█▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐   
	     ▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐   
	   ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌   
	  ▐▒▒▒▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▌  			much wow
	  ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐  
	 ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌ 
	 ▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌ 
	▌▒▒▒▄██▄▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▐ 		much secure
	▐▒▒▐▄█▄█▌▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
	▐▒▒▐▀▐▀▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▐				so python
	 ▌▒▒▀▄▄▄▄▄▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▌ 
	 ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▒▄▒▒▐  
	  ▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▄▒▒▒▒▌  such application
	    ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀   
	      ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀     
	         ▀▀▀▀▀▀▀▀▀▀▀▀      
{bcolors.OKGREEN}    ____  ____  ________________  _____ ___ 
{bcolors.OKCYAN}   / __ \/ __ \/ ____/ ____/ __ \/ ___//   |
{bcolors.OKBLUE}  / / / / / / / / __/ __/ / /_/ /\__ \/ /| |
{bcolors.HEADER} / /_/ / /_/ / /_/ / /___/ _, _/___/ / ___ |
{bcolors.FAIL}/_____/\____/\____/_____/_/ |_|/____/_/  |_|

{bcolors.WARNING}Top notch military grade encryption algorithm for your super duper ultra mega secret message.{bcolors.ENDC}
'''
	)

	parser.add_argument("-p", help='Set the prime number p', type=int)
	parser.add_argument('-q', help='Set the prime number q', type=int)
	parser.add_argument('-i', '--input', help='Input text')

	args = parser.parse_args()

	p = 1000000000100011 # default values
	q = 1003229774283941 # default values
	
	# If no P argument... ask user for P
	if args.p == None:
		try:
			while True:
				user_input = int(input('Set the value of P: '))
				p = user_input

				if is_prime(p):
					pass
				else:
					print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} P must be a prime number.{bcolors.ENDC}')

				if p > 100000000000000:
					break
				else:
					print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} P must be 15 digits long or more.{bcolors.ENDC}')

		except:
			print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} Invalid input, will use default values...{bcolors.ENDC}')
	else:
		p = args.p

	# If no Q argument... ask the user for Q
	if args.q == None:
		try:
			while True:
				user_input = int(input('Set the value of Q: '))
				q = user_input

				if is_prime(q):
					pass
				else:
					print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} Q must be a prime number.{bcolors.ENDC}')

				if q > 100000000000000:
					break
				else:
					print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} Q must be 15 digits long or more.{bcolors.ENDC}')

		except:
			print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} Invalid input, will use default values{bcolors.ENDC}')
	else:
		q = args.q

	input_text = ''

	# If no input argument... ask the user for input
	if args.input == None:
		input_text = input("Enter the text to encrypt: ")
	else:
		input_text = args.input

	print('\n')

	rsa_go_brrr(p, q, input_text)

# check if two numbers is a coprime
def is_coprime(e, totient_n):

	return math.gcd(e, totient_n) == 1

def is_prime(n):

    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

# do the encryption
def encrypt(plain_text, e, n):

	cipher_text = ""

	for char in plain_text:
		cipher_text += "\\" + str(pow(ord(char), e, n))

	return cipher_text

# do the decryption
def decrypt(cipher_text, d, n):
	
	plain_text = ''
	cipher_chars = list(cipher_text.split('\\'))
	cipher_chars.remove('')

	for char in cipher_chars:
		plain_text += chr(pow(int(char), d, n))

	return plain_text

# Use RSA algorithm
def rsa_go_brrr(p, q, input_text):
	
	n = p * q

	print("P: {0} Q: {1} N: {2}".format(p, q, n))

	totient_n = (p - 1) * (q - 1)

	print("Totient: {0}".format(totient_n))

	e = 0

	while True:
		print("Select e from 1 to {0}: ".format(totient_n))
		e = int(input())

		if e < 1 or e > totient_n:
			print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} e must be in the range of {e} and {totient_n}\n{bcolors.ENDC}')
		elif not is_coprime(e, totient_n):
			print(f'{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}[ERROR]{bcolors.ENDC}{bcolors.WARNING} e must be a coprime with {totient_n}\n{bcolors.ENDC}')
		else:
			break

	# # determine the d
	d = pow(e, -1, totient_n)

	print(f"{bcolors.OKCYAN}Public key:\ne: {e} \n: {n}{bcolors.ENDC}")
	print(f"{bcolors.OKCYAN}Private key:\nd: {d} \n: {n}{bcolors.ENDC}")
	print(f"{bcolors.OKCYAN}Message: {input_text}{bcolors.ENDC}")

	print("Encrypting message...")
	cipher_text = encrypt(input_text, e, n)
	cipher_string = cipher_text.strip('\\')
	print(f"{bcolors.OKGREEN}Cipher text: {cipher_string}{bcolors.ENDC}")

	print("Decrypting message...")
	plain_text = decrypt(cipher_text, d, n)
	print(f"{bcolors.OKGREEN}Plain text: {plain_text}{bcolors.ENDC}")

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