#example 4-5

import bitcoin
from hashlib import sha256
import base58
import binascii

#hashlib enables us to utilze the SHA256 function
from hashlib import sha256

#generate a random private key
valid_private_key = False
while not valid_private_key:
    #generate a random private key in Hex - this is a string datatype (STR)
    new_private_key_hex = bitcoin.random_key()
    private_key_decimal = bitcoin.decode_privkey(new_private_key_hex,'hex')

    #checking to see if private key does not exceed the following very large number:
    # 115792089237316195423570985008687907852837564279074904382605163141518161494337
    if private_key_decimal > 0 and private_key_decimal < bitcoin.N:
        valid_private_key = True
print("   ******Generating WIF Using PyPi Library*****   \n")
print("1. The new private key (Hex) is:","\n",new_private_key_hex)

#convert the private key to WIF(Wallet interchange format) format using the bitcoin libray function.
new_private_key_hex_WIF = bitcoin.encode_privkey(new_private_key_hex,'wif')
print("\n")
print("2. WIF Private Key using pypi 'bitcoin' library = ","\n",new_private_key_hex_WIF)

#Converting the WIF Private key manually, the hard way:
# https://en.bitcoin.it/wiki/Wallet_import_format

#Step 1: Prefix version information
#Prefix 0x80 for mainnet or 0xef for test net. The following step generates a Hex literal string with "80" prefixed to it:
new_private_key_hex01 = '80'+new_private_key_hex

print("\n")
print("   ******Generating WIF the hard way*****   \n")
print("3. Generating WIF the hard way:")
print("3.1 Step1-WIF: New_private_key_hex01 with 80 prefixed:","\n",new_private_key_hex01)
#Step 1.1:
new_private_key_binary = binascii.unhexlify(new_private_key_hex01)
print("3.2 New_private_key_binary =","\n",new_private_key_binary)

print("\n")
#Step 2: Perform 2 SHA256 hashes on the above private key
#https://bitcoin.stackexchange.com/questions/43347/how-to-generate-bitcoin-address

# IMPORTANT!!! - Always convert the Hex value of the ECDSA private key 
# into Raw Bytes before Hashing it using SHA256
SHA256_1_input = new_private_key_binary
SHA256_1_output = sha256(SHA256_1_input).hexdigest()
print("4. The first sha 256 of the pre-fixed Private Key is:","\n",SHA256_1_output)

print("\n")
#Step 2.1:
SHA256_1_binary = binascii.unhexlify(SHA256_1_output)
print("5. SHA256_1_binary =","\n",SHA256_1_binary)

print("\n")
SHA256_2_input = SHA256_1_binary
SHA256_2_output = sha256(SHA256_1_binary).hexdigest()
print("6. The double sha 256 of the pre-fixed Private Key is:","\n",SHA256_2_output)

#new_private_key_hex01_SHA256 = sha256(sha256(new_private_key_hex01.encode('utf-8')).digest()).digest()
#print("the double sha 256 of the pre-fixed Private Key is:",new_private_key_hex01_SHA256)

#Step 3: Get the first 4 bytes of the double sha Hex:
first4 = SHA256_2_output[0:8]
print("First 4 bytes of double SHA256 = ","\n",first4)

print("\n")
#Step 4: Add checksum to priv key (suffix)
new_private_key_hex01_with_checksum = new_private_key_hex01 + first4
print("7. New private key w checksum = ","\n",new_private_key_hex01_with_checksum)

new_private_key_hex01_with_checksum_decimal = int(new_private_key_hex01_with_checksum,16)
print("\n")
#Step 5: Base58 Check Encode
private_key_base58 = base58.b58encode_int(new_private_key_hex01_with_checksum_decimal)
print("8. base58 key WIF is:","\n",private_key_base58)
