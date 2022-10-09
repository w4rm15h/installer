#w4rm15h installer
#Final installer forever
import sys, os
from ftplib import FTP

todo = {
    "init": "Incomplete",
    "ftp files": "Incomplete",
    "Install Code": "Incomplete",
}

def printTitle():
    os.system("clear")
    print("Fresh Installer")

def init():
    os.system("clear")
    print("getting things ready boss...")
    try:
        os.mkdir("scripts")
    except:
        pass

def ftpFiles():
    ftp = FTP('66.220.9.50')
    ftpUser = input("Enter Username: ")
    ftpPass = input("Enter Password: ")
    ftp.login(f"{ftpUser}", f"{ftpPass}")
    ftp.getwelcome()

def mainFunction():
    printTitle()

if __name__ == "__main__":
    mainFunction()


