from ast import Or
from cgi import test
import time
import pyautogui
import keyboard
import schedule
import PIL
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
from datetime import datetime
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

"""Cette versionde littlefinger nécessite d'avoir les images du bouton connecté et signer du wallet dans le même dossier que le script
J'utilise pour le moment pyautogui pour faire des click avec des coordonnées plutôt que des images sauf pour la vérification de déconnexion,
qui pourrais très bien se faire avec un pyautogui.pixel mais le but final du programme est d'être totalement autonome avec de la reconnaissance d'image
et d'inclure dans le futur un module de configuration ou l'utilisateur choisirait les zones sur lesquels il veut cliquer. 

Pour le moment il n'est configuré que pour Bombcrypto mais à venir littlefinger sera un véritable bot de clic qui simulera l'activité humaine et sera totalement personnalisable et exportable sur n"importe quel jeu/logiciel
Amélioration à venir : 
    _interface graphique
    _choix de stratégie pour BC 
    _utilisation de reconnaissance d'image pour le clic
    
"""
time.sleep(5)


    
def lancerCycle():
    print("cycle lancé", str(datetime.now()))           #permet de ce repérer dans la fenêtre de contrôle
    pyautogui.moveTo(2871,436)
    time.sleep(0.1)
    pyautogui.leftClick(2871,436)
    time.sleep(0.1)
    pyautogui.moveTo(2875,744)
    time.sleep(0.1) 
    pyautogui.leftClick(2875,744)   #click sur la petite fleche dans la fenetre de map
    time.sleep(2)
    pyautogui.moveTo(2868,721)
    time.sleep(0.1) 
    pyautogui.leftClick(2868,721)   #click sur l'image du chevalier
    time.sleep(30)# on laisse 30 sec entre le clic sur le chevalier et l'apparition du bouton ALL. Pourrais être corrigé dans une version qui utilise de la reconnaissance d'image pour toutes les actions
    pyautogui.moveTo(2785,323)
    time.sleep(0.1)
    pyautogui.leftClick(2785,323)   #click sur le bouton ALL
    time.sleep(2)
    pyautogui.moveTo(2931,279)
    time.sleep(0.1)
    pyautogui.leftClick(2931,279)   #click sur la petite croix rouge
    time.sleep(2)
    verifWork()
    time.sleep(2)
    pyautogui.moveTo(2893,436)
    time.sleep(0.1)
    pyautogui.leftClick(2893,436)   #click au centre de la map pour remettre tout le monde au taff
    time.sleep(0.1)
    pyautogui.leftClick(2893,436)   #deuxième click de sureté pour remettre au centre de la map, de temps en temps ça foire pour aucune raison

def verifWork():
    character = pyautogui.locateOnScreen('character3.png', confidence=0.9) 
    if character != None :
        pyautogui.leftClick(2785,323)   #click sur le bouton ALL
        time.sleep(2)
        pyautogui.moveTo(2931,279)
        time.sleep(0.1)
        pyautogui.leftClick(2931,279)   #click sur la petite croix rouge
        time.sleep(2)
        verifWork()

        
def earn(): #fonction pour savoir combien de Bcoin on a gagné
    coffre = pyautogui.locateOnScreen('coffre.png', confidence = 0.7)
    pyautogui.moveTo(coffre)
    time.sleep(0.1)
    pyautogui.click(coffre)
    time.sleep(2)
    earning = pyautogui.screenshot(region=(2818,351,300,50))
    earning.save(r"C:\Users\Yanis\Desktop\autocliker\screenshot.png")
    croix = pyautogui.locateOnScreen('croix.png', confidence = 0.7)
    pyautogui.moveTo(croix)
    time.sleep(0.1)
    pyautogui.leftClick(croix)
    print(pytesseract.image_to_string('screenshot.png'))
           
def antiAfk():
    print("Replace les héros")      #permet de ce repérer dans la fenêtre de contrôle
    pyautogui.leftClick(2436,197)   #click sur la flêche verte pour retour au menu principal
    time.sleep(0.1)
    pyautogui.leftClick(2871,436) #click sur le mode trésor adventure
    time.sleep(0.1)
    pyautogui.leftClick(2871,436)  #click sur le mode trésor adventure (clique de sécurité)

def verifafk(): #fonction qui vérifie si le jeu est passé en AFK
    print('verif', str(datetime.now()))
    erreurafk = pyautogui.locateOnScreen('afkbc.png', confidence=0.5)
    if erreurafk != None:
        print('on est afk')
        pressok = pyautogui.locateOnScreen('okafk.png', confidence=0.9)
        pyautogui.leftClick(pressok)
           
def disconnected(): # fonction de test de connexion
    
        
        connect = pyautogui.locateOnScreen('connectWallet.png', confidence=0.7) #variable qui prend en argument la recherche du bouton connection via une image
        control = 'test'
        
        if connect !=None:    #test si le prog a trouver le bouton = variable pas vide
            print("je vois le bouton, on est déco !") 
            pyautogui.leftClick(connect) #on se dirige vers le bouton connect
            """time.sleep(0.1)
            pyautogui.leftClick()""" #ça click
            time.sleep(20) # on utilise un repos de 20 seconde pour laisser le temps a la fenêtre MM de pop
            ConnectLogin = pyautogui.locateOnScreen('ConnectLogin.png', confidence=0.7)
            pyautogui.leftClick(ConnectLogin)
            time.sleep(20)
            
            
        signature = pyautogui.locateOnScreen('signerMM.png', confidence=0.9)
        if signature !=None :
            pyautogui.leftClick(signature)
            time.sleep(0.1)
            control = 1
            control = int
            time.sleep(2)
            print("c'est signé chef !")
            time.sleep(60)
            pyautogui.leftClick(2871,436)
            time.sleep(0.1)
            

            
        elif connect !=None and signature == None and control != 1:
            pyautogui.press('f5')
            
        else :
            print("On est connecté !")
            
           

def bombcrypto():
    print('ça commence', str(datetime.now()))
    time.sleep(480)
    verifafk()
    time.sleep(20)
    disconnected()
    time.sleep(30)
    lancerCycle()



schedule.every(1).hours.do(bombcrypto)
schedule.every(5).minutes.do(antiAfk)
    

while True:
    schedule.run_pending()
    time.sleep(1)

