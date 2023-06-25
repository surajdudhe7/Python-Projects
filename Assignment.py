from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
webdriver_path = 'C:\Program Files (x86)\Google\Chrome\Application' 
chrome_options = Options()
chrome_options.add_argument('--headless')  
driver = webdriver.Chrome(service=Service(executable_path=webdriver_path), options=chrome_options)
driver.get('https://ceoelection.maharashtra.gov.in/searchlist/')
district_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ac')))
district_dropdown.send_keys('Select Any')
assembly_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ac')))
assembly_dropdown.send_keys('Select Any')
revision_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ssr')))
revision_dropdown.send_keys('SSR 2023')
language_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'language')))
language_dropdown.send_keys('Marathi')
part_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'part')))
part_dropdown.send_keys('Select Any')
captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'captcha')))
captcha_input.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(EC.url_contains('a.pdf'))
def automate_download(district):
    driver.get('https://ceoelection.maharashtra.gov.in/searchlist/')
    district_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ac')))
    district_dropdown.send_keys(district)
    input("Please enter the Captcha and press Enter to continue...")
    open_pdf_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'captcha'))) 
    open_pdf_button.send_keys(Keys.ENTER)
    time.sleep(5) 
driver.quit()
automate_download('Your District Name')