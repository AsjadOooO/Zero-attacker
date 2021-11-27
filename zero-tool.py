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
""")

print(Fore.YELLOW+"""

1.IP SCANNER                   | 7.Sub-Domain-Scanner      
2.Discord-Nuke                 | 8.DDOS-TOOL
3.Discord-BruteForce           | 9:Discord-Token-Checker
4.Email-Boomber                | 10.Proxies-Generator
5.Phone-Locator                | 11.Email-Generator
6.Port-Scanner                 | 12.Zero-RaidTool
13.Zero-Token-Generator        | 14.Spammer (Beta)
15.SELFBOT(NOT A HACKING TOOL) | 16.Zero-Web-Hacking-Tool
""")

command = input('> ')

if command == '1':
   os.system('cmd /k "python ip-locater.py"')

elif command == '2':
  os.system('cmd /k "python Discord-Nuke-Tool.py')

elif command == '3':
   os.system('cmd /k "python Discord-Token-BruteForce.py')

elif command == '4':
    os.system('cmd /k "python emailboomber.py')

elif command == '5':
    os.system('cmd /k "python phlocator.py"')

elif command == '6':
    os.system('cmd /k "python Port-Scanner.py')

elif command == '7':
    os.system('cmd /k "python Sub-Domain-Scanner.py')

elif command == '8':
    os.system('cmd /k "python ddos.py"')

elif command == '9':
    os.system('cmd /k "python Discord-Token-Checker.py"')


elif command == '10':
    os.system('cmd /k "python proxies-generator.py"')

elif command == '11':
    os.system('cmd /k "python email-generator.py"')


elif command == '12':
    os.system('cmd /k "python raidtool.py"')

elif command == '13':
  os.system('cmd /k "python Zero-Gen/start.py"')

elif command == '14':
  os.system('cmd /k "python Spammers(Beta)/spammer.py"')

elif command == '15':
  os.system('cmd /k "python ZEROSELFBOT-(NOT-HACKING-TOOL)/zeroselfbot.py"')

elif command == '16':
  os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    
      

else:
  print('Please choose the correct one dont be dumb')
