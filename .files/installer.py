#w4rm15h installer
#Final installer forever
import shutil, os
import wget

todo = {
    "Install VsCode" : "Complete",
    "Copied Script files" : "Incomplete",
}

def printTitle():
    os.system("clear")
    print("--------------------")
    print("-I N S T A L L E R -")
    print("--------------------")
    for key, status in todo.items():
        print(f"{key}: {status}")
    print("--------------------")

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

def mainFunction():
    printTitle()
    copyFiles()
    
if __name__ == "__main__":
    mainFunction()


