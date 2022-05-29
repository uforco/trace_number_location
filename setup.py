import time
import subprocess
import sys
import os
from turtle import right
from unittest import result
from lib.sca_studio import *
from lib.loss_in_site.letbee import *
from lib.loss_in_site.checkboll.dont_dot.main_loca.pack_loca import *
#packge check 
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
# print(installed_packages)
# print(type(installed_packages))
#print("pyfiglet" not in installed_packages)
# if "os" not in installed_packages:
#     print("install in os packages")
#     subprocess.run("pip install os")
if "python-decouple" not in installed_packages:
    print("install in python-decouple packages")
    subprocess.run("pip install python-decouple")
if "pyfiglet" not in installed_packages:
    print("install in pyfiglet packages")
    subprocess.run("pip install pyfiglet")
if "phonenumbers" not in installed_packages:
    print("install in phonenumbers packages")
    subprocess.run("pip install phonenumbers")
if "opencage" not in installed_packages:
    print("install in opencage packages")
    subprocess.run("pip install opencage")
if "folium" not in installed_packages:
    print("install in folium packages")
    subprocess.run("pip install folium")
if "numpy" not in installed_packages:
    print("install in numpy packages")
    subprocess.run("pip install numpy")
else:
    #print("pro")
    #def sca
    sca1()
    '''
       _____      __              _
      / ___/_____/ /______ _     (_)___  __  __
      \__ \/ ___/ //_/ __ `/    / / __ \/ / / /
     ___/ / /  / ,< / /_/ /    / / /_/ / /_/ /
    /____/_/  /_/|_|\__,_/  __/ /\____/\__, /
                           /___/      /____/
           ____
          / __ )__  __
         / __  / / / /
        / /_/ / /_/ /
       /_____/\__, /
             /____/
        __
       / /   ___  ____  ___
      / /   / _ \/_  / / _ \
     / /___/  __/ / /_/  __/
    /_____/\___/ /___/\___/

    '''
    print(""" 
        Hi, Srka joy 
    Please Enter App Password !""")
    checktoOut = beckthink()
    if checktoOut == lossp() :
        print("\n     Try Again")
        #time.sleep(0.2)
        subprocess.run("py .\setup.py")
    elif checktoOut == blockoff() :
        print("\n   please wait Close This Program\n          Exit By Tools\n")
        time.sleep(2)
        exit()
    elif checktoOut != passtokay () :
        print("\n   Wrong Password")
        time.sleep(0.1)
        subprocess.run("py .\setup.py")
    else:
        sca2()
        offbrack_f ()
        re_mapfile ()