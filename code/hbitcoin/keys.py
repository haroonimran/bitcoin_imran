#example 4-5
##############################################################################################
# HAROON IMRAN
# haroon.imran@gmail.com
##############################################################################################

import base58              #to encode Private key to base58
import binascii            #using binascii.unhexlify()
from hashlib import sha256
import hashlib
import hbitcoin
import os
import hbitcoin.ecch

class KeyTriplet:

    def __init__(self):
        self.compressed = 0
        self.uncompressed = 0
        self.intkey = 0
        return


def PrivateKey():

    new_private_key = KeyTriplet()

#STEP 1. #########  GENERATE PRIVATE KEY ############

#Generate a new 32bit random key using the OS's CSPRNG:
    private_key_bytes = os.urandom(32)
    private_key_hex = private_key_bytes.hex()
    #private_key_hex = '8B7C0FCC173893EB11B15BC0015C6CABD485DAB72E2FE52E48F406406C2871FE'

    private_key_int = int(private_key_hex,16)
    #print("Private key Bytes =", private_key_bytes)
    private_key_hex = private_key_bytes.hex()
    #print("Private key Hex",private_key_hex)

    #compressed Private key
    private_key_uncomp = '80'+private_key_hex
    sha1 = sha256(binascii.unhexlify(private_key_uncomp)).hexdigest()
    sha2 = sha256(binascii.unhexlify(sha1)).hexdigest()
    first4 = sha2[0:8]
    print("first 4 =",first4)

    private_key_w_checksum_uncmp = private_key_uncomp+first4
    #print("private_key_temp_checksum =",private_key_w_checksum_uncmp)

    private_key_uncmp_int = int(private_key_w_checksum_uncmp,16)

    #base58check
    private_uncompressed = base58.b58encode_int(private_key_uncmp_int)
    #print("private key uncompressed:",private_uncompressed)


    #uncompressed Private key
    private_key_cmp = '80'+private_key_hex+'01'
    sha1 = sha256(binascii.unhexlify(private_key_cmp)).hexdigest()
    sha2 = sha256(binascii.unhexlify(sha1)).hexdigest()
    first4_cmp = sha2[0:8]
    print("first 4 cmp =",first4_cmp)

    private_key_w_checksum_cmp = private_key_cmp+first4_cmp


    private_key_cmp_int = int(private_key_w_checksum_cmp,16)
    print("private_key_cmp=",private_key_w_checksum_cmp)
    private_compressed = base58.b58encode_int(private_key_cmp_int)
    #print("private key compressed:",private_compressed)

    new_private_key.compressed = private_compressed
    new_private_key.uncompressed = private_uncompressed
    new_private_key.intkey = private_key_int
    
    return new_private_key
    

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
def PublicKey(input_private_key):
    _p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    _r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    _a = 0x0000000000000000000000000000000000000000000000000000000000000000
    _b = 0x0000000000000000000000000000000000000000000000000000000000000007
    _Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    _Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

    # Define new secp256k1 curve:
    p_Gx = hbitcoin.ecch.FieldElement(_Gx,_p)
    p_Gy = hbitcoin.ecch.FieldElement(_Gy,_p)
    p_a = hbitcoin.ecch.FieldElement(_a,_p)
    p_b = hbitcoin.ecch.FieldElement(_b,_p)

    private_key = input_private_key
    
    generator = hbitcoin.ecch.Point(p_Gx,p_Gy,p_a,p_b)
    hbitcoin.ecch.Point.onCurve(generator)
    pubkey = private_key * generator
    #print("-------Publick Key Coordinates----------")
    #print("Public Key = ",pubkey)

    # https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses#How_to_create_Bitcoin_Address

    # 1 - Take the corresponding public key generated with it (33 bytes, 1 byte 0x02 (y-coord is even), and 32 bytes corresponding to X coordinate) 
    public_key_x = pubkey.x.num
    public_key_y = pubkey.y.num
    if public_key_y % 2 == 0:
        prefix = '02'
    else:
        prefix= '03'

    temp_pub_key = prefix + (hex(public_key_x)[2:]).rjust(64,'0')

    #print("temp_pub_key =",temp_pub_key)
    #print(len(temp_pub_key))

    # 2 - Perform SHA-256 hashing on the public key 
    temp_pub_key_SHA = sha256(binascii.unhexlify(temp_pub_key)).hexdigest()
    #print("sha1 pub",temp_pub_key_SHA)

    # 3 - Perform RIPEMD-160 hashing on the result of SHA-256 
    h = hashlib.new('ripemd160')
    h.update(binascii.unhexlify(temp_pub_key_SHA))
    temp_pub_key_SHA_160 = h.hexdigest()
    #print("RIP160 pub",temp_pub_key_SHA_160)

    #4 - Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
    temp_pub_key_SHA_160_plus_version = '00'+temp_pub_key_SHA_160
    #print("temp_pub_key_SHA_160_plus_version=",temp_pub_key_SHA_160_plus_version)

    #5 - Perform SHA-256 hash on the extended RIPEMD-160 result 
    temp_pub_key_SHA1 = sha256(binascii.unhexlify(temp_pub_key_SHA_160_plus_version)).hexdigest()
    #print("temp_pub_key_SHA1=",temp_pub_key_SHA1)


    #6 - Perform SHA-256 hash on the result of the previous SHA-256 hash 
    temp_pub_key_SHA2 = sha256(binascii.unhexlify(temp_pub_key_SHA1)).hexdigest()
    #print("temp_pub_key_SHA2=",temp_pub_key_SHA2)


    #7 - Take the first 4 bytes of the second SHA-256 hash. This is the address checksum
    checksum_pub = temp_pub_key_SHA2[0:8]
    #print(checksum_pub)

    #8 - Add the 4 checksum bytes from stage 7 at the end of extended RIPEMD-160 hash from stage 4. This is the 25-byte binary Bitcoin Address.
    #temp_pub_key_with_checksum =  bytes(('0x'+temp_pub_key_SHA_160_plus_version + checksum_pub),'utf-8')

    temp_pub_key_with_checksum =  temp_pub_key_SHA_160_plus_version + checksum_pub
    #print("temp_pub_key_with_checksum=",temp_pub_key_with_checksum)

    temp_pub_key_with_checksum_int = int(temp_pub_key_with_checksum,16)
    #9 - Convert the result from a byte string into a base58 string using Base58Check encoding. This is the most commonly used Bitcoin Address format 


    pub_address = '1'+  str(base58.b58encode_int(temp_pub_key_with_checksum_int),'utf-8')
    #print("pub_address=",pub_address)

    #test here:
    # https://walletgenerator.net/#

    return pub_address

