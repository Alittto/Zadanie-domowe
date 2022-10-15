import math


def v_szescian():
    a = float(input("podaj a: "))
    return a**3
    
def v_donut(r:float, R:float):
    return 2 * pi * 2 * r**2 * R


def  v_graniastoslup_trojkatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    H = float(input("podaj H: "))
    return (1/3) * a * h * H
    
    
    
def v_walec(r:float, h:float):
    return math.pi * r **2 * h

def v_kuli(r:float):
    return (4/3) * math.pi * r**3

def v_stozek(r:float, h:float):
    return (1/3) * math.pi * r**2 * h
    
    
    
def v_piramidy(a:float, h:float):
    return a**2 * h / 3


    



    
    
    
    