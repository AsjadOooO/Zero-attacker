import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

 _______  _______  _______  _______         _______ __________________ _______  _______  _        _______  _______ 
/ ___   )(  ____ \(  ____ )(  ___  )       (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )
\/   )  || (    \/| (    )|| (   ) |       | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| (    \/| (    )|
    /   )| (__    | (____)|| |   | | _____ | (___) |   | |      | |   | (___) || |      |  (_/ / | (__    | (____)|
   /   / |  __)   |     __)| |   | |(_____)|  ___  |   | |      | |   |  ___  || |      |   _ (  |  __)   |     __)
  /   /  | (      | (\ (   | |   | |       | (   ) |   | |      | |   | (   ) || |      |  ( \ \ | (      | (\ (   
 /   (_/\| (____/\| ) \ \__| (___) |       | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
(_______/(_______/|/   \__/(_______)       |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_______/|/   \__/
                                                                                                                   
                                                                 

BY: DEV7KNIGHT X ASJAD
Version 0.1
""")

print(Fore.YELLOW+"""

1: Zero-Tool (Hacking Tools)   | 2:Zero-Web-Hacking-Tool
3: Zero-Token-Generator        | 4.Spammer (Beta)
5: Information about us        | 6.SELFBOT(NOT A HACKING TOOL)
""")

command = input('> ')

if command == '1':
   os.system('cmd /k "python Zero-Tool/zero.py"')


elif command == '2':
  os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    

elif command == '3':
  os.system('cmd /k "python Zero-Gen/start.py"')

elif command == '4':
  os.system('cmd /k "python Spammers(Beta)/spammer.py"')

elif command == '5':
  os.system('cmd /k "python info.py"')

elif command == '6':
  os.system('cmd /k "python ZEROSELFBOT-(NOT-HACKING-TOOL)/zeroselfbot.py"')


    
      

else:
  print('Please choose the correct one dont be dumb')
