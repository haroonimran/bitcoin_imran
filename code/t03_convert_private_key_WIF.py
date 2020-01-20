#example 4-5

import bitcoin
import hashlib
import base58


#hashlib enables us to utilze the SHA256 function
from hashlib import sha256

#generate a random private key
valid_private_key = False
while not valid_private_key:
    #generate a random private key in Hex - this is a string datatype (STR)
    new_private_key_hex = bitcoin.random_key()
    
    #convert the hex key to decimal
    #this could potentially be acheived using the native python function int(x,16) where x is a Hex string
    private_key_decimal = bitcoin.decode_privkey(new_private_key_hex,'hex')

    #checking to see if private key does not exceed the following very large number:
    # 115792089237316195423570985008687907852837564279074904382605163141518161494337
    if private_key_decimal > 0 and private_key_decimal < bitcoin.N:
        valid_private_key = True

print(valid_private_key)
print("The new private key (Hex) is:",new_private_key_hex)

#convert the private key to WIF(Wallet interchange format) format using the bitcoin libray function.
new_private_key_hex_WIF = bitcoin.encode_privkey(new_private_key_hex,'wif')
print("The private key in the WIF format = ",new_private_key_hex_WIF)

#Converting the WIF Private key manually, the hard way:
# https://en.bitcoin.it/wiki/Wallet_import_format

#Step 1: Prefix version information
#Prefix 0x80 for mainnet or 0xef for test net. The following step generates a Hex literal string with "80" prefixed to it:
new_private_key_hex01 = str(80)+new_private_key_hex
print("Step1-WIF: New_private_key_hex01 with 80 prefixed: ", new_private_key_hex01)

#Step 2: Perform 2 SHA256 hashes on the above private key
SHA256_1 = sha256(new_private_key_hex01.encode()).digest()
print("The first sha 256 of the pre-fixed Private Key is:",SHA256_1)

SHA256_2 = sha256(SHA256_1).digest()
print("the double sha 256 of the pre-fixed Private Key is:",SHA256_2)

new_private_key_HEX_SHA256 = SHA256_2.hex()
print("the double sha 256 of the pre-fixed Private Key iin HEX is:",new_private_key_HEX_SHA256)

#new_private_key_hex01_SHA256 = sha256(sha256(new_private_key_hex01.encode('utf-8')).digest()).digest()
#print("the double sha 256 of the pre-fixed Private Key is:",new_private_key_hex01_SHA256)

#Step 3: Get the first 4 bytes of the double sha Hex:
first4 = new_private_key_HEX_SHA256[0:8]
print("First 4 bytes = ",first4)

#Step 4: Add checksum to priv key (suffix)
new_private_key_hex01_with_checksum = new_private_key_hex01 + first4
print("New private key w checksum = ",new_private_key_hex01_with_checksum)

new_private_key_hex01_with_checksum_decimal = int(new_private_key_hex01_with_checksum,16)

#Step 5: Base58 Check Encode
private_key_base58 = base58.b58encode_int(new_private_key_hex01_with_checksum_decimal)
print("base58 key is:", private_key_base58)
