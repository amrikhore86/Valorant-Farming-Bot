print("Service Starting")
import pyautogui,time,cv2,keyboard

pyautogui.FAILSAFE=False

def bot():
    while True:
        time.sleep(0.5)
        if pyautogui.locateOnScreen('play.png',confidence=0.8,grayscale=True)!=None:
            time.sleep(0.5)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('play.png',confidence=0.8,grayscale=True)))
            print("Open Play Area")
            break
    
    while True:
        time.sleep
        if pyautogui.locateOnScreen('deathmatch.png',confidence=0.8,grayscale=True)!=None:
            time.sleep(0.5)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('deathmatch.png',confidence=0.8,grayscale=True)))
            print("Switching to deathmatch Mode")
            break
    
    while True:        
        if pyautogui.locateOnScreen('start.png',confidence=0.8,grayscale=True)!=None:
            time.sleep(0.5)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('start.png',confidence=0.8,grayscale=True)))
            print("Searching for match")
            break

def iterate():
    while True:
        if pyautogui.locateOnScreen('playagain.png',confidence=0.75,grayscale=True)!=None:
            time.sleep(0.5)
            time.sleep(0.5)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('playagain.png',confidence=0.75,grayscale=True)))
            print('Playing Again')
            break
        
def agent():
    while True:
        if pyautogui.locateOnScreen('agent.png',confidence=0.7,grayscale=True)!=None:
            time.sleep(0.25)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen("agent.png",confidence=0.75,grayscale=True)))
            time.sleep(0.2)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen("agent.png",confidence=0.75,grayscale=True)))
            if pyautogui.locateOnScreen('agent2.png',confidence=0.7,grayscale=True)!=None:
                time.sleep(0.25)
                pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen("agent2.png",confidence=0.75,grayscale=True)))
                time.sleep(0.2)
                pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen("agent2.png",confidence=0.75,grayscale=True)))
                
            print("Agent Choosed")
            break

        
#def buy():
#    while True:
#        keyboard.press('b')
#        if pyautogui.locateOnScreen('buy.png',confidence=0.8,grayscale=True)!=None:
#            time.sleep(0.25)
#            time.sleep(0.25)
#            if pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen('agent.png',confidence=0.7,grayscale=True)))
                
        
def antiafk():
    print("Now Playing Anti-Afk")
    while True:
        pyautogui.keyDown('ctrl')
        time.sleep(1)
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)
        pyautogui.keyDown("space")
        time.sleep(0.5)
        pyautogui.keyUp("space")
        time.sleep(0.5)
        if pyautogui.locateOnScreen('playagain.png',confidence=0.7,grayscale=True)!=None:
            break
        
            
itr=input('Enter the number of iteration. "0" if infinite or else a specific integer value e.g. 1,10,19 : ')

if itr=='0':
    while True:
        bot()
        #agent()
        while True:
            antiafk()
            iterate()
        
else:
    for i in range(itr):
        bot()
        antiafk()
        iterate()
        print("Completed")
