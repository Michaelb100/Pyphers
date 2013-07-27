global alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Cipher(object):
	"""Superclass for all ciphers."""
	
	@staticmethod
	def encrypt(self, data, key):
		"""Encrypts the string data based on a given key and
		returns the encrypted data as a string.
		"""
		data = str(data).upper()
		key = str(key).upper()
	
	@staticmethod
	def decrypt(self, data, key):
		"""Decrypts the string data based on a given key and
		returns the decrypted data as a string.
		"""
		data = str(data)
		key = str(key)
		
	def __str__(self):
		return "Cipher: %s" % self.__class__.__name__
	
	__repr__ = __str__



class Caesar(Cipher):
	"""A class capable of encrypting and decrypting
	data using the Caesar cipher.
	"""
	
	@staticmethod
	def encrypt(self, data, key):
		"""Encrypts data using the Caesar cipher."""
		data = str(data).upper()
		key = int(key) % 26
		encrypted = ""
		
		for char in data:
			if not char in alphabet:
				encrypted += char
			else: 
				encrypted += alphabet[(alphabet.index(char) + key) % 26]
		return encrypted
	
	@staticmethod
	def decrypt(self, data, key):
		"""Decrypts data encrypted with the Caesar cipher."""
		data = str(data).upper()
		key = int(key) % 26
		decrypted = ""
		
		for char in data:
			if not char in alphabet:
				decrypted += char
			else:
				decrypted += alphabet[(alphabet.index(char) - key) % 26]
		return decrypted
	


class Vigenere(Cipher):
	"""A class capable of encrypting and decrypting
	data using the Vigenere cipher.
	"""
	
	@staticmethod
	def encrypt(data, key):
		data = data.upper()
		key = key.upper()
		encrypted = ""
		key_marker = 0
		
		for char in data:
			if char not in alphabet or not key[key_marker] in alphabet:
				encrypted += char
			else: 
				encrypted += alphabet[(alphabet.index(key[key_marker])
										+ alphabet.index(char)) % len(alphabet)]
			key_marker += 1
			key_marker %= len(key)
		
		return encrypted
	
	@staticmethod
	def decrypt(data, key):
		data = data.upper()
		key = key.upper()
		decrypted = ""
		
		key_marker = 0
		for char in data:
			if char not in alphabet or not key[key_marker] in alphabet:
				decrypted += char
			else:
				decrypted += alphabet[(alphabet.index(char)
										- alphabet.index(key[key_marker])) % len(alphabet)]
			key_marker += 1
			key_marker %= len(key)
		
		return decrypted
