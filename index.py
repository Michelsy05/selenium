from pprint import pprint
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pprint import pprint
import time 

def dbON():
    return 0

def dbSQL(sql):
    return 0

def dbOFF():
    return 0

driver = webdriver.Chrome('./chromedriver')
tw = []

def waitUntilReady(driver, delay, by, value_by):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, value_by)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

def index(user):
    driver.get("https://twitter.com/" + user)
    waitUntilReady(driver, 5, By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
    pprint(elements)
    setTW(elements)

def updateTable():
    sql = "INSERT INTO tw (nom, user, text, date) VALUES "
    values = ""

def optenerTextDelTweet(e):
    text = ""
    return text

def setTW(elements):
    for e in elements:
        tw.append(
            optenerTextDelTweet(e)
        )

#driver.close()
index("@Minecraft")