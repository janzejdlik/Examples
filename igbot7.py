from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pyautogui
import time


# Launch Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Login navigation
for i in range(7):
    pyautogui.press('tab')

pyautogui.press('enter')

# Find username and password fields and enter login information
for i in range(2):
    pyautogui.press('tab')

time.sleep(2)

# Enter username
pyautogui.typewrite('username')

# Find password field and set password as input
for i in range(1):
    pyautogui.press('tab')

pyautogui.typewrite("password")

for i in range(2):
    pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(5)

# Accept cookies 
pyautogui.click(x=1250, y=700)

time.sleep(3)

pyautogui.click(x=1250, y= 850)

time.sleep(2)

pyautogui.click(x=100, y=270)

pyautogui.sleep(2)

# Click on search bar
pyautogui.press('/')

with open('ignames.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pyperclip.copy(line)

        # Paste the name and click on the first person
        pyautogui.sleep(2)
        pyautogui.hotkey('command', 'v')
        pyautogui.sleep(2)
        pyautogui.click(x=115, y=288)
        pyautogui.sleep(2)

        # Give Follow
        for i in range(1):
            pyautogui.press('tab')

        pyautogui.press('enter')

        pyautogui.press('enter')

        pyautogui.sleep(2)

        # Message send button
        pyautogui.click(x=1500, y= 135)

        pyautogui.sleep(4)

        # Notification approval
        pyautogui.sleep(2)
        pyautogui.click(x=1339, y= 790)

        # Message send 
        pyautogui.sleep(2)
        pyautogui.click(x=1400, y= 1235)
        pyautogui.sleep(2)
        pyautogui.typewrite("Zdarec, jak se dneska mame?:)")
        pyautogui.sleep(2)
        pyautogui.click(x=1733, y= 1235)

        # Click on search bar
        pyautogui.sleep(2)
        pyautogui.click(x=120, y= 270)

