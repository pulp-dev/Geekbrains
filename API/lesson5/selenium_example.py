from selenium import webdriver
import requests

DRIVER_PATH = r"./geckodriver/geckodriver.exe"
url = "https://www.google.com/"

options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")


driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
driver.get(url)
