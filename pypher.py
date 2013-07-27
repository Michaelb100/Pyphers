from crypto.ciphers import *

### -EXAMPLE USAGE- ###

# Encrypting a message:
enc = Vigenere.encrypt("Hello, world! This is encrypted!", "pypher")

# Decrypting a message:
dec = Vigenere.decrypt(enc, "pypher")

print("Encrypted:", enc)
print("Decrypted:", dec)