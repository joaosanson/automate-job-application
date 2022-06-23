from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

ser = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

YOUR_EMAIL = ''
YOUR_PASSWORD = ''


driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000000&keywords=python%20developer&location=Mundial"
           "mente&sortBy=R")
driver.maximize_window()
sleep(3)

sign_in_btn = driver.find_element(By.XPATH, '/html/body/div[3]/a[1]')
sign_in_btn.click()

username = driver.find_element(By.ID, "username")
username.send_keys(YOUR_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(YOUR_PASSWORD)

sleep(1)

sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()

sleep(2)

experience_level = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div/button')
experience_level.click()
sleep(2)


estagio = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[1]/label/p/'
                                        'span[1]')
estagio.click()

junior = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[3]/label/p/'
                                       'span[1]')
junior.click()

sleep(2)

search = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/button[2]/span')
search.click()

sleep(3)

driver.maximize_window()

sleep(2)

list_of_jobs = driver.find_elements(By.CLASS_NAME, 'job-card-list__title')
for job in list_of_jobs:
    job.click()
    sleep(1)
    salvar = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/'
                                           'div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
    print(salvar.text)
    if salvar.text == "Salvar":
        sleep(2)
        salvar.click()

