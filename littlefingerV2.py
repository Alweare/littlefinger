from pickle import TRUE
from sqlite3 import connect
import time
import pyautogui
import schedule
import keyboard

time.sleep(5)

def click():
    pyautogui.leftClick()
    time.sleep(0.1)
 
 
while 1: 
    connect = pyautogui.locateOnScreen('connectWallet.png',confidence=0.7)
    
    if connect !=None:
        print("je vois")
        pyautogui.moveTo(connect)
        pyautogui.leftClick()
        
        time.sleep(20)
    else : 
        print("invisible")
    time.sleep(5)
    signature = pyautogui.locateOnScreen('signerMM.png',confidence=0.7)
    if signature !=None:
        pyautogui.moveTo(signature)
        pyautogui.leftClick()
        time.sleep(0.3)
        print("c'est signé chef !")
    else : 
        print("where am i ")

"""if connect is not None:
    pyautogui.moveTo(connect)
    click()"""
    
    
"""time.sleep(6)
pyautogui.click('signerMM.png')"""
