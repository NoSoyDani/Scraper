'''
Created on 18 ene. 2020

'''
import threading
import os
def eject1():
    exec(os.system("party.py"))
def eject2():
    os.system("Scraper.py")

THT = threading.Thread(target=eject1)
THT2 = threading.Thread(target=eject2)
THT.start()
THT2.start()
