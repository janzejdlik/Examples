from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller
import time
import pyautogui
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
import requests
from bs4 import BeautifulSoup


# Launch Firefox
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.name-generator.org.uk/instagram/")


# Accept Cookies 
time.sleep(2)
driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div[2]/div/button[3]/span").click()
time.sleep(2)


# Generate and copy first name
driver.find_element(By.XPATH, "//html/body/div[3]/div[1]/div[2]/div[3]/div/div/form/input[9]").click()
driver.find_element(By.XPATH, "//html/body/div[3]/div[1]/div[2]/div[3]/div/div/form/div[1]").click()
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('command', 'c')
name1 = pyperclip.paste()
time.sleep(1)


# Generate and copy second name
driver.find_element(By.XPATH, "//html/body/div[3]/div[1]/div[2]/div[3]/div/div/form/input[13]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//html/body/div[3]/div[1]/div[2]/div[3]/div/div/form/input[12]").click()
time.sleep(1)
pyautogui.hotkey('command', 'a')
time.sleep(1)
pyautogui.hotkey('command', 'c')
name2 = pyperclip.paste()


with open("outputnames.txt", "w") as file:
    file.write(name1 + "\n")
    file.write(name2)


# Password generator
driver.get("https://www.avast.com/random-password-generator#mac")
time.sleep(1)


# Accept cookies
for i in range(3):
    pyautogui.press("tab")
pyautogui.press("enter")

# Copy text and paste into password file 
driver.find_element(By.XPATH, "//html/body/div[4]/div[3]/div/section/div/div[2]/div[1]/div[1]/div[1]").click()

pyautogui.hotkey('command', 'c')
time.sleep(1)

password = pyperclip.paste()
time.sleep(1)



with open("password.txt", "w") as file:
        file.write(name2)


# Yandex email creation
driver.get("https://mail.yandex.com/")
driver.find_element(By.XPATH, "//html/body/div/div/div/div[3]/section[1]/div/a[1]").click()

# Name
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/span").click()
pyautogui.typewrite(name1)

# Last name
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[2]").click()
pyautogui.typewrite(name2)

# Login name
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[3]").click()
pyautogui.typewrite(name1 + name2)

# Password
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[1]").click()
pyautogui.typewrite(password)

# Confirm password
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[2]").click()
pyautogui.typewrite(password)

# Mobile phone number
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]").click()
pyautogui.typewrite("phone number")

# Register button
driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/main/div/div/div/form/div[4]").click()


time.sleep(3)
driver.quit()
