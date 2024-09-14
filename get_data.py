from selenium.webdriver.common.by import By
from chrome import Chrome

class GetData:

    def search_and_print_collage(self):
        driver = Chrome.chrome_driver(self)
        driver.get("https://www.tapmusic.net") #url do site
        driver.find_element(By.XPATH, '//*[@id="page-wrap"]/form/input[1]').send_keys('username') # passando o username
        driver.find_element(By.XPATH, '//*[@id="page-wrap"]/form/select[1]').send_keys('days/months') # o periodo de tempo
        driver.find_element(By.XPATH, '//*[@id="page-wrap"]/form/select[2]').send_keys('size') # passado o tamanho
        driver.find_element(By.XPATH, '//*[@id="page-wrap"]/form/input[2]').click() #submetendo colagem
        
        driver.save_screenshot("collage.png") # print da colagem 

GetData().search_and_print_collage()