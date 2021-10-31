import os
import time
import sys
import pyperclip as pc
import random
import nmap
import re

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
watsonlogo = color_random[1] + '''
$$$$$$$\                      $$\      $$\             $$\                                   
$$  __$$\                     $$ | $\  $$ |            $$ |                                  
$$ |  $$ | $$$$$$\            $$ |$$$\ $$ | $$$$$$\  $$$$$$\    $$$$$$$\  $$$$$$\  $$$$$$$\  
$$ |  $$ |$$  __$$\           $$ $$ $$\$$ | \____$$\ \_$$  _|  $$  _____|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  \__|          $$$$  _$$$$ | $$$$$$$ |  $$ |    \$$$$$$\  $$ /  $$ |$$ |  $$ |
$$ |  $$ |$$ |                $$$  / \$$$ |$$  __$$ |  $$ |$$\  \____$$\ $$ |  $$ |$$ |  $$ |
$$$$$$$  |$$ |      $$\       $$  /   \$$ |\$$$$$$$ |  \$$$$  |$$$$$$$  |\$$$$$$  |$$ |  $$ |
\_______/ \__|      \__|      \__/     \__| \_______|   \____/ \_______/  \______/ \__|  \__|
        '''
watsonPrompt = color.END + "watson ~# "

def start():
    print(watsonlogo)

class watson:
    def __init__(self):
        clearScr()
        print (watsonlogo + color.RED + '''
       }---------------{+} Coded By bartosz-skejcik {+}--------------{
       }--------{+}  GitHub.com/bartosz-skejcik/dr.watson {+}--------{
    ''' + color.END + '''
       [1]  Information Gathering
       [2]  Hashing
       [0]  EXIT
     ''')
        choice = raw_input(watsonPrompt)
        clearScr()
        if choice == "1":
            informationGatheringMenu()
        elif choice == "2":
            hashingMenu()
        elif choice == "00":
            self.update()
        elif choice == "0":
            sys.exit()
        elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
            self.__init__()
        else:
            try:
                print(os.system(choice))
            except:
                pass
        self.completed()


        def update(self):
            os.system("git clone --depth=1 https://github.com/bartosz-skejcik/dr.watson.git")
            os.system("cd dr.watson && bash ./update.sh")
            os.system("watson")


class hashingMenu:
    menuLogo = '''
 _   _              _      _               
| | | |            | |    (_)              
| |_| |  __ _  ___ | |__   _  _ __    __ _ 
|  _  | / _` |/ __|| '_ \ | || '_ \  / _` |
| | | || (_| |\__ \| | | || || | | || (_| |
\_| |_/ \__,_||___/|_| |_||_||_| |_| \__, |
                                      __/ |
                                     |___/ 
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)

        print("  [1]  Decoding    [2]  Encoding\n")
        print("  [0]-Back To Main Menu \n")
        choice2 = input(watsonPrompt)
        clearScr()
        if choice2 == "1":
            decode()
        elif choice2 == "1":
            encode()
        elif choice2 == "0":
            watson()
        else:
            self.__init__()
        self.completed()


class informationGatheringMenu:
    menuLogo = '''
    88 88b 88 888888  dP"Yb
    88 88Yb88 88__   dP   Yb
    88 88 Y88 88""   Yb   dP
    88 88  Y8 88      YbodP
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)

        print("  [1] Nmap - Network Port Scanner\n")
        print("  [0]-Back To Main Menu \n")
        choice2 = input(watsonPrompt)
        clearScr()
        if choice2 == "1":
            nmap()
        elif choice2 == "0":
            watson()
        else:
            self.__init__()
        self.completed()

class decode:

    menuLogo = '''    
______                         _  _               
|  _  \                       | |(_)              
| | | |  ___   ___   ___    __| | _  _ __    __ _ 
| | | | / _ \ / __| / _ \  / _` || || '_ \  / _` |
| |/ / |  __/| (__ | (_) || (_| || || | | || (_| |
|___/   \___| \___| \___/  \__,_||_||_| |_| \__, |
                                             __/ |
                                            |___/ 
'''

    def __init__(self):
        clearScr()
        print(self.menuLogo)

        choice2 = input('message/' + watsonPrompt)
        clearScr()
        if choice2 == "1":
            nmap()
        elif choice2 == "0":
            watson()
        else:
            self.__init__()
        self.completed()