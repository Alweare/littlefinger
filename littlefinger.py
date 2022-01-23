from cgi import test
import time
import pyautogui
import keyboard
import schedule

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

def lancerCycle():
    print("cycle lancé")            #permet de ce repérer dans la fenêtre de contrôle
    pyautogui.leftClick(2884,736)   #click sur la petite fleche dans la fenetre de map
    time.sleep(2)
    pyautogui.leftClick(2885,746)   #click sur l'image du chevalier
    time.sleep(30)                  # on laisse 30 sec entre le clic sur le chevalier et l'apparition du bouton ALL. Pourrais être corrigé dans une version qui utilise de la reconnaissance d'image pour toutes les actions
    pyautogui.leftClick(2797,315)   #click sur le bouton ALL
    time.sleep(2)
    pyautogui.leftClick(2933,275)   #click sur la petite croix rouge
    time.sleep(2)
    pyautogui.leftClick(2893,436)   #click au centre de la map pour remettre tout le monde au taff
    time.sleep(0.1)
    pyautogui.leftClick(2883,434)   #deuxième click de sureté pour remettre au centre de la map, de temps en temps ça foire pour aucune raison
    
def antiAfk():
    print("Replace les héros")      #permet de ce repérer dans la fenêtre de contrôle
    pyautogui.leftClick(2443,193)   #click sur la flêche verte pour retour au menu principal
    time.sleep(0.1)
    pyautogui.leftClick(2883,434) #click sur le mode trésor adventure
    time.sleep(0.1)
    pyautogui.leftClick(2883,434)  #click sur le mode trésor adventure (clique de sécurité)

def disconnected():
    connect = pyautogui.locateOnScreen('connectWallet.png',confidence=0.7) #variable qui prend en argument la recherche du bouton connection via une image
    
    
    if connect !=None:    #test si le prog a trouver le bouton = variable pas vide
        print("je vois le bouton") 
        pyautogui.moveTo(connect) #on se dirige vers le bouton connect
        pyautogui.leftClick() #ça click
        time.sleep(20) # on utilise un repos de 20 seconde pour laisser le temps a la fenêtre MM de pop
        signature = pyautogui.locateOnScreen('signerMM.png',confidence=0.7)
        pyautogui.moveTo(signature)
        pyautogui.leftClick()
        time.sleep(0.3)
        print("c'est signé chef !")
    else :
        print("On est connecté !")
    
schedule.every(5).minutes.do(disconnected)
schedule.every(12).minutes.do(antiAfk)
schedule.every(2).hours.do(lancerCycle)
    




while True:
    schedule.run_pending()
    time.sleep(1)

