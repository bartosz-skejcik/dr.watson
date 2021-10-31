import pyperclip as pc
from func import *
import os
import time
import sys
import random

try:
    from cryptography.fernet import Fernet
    print("All required modules are installed")
    time.sleep(2)
except ModuleNotFoundError:
    print("App requires module 'cryptography' to work correctly")
    install = input("Do You want to install it? (y/n): ")
    if install == "y":
        os.system("pip3.10 install cryptography")
        try:
            from cryptography.fernet import Fernet
            print("""Module installed correctly.
Opening the app...""")
            time.sleep(1)
        except ModuleNotFoundError:
            print("Module did not install correctly\nExiting...")
            time.sleep(2)
            exit()
        
    else:
        print("Exiting the program...")
        time.sleep(1)
        exit()

while True:
    os.system('cls')
    start()
    a = input(fsocietyPrompt)

    