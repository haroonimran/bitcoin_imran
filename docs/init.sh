#!/bin/bash
sudo apt-get update
sudo apt-get -y install vim
sudo apt-get -y install git
git clone https://github.com/bitcoin/bitcoin.git
sudo apt-get -y install autoconf
sudo apt-get -y install libboost-dev
sudo apt-get -y install libboost-all-dev
sudo apt-get -y install libevent-dev
sudo apt-get -y install libminiupnpc-dev
sudo apt-get -y install qt4*
sudo apt-get -y install libssl-dev
sudo apt-get -y install libqrencode-dev
sudo apt-get -y install libdb4.8
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get -y update
sudo apt-get -y install -y libdb4.8-dev libdb4.8++-dev
sudo apt-get -y install libzmq2-dev
sudo apt-get -y install g++
sudo apt-get -y libtool*
sudo apt-get -y install pkg-config
cd bitcoin
./autogen.sh
./configure
make
sudo make check && sudo make install
sudo apt-get -y install python3-bitcoinlib
