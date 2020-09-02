import os
import platform
from sys import platform as _platform
import colorama
from colorama import Fore , Back, Style
colorama.init()
def uyarı():
    print(Fore.BLUE)
    print("I dont accept any responsibility when you use this tool")
def giris():
    print(Fore.RED)
    print("""

__________              __                                                     
\______   \____________/  |_    ______ ____ _____    ____   ____   ___________ 
 |     ___/  _ \_  __ \   __\  /  ___// ___\\__  \  /    \ /    \_/ __ \_  __ \
 |    |  (  <_> )  | \/|  |    \___ \\  \___ / __ \|   |  \   |  \  ___/|  | \/
 |____|   \____/|__|   |__|   /____  >\___  >____  /___|  /___|  /\___  >__|   
                                   \/     \/     \/     \/     \/     \/       

""")
giris()
uyarı()
print(Fore.YELLOW)
warning = input("Do you accept all responsibility of using this tool ? ")
if warning == "yes" or "Yes" or "YES":
    print(Fore.RED)
    print("Well you accept the responsibility you can use it by ur self ! ")
    if _platform == "win32"+"win64":
        
       print(Fore.YELLOW)
       print("Wındowsda nmap olmadıgı ıcın program calısamaz ! ")
    if _platform == "linux" or _platform == "linux2":
        print(Fore.BLUE)
        print("Program calısabılır durumda ! ")
    
secim = input("Acık portları gormek ıcın oncelıkle hedef ip gırmelısın :")
os.system("nmap -sS -sV"+secim)

            
