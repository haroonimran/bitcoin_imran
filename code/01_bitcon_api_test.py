#bitcoin.rpc is part of the "bitcoinlib" pythonpackage
from bitcoin.rpc import RawProxy
p = RawProxy()
info = p.getblockchaininfo()
print(info)
