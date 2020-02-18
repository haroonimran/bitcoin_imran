import hbitcoin.keys

count =  int(input("Enter the number of key pairs to generate:"))
for _ in range(count):
    new_private_key = hbitcoin.keys.PrivateKey()
    pubic_key = hbitcoin.keys.PublicKey(new_private_key.intkey)
    print("Private Key Uncompressed = {}\nPrivate Key Compressed   = {}\nPublic  Key Compressed   = {}\n"\
        .format(str(new_private_key.uncompressed)[2:-1],str(new_private_key.compressed)[2:-1],pubic_key))
