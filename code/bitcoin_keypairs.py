from keygen import PrivateKey
from keygen import PublicKey

class GenerateKeyPair:

    def __init__(self, final_private_key, final_public_key):
        self.final_private_key = PrivateKey(integer = False, compressed = True)
        self.final_public_key = PublicKey()
        return
        
    def __repr__(self):
        return 'Public Key:[{}],Privare Key[{}]'.format(self.final_private_key,self.final_public_key)
