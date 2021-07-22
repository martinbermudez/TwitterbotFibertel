from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

WEB_DRIVER = r"C:\Users\Martin\Desktop\Python\Selenium Bot\chromedriver.exe"
TWITTER_USER = "honestfibertel1"
TWITTER_PASS = "*************"
TWITTER_AT = "@CableFibertel"
BAJADA_ESTIMADA = 300

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
#driver = webdriver.Chrome(options=options, executable_path=WEB_DRIVER)

class TwitterBot():
    # Inicializador del objeto
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=options, executable_path=WEB_DRIVER)
        self.subida = 0
        self.bajada = 0
    
    #Obtener datos de speedtest
    def get_velocidad_internet(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element_by_class_name('start-button')
        start_button.click()
        time.sleep(60)
        self.subida = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.bajada = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    
    #Logueo en Twitter
    def login_twitter(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        campo_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        campo_user.send_keys(TWITTER_USER)
        campo_pass = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        campo_pass.send_keys(TWITTER_PASS)
        time.sleep(2)
        campo_pass.send_keys(Keys.ENTER)
        time.sleep(3)
        self.tweet_queja()
        time.sleep(5)
        self.driver.quit()

    #Armado de tweet y posteo
    def tweet_queja(self):
        tweet_board = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f'Se obtuvo una descarga de {self.subida}Mbps de bajada y unos {self.bajada}Mbps de subida. Con un plan de {BAJADA_ESTIMADA}Mbps.'
        tweet_board.send_keys(tweet)
        tweet_send = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_send.click()
        
bot = TwitterBot(WEB_DRIVER)
bot.get_velocidad_internet()
#print(bot.subida, bot.bajada)
bot.login_twitter()