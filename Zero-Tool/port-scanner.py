import sys 
import socket 
from datetime import datetime 
print("Enter your host ip address , Example '192.168.10.10'")
host = socket.gethostbyname(input("Enter your host ip address: "))

print("Enter the range, Example '50'")
ports = input(str("Enter range between 1 to 1000 "))

print("-" * 50)
print("scanning  target" + host)
print("Time started" + str(datetime.now()))
print("-" * 50)
try:
             for port in range(int(ports)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((host,port))
                    if result == 0:
                            print(F"Following {port} is open")
                    s.close()
         
except KeyboardInterrupt:
    print("\r Exiting program")

except socket.gaierror:
    print("Host name could not be solved")
    sys.exit()
except socket.error:
    print("could not connect")
    sys.exit()