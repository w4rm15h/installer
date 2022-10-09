#!/bin/bash

echo "Let's set our git login"
echo "Enter your email address"
read email
git config --global user.email "$email"
echo "Enter your username"
read userName
git config --global user.name "$userName"
echo "installing pip requirements"
pip install virtualenv
pip install wget
python3 files/installer.py