#example 4-5

import bitcoin

#generate a random private key
valid_private_key = False
while not valid_private_key:
    new_private_key_hex = bitcoin.random_key()
    private_key_decimal = bitcoin.decode_privkey(new_private_key_hex,'hex')
    if private_key_decimal > 0 and private_key_decimal < bitcoin.N:
        valid_private_key = True

print("Valid_private_key = ",valid_private_key)
print("The private key in HEX = ",new_private_key_hex)
print("The private key in decimal  =",private_key_decimal)
print("Bitcoin.N = ",bitcoin.N)

#test Decimal to Hex:
print("Decimal to Hex using hex():",hex(private_key_decimal))

#test Hex to Decimal:
print("Hex to Decimal using int(x,16):",int(new_private_key_hex,16))
