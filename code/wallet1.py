from bitcoinlib.wallets import HDWallet
w = HDWallet.create('Wallet1')
w
key1 = w.new_key()
key1
key1.address
