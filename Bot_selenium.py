#IMPORTAR LIBRERÍAS
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


settings = Options()
settings.add_argument("--start-maximized")
init = webdriver.Chrome(options=settings)

init.get("https://www.youtube.com/")
time.sleep(10)

Search_input= WebDriverWait(init, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')))
Search_input.send_keys("#RutinasNCMotivacionGym/ Rompiendo los limites!")

Search_botton= WebDriverWait(init, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon/yt-icon-shape/icon-shape/div')))
Search_botton.click()
time.sleep(10)
