from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/me/Documents/development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
buy_cursor = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
buy_factory = driver.find_element(By.ID, "buyFactory")
buy_mine = driver.find_element(By.ID, "buyMine")
buy_shipment = driver.find_element(By.ID, "buyShipment")
buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
buy_portal = driver.find_element(By.ID, "buyPortal")
buy_time_machine = driver.find_element(By.ID, "buyTime machine")

timeout = time.time() + 60*5
while time.time() < timeout:
    cookie.click()
    if time.time() % 5 == 0:
        buy_time_machine.click()
        buy_portal.click()
        buy_alchemy_lab.click()
        buy_shipment.click()
        buy_mine.click()
        buy_factory.click()
        buy_grandma.click()
        buy_cursor.click()