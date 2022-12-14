import colorama
from colorama import Fore, Style

print(Fore.GREEN + " Hello World")

import os

os.system('')


def RGB(red=None, green=None, blue=None, bg=False):
    if (bg == False and red != None and green != None and blue != None):
        return f'\u001b[38;2;{red};{green};{blue}m'
    elif (bg == True and red != None and green != None and blue != None):
        return f'\u001b[48;2;{red};{green};{blue}m'
    elif (red == None and green == None and blue == None):
        return '\u001b[0m'


g0 = RGB()
g1 = RGB(150, 50, 0)
g2 = RGB(0, 100, 0, True) + "" + RGB(100, 255, 100)
g3 = RGB(0, 255, 0, True) + "" + RGB(0, 50, 0)
print(g1)
print(f"{g1}green1{g0}")
print(f"{g2}green2{g0}")
print(f"{g3}green3{g0}")
