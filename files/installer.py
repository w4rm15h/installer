#w4rm15h installer
#Final installer forever
import shutil, os
import wget

todo = {
    "Copying Files" : "Incomplete",
    "Install Code" : "Incomplete",
}

def printTitle():
    os.system("clear")
    print("--------------------")
    print("-I N S T A L L E R -")
    print("--------------------")
    for key, status in todo.items():
        print(f"{key}: {status}")
    print("--------------------")

def installVCode():
    dlink = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    fName = "vcode_current.deb"
    response = wget.download(dlink, f"Downloads/{fName}")


def copyFiles():
    username = os.getlogin()
    path = f"/home/{username}/scripts/"
    installPath = "scripts/"
    #Making the scripts folder
    if not os.path.exists(path):
        os.mkdir(path)      
    #copying files from installer to local
    for file in os.listdir(installPath):
        shutil.copy(f"{installPath}{file}", f"{path}{file}")
    #PIP INSTALLS
    

def mainFunction():
    printTitle()
    copyFiles()
    installVCode()
    
if __name__ == "__main__":
    mainFunction()


