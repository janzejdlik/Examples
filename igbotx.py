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


# Launch Firefox
driver = webdriver.Firefox()
driver.maximize_window()


# Navigate to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)


# Login navigation
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]").click()
time.sleep(2)


# Find username field and enter username
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").click()
pyautogui.typewrite('username')


# Find password field and set password as input
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input").click()
pyautogui.typewrite("password")
time.sleep(2)

# Login button click
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
time.sleep(8)



# Accept cookies 
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
time.sleep(2)


# Click on search bar
pyautogui.press('/')


with open('ignames.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pyperclip.copy(line)

        # Paste the name and click on the first person

        # Click on search bar
        pyautogui.sleep(2)
        pyautogui.hotkey('command', 'v')
        pyautogui.sleep(2)
        # Mouse click might work #
        pyautogui.click(x=250, y=280)
        #driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[1]/span/div/span").click()
        pyautogui.sleep(2)

        # Follow button click
        driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div[1]").click()
        pyautogui.press('enter')

        # Check if message button is present
        try:
            message_button = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div")
            message_button.click()
            pyautogui.sleep(4)

            # Message send 
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").click()
            pyautogui.sleep(2)
            pyautogui.typewrite("Zdarec, jak se dneska mame?:)")
            pyautogui.sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div").click()
        except NoSuchElementException:
            pass

        # Click on search bar
        pyautogui.sleep(2)
        pyautogui.click(x=40, y=266)

        #driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div/svg").click()


# Quits Firefox 
driver.quit()
