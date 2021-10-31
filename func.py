import os
import time
import sys
import pyperclip as pc
import random

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

                ************************************************************
                
                * Copyright of Bartek Paczesny, 2021                       *
                
                * http://dev.paczesny.pl                                   *
                
                * https://www.youtube.com/channel/UC2ltR6-85OHpZfSPyNQx66Q *
                
                ************************************************************
        '''
watsonPrompt = color.END + "watson ~# "

def hashing():
    try:
        if(not os.path.isfile('klucz.key')):
            key = Fernet.generate_key()

            file = open('klucz.key', 'wb')
            file.write(key)
            file.close()
        else:
            os.system("cls")
            file = open('klucz.key', 'rb')
            key = file.read()
            file.close()
            print("Using key: ", key, "\n")

            print("What do you want to do?\n1. Encrypt a message\n2. Decrypt a message")
            enc_dec = input("> ")
            if(enc_dec == "1"):
                message = input("message> ")

                encoded = message.encode() # enkodowanie wiadomosci na bajty

                f = Fernet(key)
                
                encrypted = f.encrypt(encoded) # enkryptowanie enkodowanej wiadomosci (jak nie zenkodujesz to nie zadziała)
                original_msg = encrypted.decode() # dekodowanie zaszyfrowanej wiadomosci
                pc.copy(original_msg)

                print("\nmessage ->  ", original_msg)
                time.sleep(3)
            elif(enc_dec == "2"):
                message = input("message> ")
                f = Fernet(key)

                encrypted = message.encode()

                decrypted = f.decrypt(encrypted)
                original_msg = decrypted.decode()
                pc.copy(original_msg)

                print("\nmessage ->  ", original_msg)
                time.sleep(3)
            else:
                print('wrong code!')
                exit()
    except ModuleNotFoundError:
        print("Cannot find module named: 'cryptography'")

def start():
    print(watsonlogo)

class fsociety:
    def __init__(self):
        clearScr()
        self.createFolders()
        print (watsonlogo + color.RED + '''
       }--------------{+} Coded By Manisso {+}--------------{
       }--------{+}  GitHub.com/bartosz-skejcik/dr.watson {+}--------{
    ''' + color.END + '''
       {1}--Information Gathering
       {2}--Password Attacks
       {3}--Wireless Testing
       {4}--Exploitation Tools
       {5}--Sniffing & Spoofing
       {6}--Web Hacking
       {7}--Private Web Hacking
       {8}--Post Exploitation
       {0}--INSTALL & UPDATE
       {11}-CONTRIBUTORS
       {0}-EXIT\n
     ''')
        choice = raw_input(watsonPrompt)
        clearScr()
        if choice == "1":
            informationGatheringMenu()
        elif choice == "2":
            passwordAttacksMenu()
        elif choice == "3":
            wirelessTestingMenu()
        elif choice == "4":
            exploitationToolsMenu()
        elif choice == "5":
            sniffingSpoofingMenu()
        elif choice == "6":
            webHackingMenu()
        elif choice == "7":
            privateWebHacking()
        elif choice == "8":
            postExploitationMenu()
        elif choice == "00":
            self.update()
        elif choice == "11":
            self.githubContributors()
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