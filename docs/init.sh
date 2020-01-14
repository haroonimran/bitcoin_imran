sudo apt-get update
sudo apt-get install vim
sudo apt-get install git
git clone https://github.com/bitcoin/bitcoin.git
sudo apt-get install autoconf
sudo apt-get install libboost-dev
sudo apt-get install libboost-all-dev
sudo apt-get install libevent-dev
sudo apt-get install libminiupnpc-dev
sudo apt-get install qt4*
sudo apt-get install libssl-dev
sudo apt-get install libqrencode-dev
sudo apt-get install libdb4.8
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install -y libdb4.8-dev libdb4.8++-dev
sudo apt-get install libzmq2-dev
sudo apt-get install g++
sudo apt-get libtool*
sudo apt-get install pkg-config
./autogen.sh
./configure
make
sudo make check && sudo make install
sudo apt-get install python3-bitcoinlib
