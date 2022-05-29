import random
from pyfiglet import Figlet
def sca1 ():
    #sca1 studio
    f = Figlet(font='slant')
    mass = f.renderText('Srka joy\n     By\n  Leze')
    print(mass)
def sca2 ():
    f15toall = ["isometric1", "univers", "stop", "starwars", "slant", 
                "smisome1", "sblood", "roman", "epic", "dotmatrix", 
                "doh", "block", "binary", "banner3", "bubble"]
    f15tor  = random.randint(0,14)
    cfornt = f15toall[f15tor]
    f2 = Figlet(font= cfornt)
    ler = ["LOCATION", "SHARIF", "PYTHON", "Lazzy", "Uforcode", "SrkaJoy", "getPont", "Password", "Not Try", "Push"]
    rend  = random.randint(0,9)
    #print(rend)
    #print(ler[rend])
    massloop = ler[rend]
    #print(massloop)
    mass2 = f2.renderText(massloop)
    print(mass2)