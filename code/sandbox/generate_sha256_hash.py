import hashlib
from bitcoin.core import *
print("Enter string to encode:")
inputString = input().encode('utf-8')
hash_result = hashlib.sha256(inputString).digest()
print("The hash of the value entered is:",b2x(hash_result))
