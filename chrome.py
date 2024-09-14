from selenium import webdriver
from selenium.webdriver.common.by import By

class Chrome:
    
    def chrome_driver(self):
            chromeoptions = webdriver.ChromeOptions()
            chromeoptions.add_argument('--ignore-certificate-errors')
            chromeoptions.add_argument('--ignore-ssl-errors')
            chromeoptions.add_argument("--headless")
            return webdriver.Chrome(options=chromeoptions)