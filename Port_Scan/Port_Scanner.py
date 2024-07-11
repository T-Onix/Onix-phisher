import sys
from queue import Queue
import threading
from datetime import datetime
import os
#=============================================================================================
try:
    import win32gui , win32con
    import socket
    from colorama import Fore , init ; init()
except ImportError or ModuleNotFoundError:
    os.system("pip3 install colorama , socket , pywin32")

#Full Screnn=============================================================================================
getsize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(getsize , win32con.SW_MAXIMIZE)
#=============================================================================================
Red = Fore.RED
White = Fore.LIGHTWHITE_EX
Magenta = Fore.MAGENTA
Green = Fore.GREEN
Reset = Fore.RESET
#=============================================================================================
def clear():
 
    # for windows
    if os.name == "nt":
        os.system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system("clear")

clear()
#=============================================================================================
print(White + '''
        
     ▒█████   ███▄    █  ██▓▒██   ██▒    ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
    ▒██▒  ██▒ ██ ▀█   █ ▓██▒▒▒ █ █ ▒░   ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
    ▒██░  ██▒▓██  ▀█ ██▒▒██▒░░  █   ░   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
    ▒██   ██░▓██▒  ▐▌██▒░██░ ░ █ █ ▒    ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
    ░ ████▓▒░▒██░   ▓██░░██░▒██▒ ▒██▒   ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
    ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ▒▒ ░ ░▓ ░   ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░░░   ░▒ ░   ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
    ░ ░ ░ ▒     ░   ░ ░  ▒ ░ ░    ░     ░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
        ░ ░           ░  ░   ░    ░                  ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                                                        ░                                                        
''' + Reset)

#=============================================================================================

try:
    host = socket.gethostbyname(input(Magenta + "Enter The Domain/IP : " + White))
except KeyboardInterrupt or Exception:
    exit(f"\n{Red}[-]{Fore.BLUE} An Error occurred !!")


startfrom = 1
endwith = 1025

allPort = 1
allPortEnd = 65535

customPortStart = 0
customPortEnd = 0

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(f"\n{Red}[1]{White} 1024 port Scan ")
print(f"{Red}[2]{White} Full Scan (1 / 65535)")
print(f"{Red}[3]{White} Custom Port Scan")
print(f"{Red}[4]{White} Show IP and Exit \n")

try:
    mode = int(input(Magenta + "Select Any Option : " + White))
    print(" ")
except ValueError or KeyboardInterrupt:
    exit(f"{Red}[-]{Fore.BLUE} An error occurred !!")

if mode == 3:
    try:
        customPortStart = int(input(Magenta + "Enter starting port number : ".title() + Reset))
        customPortEnd = int(input(Magenta + "Enter ending port number : ".title() + Reset))
    except KeyboardInterrupt:
        exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")


print("-"*50)
print(f"{Green}Target IP :{White} {host}")
print(f"{Green}Scanning started at :{White} {current_time}")
print("-"*50 + Reset) 

def scan(port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((host, port))
    if result == 0:
       print(f"Port {Green}{port}{White} is Open")
    s.close()

queue = Queue()

#=============================================================================================
def get_ports(mode):
    if mode == 1:
        print(f"\n{Fore.YELLOW}亗{White} Scaning {Fore.YELLOW}亗\n" + White)
        for port in range(startfrom , endwith):
            queue.put(port)

#=============================================================================================
    elif mode == 2:
        print(f"\n{Fore.YELLOW}亗{White} Scaning {Fore.YELLOW}亗\n" + White)
        for port in range(allPort, allPortEnd+1):
            queue.put(port)

#=============================================================================================
    elif mode == 3:
        print(f"\n{Fore.YELLOW}亗{White} Scaning {Fore.YELLOW}亗\n" + White)
        for port in range(customPortStart, customPortEnd+1):
            queue.put(port)

#=============================================================================================
    elif mode == 4:
        sys.exit()

#=============================================================================================
open_ports = [] 
def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for i in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

run_scanner(1021, mode)
print(f"\n{Fore.YELLOW}Scan Completed in:{White} {current_time}")