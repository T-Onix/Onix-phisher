from time import sleep
import subprocess
import platform
import random
import os
import sys

#for Windows ====================================================================================================
if os.name == "nt":
    try:
        from colorama import Fore , init; init()
        
    except (ImportError , ModuleNotFoundError):
        install = input("unfortunately you dont have excepetd modules !!\nWant to install ? (y/n) : ")
        if install == "y" or install == "Y":
            subprocess.call("pip install colorama" , shell=True)
            sleep(1)
            sys.exit()
        else:
            exit("\nhave a good day".title())
#for termux ====================================================================================================
try:
    from colorama import Fore , init; init()
    
except (ImportError , ModuleNotFoundError):
    if platform.uname()[1] == "localhost" :
        print("\nYou may have missing libraries , colorama!\n")
        subprocess.call("pkg install python-colorama" , shell=True)
        sleep(1)
        sys.exit()
    else:
        pass

#for Linux====================================================================================================

else:
    try:
        from colorama import Fore , init ;init()
            
    except (ImportError , ModuleNotFoundError):
        try:
            print("You may have missing libraries , colorama\n")
            
            package_installer = input("\nEnter your package installer (like 'apt install' or 'pacman -S') >> ")
            python_v = input("\nYour linux using [1]python3 or [2]python for installing packages of python (Enter 1 or 2) >> ")
            if python_v == "1":
                subprocess.call(f"{package_installer} python3-colorama" ,  shell=True)
                sys.exit()
                
            elif python_v == "2":
                subprocess.call(f"{package_installer} python-colorama" ,  shell=True)
                sys.exit()
        except NameError:
            exit("\nWrong package installer name or python name !")
        except KeyboardInterrupt:
            exit("\n\nUser Exited :)")

#Banner ====================================================================================================

Banner_color = (Fore.RED , Fore.MAGENTA , Fore.BLUE , Fore.GREEN)

def banner():
   global Banner_color

   print(fr"""{random.choice(Banner_color)}
         
    ███████                ███                 ███████████  █████       ███          █████                        
  ███░░░░░███             ░░░                 ░░███░░░░░███░░███       ░░░          ░░███                         
 ███     ░░███ ████████   ████  █████ █████    ░███    ░███ ░███████   ████   █████  ░███████    ██████  ████████ 
░███      ░███░░███░░███ ░░███ ░░███ ░░███     ░██████████  ░███░░███ ░░███  ███░░   ░███░░███  ███░░███░░███░░███
░███      ░███ ░███ ░███  ░███  ░░░█████░      ░███░░░░░░   ░███ ░███  ░███ ░░█████  ░███ ░███ ░███████  ░███ ░░░ 
░░███     ███  ░███ ░███  ░███   ███░░░███     ░███         ░███ ░███  ░███  ░░░░███ ░███ ░███ ░███░░░   ░███     
 ░░░███████░   ████ █████ █████ █████ █████    █████        ████ █████ █████ ██████  ████ █████░░██████  █████    
   ░░░░░░░    ░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░    ░░░░░        ░░░░ ░░░░░ ░░░░░ ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░
{Fore.RESET}""")