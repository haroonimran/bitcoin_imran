#!/bin/bash
sudo apt-get update
sudo apt-get -y install vim
sudo apt-get -y install git
sudo apt-get -y install autoconf
sudo apt-get -y install libboost-dev
sudo apt-get -y install libboost-all-dev
sudo apt-get -y install libevent-dev
sudo apt-get -y install libminiupnpc-dev
sudo apt-get -y install qt4*
sudo apt-get -y install libssl-dev
sudo apt-get -y install libqrencode-dev

#Install libdb dependencies
sudo apt-get -y install libdb4.8
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get -y update
sudo apt-get -y install -y libdb4.8-dev libdb4.8++-dev

sudo apt-get -y install libzmq2-dev
sudo apt-get -y install g++
sudo apt-get -y libtool*
sudo apt-get -y install pkg-config

#clone bitcoin core:
git clone https://github.com/bitcoin/bitcoin.git

#navigate to the "bitcoin" directory cloned from github in the previous step
cd bitcoin
./autogen.sh
./configure
make

#installs the BitCoin Core package that was compiled in the previous step
sudo make check && sudo make install

#install the pip package for python3
sudo apt intsall -y python3-pip

# intstalls the bitcoin library for python
pip3 install bitcoin
sudo apt-get -y install python3-bitcoinlib
