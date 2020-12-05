print("Service Starting")
import pyautogui,time,cv2,keyboard

pyautogui.FAILSAFE=False

def bot():
    while True:
        if pyautogui.locateOnScreen('play.png',confidence=0.8,grayscale=True)!=None:
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('play.png',confidence=0.8,grayscale=True)))
            print("Open Play Area")
            break
    
    while True:
        if pyautogui.locateOnScreen('deathmatch.png',confidence=0.8,grayscale=True)!=None:
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('deathmatch.png',confidence=0.8,grayscale=True)))
            print("Switching to Deatchmatch Mode")
            break
    
    while True:        
        if pyautogui.locateOnScreen('start.png',confidence=0.8,grayscale=True)!=None:
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('start.png',confidence=0.8,grayscale=True)))
            print("Searching for match")
            break
        
    time.sleep(5)
    
def iterate():
    while True:
        if pyautogui.locateOnScreen('playagain.png',confidence=0.8,grayscale=True)!=None:
            time.sleep(0.25)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('playagain.png',confidence=0.8,grayscale=True)))
            print('Playing Again')
            break
        
def antiafk():
    print("Now Playing Anti-Afk")
    while True:
        keyboard.press('Ctrl')
        time.sleep(1)
        if pyautogui.locateOnScreen('playagain.png',confidence=0.8,grayscale=True)!=None:
            break
        
            
itr=input('Enter the number of iteration. "0" if infinite or else a specific integer value e.g. 1,10,19 : ')

if itr=='0':
    while True:
        bot()
        antiafk()
        iterate()
        
else:
    for i in range(itr):
        bot()
        antiafk()
        iterate()
        
    