from cgi import test
import time
import pyautogui
import keyboard
import schedule


    
"""def hello():
    print("test de fonction")"""
    

def lancerCycle():
    print("cycle lancer")
    pyautogui.leftClick(2884,736)
    time.sleep(2)
    pyautogui.leftClick(2885,746)
    time.sleep(30)
    pyautogui.leftClick(2797,315)
    time.sleep(2)
    pyautogui.leftClick(2933,275)
    time.sleep(2)
    pyautogui.leftClick(2893,436)
    
def antiAfk():
    print("Pas d'afk")
    pyautogui.leftClick(2443,193)
    time.sleep(0.1)
    pyautogui.leftClick(2883,434)

"""schedule.every(5).seconds.do(hello)"""
schedule.every(10).minutes.do(antiAfk)
schedule.every(2).hours.do(lancerCycle)

while True:
    schedule.run_pending()
    time.sleep(1)

