from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller
import time
import pyautogui


# Launch Firefox
driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# mouse = Controller()
# mouse.position = (1200,1070)

for i in range(7):
    pyautogui.press('tab')

pyautogui.press('enter')


# Find username and password fields and enter login informatio

for i in range(2):
    pyautogui.press('tab')

time.sleep(2)


# pyautogui.keyDown('command')
# time.sleep(5)
# pyautogui.keyUp('command')
	# pyautogui.hotkey('space')

pyautogui.typewrite('username')


# Find password field and set password as input

for i in range(1):
    pyautogui.press('tab')

pyautogui.typewrite("password")


# pyautogui.keyDown('command')
# time.sleep(5)
# pyautogui.keyUp('command')
# pyautogui.hotkey('space')


for i in range(2):
	pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(5)

#save_info_button = driver.find_element_by_css_selector('button.save-info')
#save_info_button.click()

pyautogui.click(x=1250, y=700)

time.sleep(3)

pyautogui.click(x=1250, y= 850)

time.sleep(2)

pyautogui.click(x=100, y=270)

pyautogui.typewrite(name)

with open('ignames.txt', 'r') as source_file:
    source_file = source_file.readlines()
    names = source_file.read()
 
    line_one = source_file[0].strip()
    line_after = source_file[+1].strip()
    print (line_one)
    print (line_after)

for line in source_file[2:]:
    print(line.strip())
    

pyautogui.typewrite(names, interval=0.1)


pyaurogui.press('tab')
pyaurogui.press('enter')


pyautogui.press('enter')


