#example 4-5

import bitcoin

#generate a random private key
valid_private_key = False
while not valid_private_key:
    #generate a random private key in Hex
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