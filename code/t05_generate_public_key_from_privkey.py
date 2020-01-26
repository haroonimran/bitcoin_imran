#example 4-5
##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
##############################################################################################

import bitcoin             #Using library funtions to generate private keys the "easy" way.
import base58              #to encode Private key to base58
import binascii            #using binascii.unhexlify()
from hashlib import sha256
import ecdsa
import os

#STEP 1. #########  GENERATE PRIVATE KEY ############

#Generate a new 32bit random key using the OS's CSPRNG:
private_key_bytes = os.urandom(32)
private_key_hex = private_key_bytes.hex()
private_key_int = int(private_key_hex,16)
print("Private key Bytes =", private_key_bytes)
private_key_hex = private_key_bytes.hex()
print("Private key Hex",private_key_hex)

#compressed Private key
private_key_temp = '80'+private_key_hex
sha1 = sha256(binascii.unhexlify(private_key_temp)).hexdigest()
sha2 = sha256(binascii.unhexlify(sha1)).hexdigest()
first4 = sha2[0:8]
print("first 4 =",first4)

private_key_w_checksum_uncmp = private_key_temp+first4
print("private_key_temp_checksum =",private_key_w_checksum_uncmp)

private_key_uncmp_int = int(private_key_w_checksum_uncmp,16)

#base58check
private_uncompressed = base58.b58encode_int(private_key_uncmp_int)
print("private key uncompressed:",private_uncompressed)


#uncompressed Private key
private_key_w_checksum_cmp = private_key_temp+'01'+first4
private_key_cmp_int = int(private_key_w_checksum_cmp,16)
private_compressed = base58.b58encode_int(private_key_cmp_int)
print("private key compressed:",private_compressed)



# STEP 2: #######    GENERATE PUBLIC KEY    ########
# As bitcoin used the elliptic curve secp256k12.4.1 # The following is excerpted from the standards document at the website below.
"""
Recommended Parameters secp256k1 http://www.oid-info.com/get/1.3.132.0.10
The elliptic curve domain parameters over F p associated with a Koblitz curve secp256k1 are
specified by the sextuple T = (p, a, b, G, n, h) where the finite field F p is defined by:
"""
#p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F
#p = 2^256 − 2^32 − 2^9 − 2^8 − 2^7 − 2^6 − 2^4 − 1
#The curve E: y 2 = x 3 + ax + b over Fp is defined by:
#a = 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
#b = 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000007

#The base point G in compressed form is:
#G = 02 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798 

#and in uncompressed form is:
#G = 04 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798 
#       483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8

#Finally the order n of G and the cofactor are:
#n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141
#h = 01 """

# Set up variables for ECDSA calculation:
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# Define new secp256k1 curve:
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p,_a,_b)

# Set generator point:
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1,_Gx,_Gy,_r)
print("generator_secp256k1",generator_secp256k1)
point = generator_secp256k1 * private_key_bytes
print(point)