#!/bin/bash

echo "Let's set our global git login"
echo "Enter your email address"
read email
git config --global user.email "$email"

echo "Enter your username"
read userName
git config --global user.name "$userName"

echo "installing pip requirements"
pip install virtualenv
pip install wget

echo "Downloading latest installer files"
wget -O vsCODE.deb "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
sudo dpkg -i vsCode.deb
echo "Visual Studio Code installed."

python3 files/installer.py