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
 
 
"""while 1: 
    connect = pyautogui.locateOnScreen('connectWallet.png',confidence=0.7) #variable qui prend en argument la recherche du bouton connection via une image
    
    if connect !=None:    #test si le prog a trouver le bouton = variable pas vide
        print("je vois") 
        pyautogui.moveTo(connect) #on se dirige vers le bouton connect
        pyautogui.leftClick() #ça click
        time.sleep(20) # on utilise un repos de 20 seconde pour laisser le temps a la fenêtre MM de pop
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
        print("where am i ")"""

def cycle():
    depart = pyautogui.locateOnScreen('fleche.png',confidence=0.8)
    hero = pyautogui.locateOnScreen('hero.png',confidence=0.8)
    work = pyautogui.locateOnScreen('all.png',confidence=0.8)
    sorti = pyautogui.locateOnScreen('croix.png',confidence=0.8)

        
    pyautogui.moveTo(depart)
    click()
    time.sleep(2)
        
    pyautogui.moveTo(hero)
    click()
    time.sleep(5)

    pyautogui.moveTo(work)
    click()
    time.sleep(5)

    pyautogui.moveTo(sorti)
    click()
    time.sleep(2)

"""   pyautogui.leftClick(2856,497)
click()"""
    
schedule.every(10).seconds.do(cycle)

while True:
    schedule.run_pending()
    time.sleep(1)
    