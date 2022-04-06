"""
Requirements:

    PSI unlocked and chosen
    Auto Start on
    Start on Homescreen
    No saved Progress
"""


from pydirectinput import press
from pyautogui import moveTo, click
from time import sleep, time
import webbrowser

targetings = {
    "first": 0,
    "last" : 1,
    "close": 2,
    "strong": 3
}
pos_Start = (950, 1000) # start button on welcome to btd6 screen
pos_Play = (820, 938) # play button on home screen
pos_Beginner = (570, 1000) # beginner Maps
pos_Expert = (1335, 975) # navigate to expert Maps
pos_Map = (530, 580) # pos of Infernal Map
pos_Easy = (600, 400) # easy difficulty
pos_Deflation = (1280, 450) # deflation
pos_Deflation_Info_Ok = (950, 750) # click ok for the info text in deflation
pos_Start_Button = (1840, 1040) # start round
pos_Next = (950, 910) # next button in victory screen
pos_Home = (700, 850) # return to home button
pos_Nothing = (100, 100) # during game where nothing is placed
pos_Heroes = (610, 960) # heroes button on home screen
pos_Heroes_PSI = (965, 980) # pos of psi in hero select screen
pos_Heroes_Select = (650, 665) # select button of hero selection

pos_PSI = (70, 580)
pos_Boom1 = (830, 770)
pos_Boom2 = (830, 300)
pos_Sub1 = (488, 806)
pos_Sub2 = (1175, 242)
pos_Dart1 = (834, 366)
pos_Dart2 = (832, 695)

def select_game():
    click(pos_Play)
    sleep(0.3)
    click(pos_Beginner)
    sleep(0.1)
    click(pos_Expert)
    sleep(0.1)
    click(pos_Map)
    sleep(0.3)
    click(pos_Easy)
    sleep(0.3)
    click(pos_Deflation)
    sleep(5)
    click(pos_Deflation_Info_Ok)
    sleep(1)
    
def place_tower(hotkey, pos, upgrade = (0, 0, 0), target = "first"):
    press(hotkey)
    moveTo(pos)
    click()
    
    if upgrade != (0, 0, 0) or target != "first":
        click()
        
    if upgrade != (0, 0, 0):
        for _ in range(upgrade[0]):
            press(',')
        for _ in range(upgrade[1]):
            press('.')
        for _ in range(upgrade[2]):
            press('/')
            
    if target != "first":
        n = targetings[target]
        for _ in range(n):
            press('tab')
    
def setup():
    place_tower('u', pos_PSI, target = "strong")
    place_tower('w', pos_Boom1, (4, 0, 2))
    place_tower('w', pos_Boom2, (4, 0, 2))
    place_tower('x', pos_Sub1, (0, 2, 3))
    place_tower('x', pos_Sub2, (0, 2, 3))
    place_tower('q', pos_Dart1, (0, 2, 3))
    place_tower('q', pos_Dart2, (0, 2, 4))
    press('esc')
    sleep(0.1)
    
def start():
    click(pos_Start_Button)
    click(pos_Start_Button)
    
def end():
    click(pos_Next)
    sleep(0.5)
    click(pos_Home)
    sleep(4)
    
def sleep_and_click(seconds):
    for _ in range(seconds // 5):
        click(pos_Nothing)
        click(pos_Nothing)
        sleep(5)
    
def start_farming():
    t0 = time()
    i = 0
    money_earned = 0
    
    sleep(2)
    
    while True:
        i += 1
        select_game()
        setup()
        start()
        sleep_and_click(340) # 5 min 50 s
        end()
        money_earned += 66
        
        print(("ROUND " + str(i)).ljust(30))
        print("TIME PASSED:".ljust(30), end = "")
        print(round(time() - t0, 2), "s", sep="")
        print("MONKEY MONEY EARNED:".ljust(30), end = "")
        print(money_earned, "$", sep="")
        
def start_game():
    url = "steam://rungameid/960090"
    webbrowser.open(url)
    sleep(10)
    
def enter_game():
    click(pos_Start) # skip animation
    sleep(1)
    click(pos_Start) # press start
    sleep(5)
    
def select_hero():
    click(pos_Heroes)
    sleep(1)
    click(pos_Heroes_PSI)
    sleep(1)
    click(pos_Heroes_Select)
    sleep(1)
    press("ESC")
    sleep(1)
    
def main():
    start_game()
    enter_game()
    select_hero()
    start_farming()
    
if __name__ == "__main__":
    main()