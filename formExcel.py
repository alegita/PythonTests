# Imports
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

with open('FormTestExcel.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
        browser.maximize_window()
        time.sleep(2)
        first_name = browser.find_element(By.ID, "input-firstname")
        first_name.send_keys(line[0])
        last_name = browser.find_element(By.ID, "input-lastname")
        last_name.send_keys(line[1])       
        email = browser.find_element(By.ID, "input-email")
        email.send_keys(line[2])
        telephone = browser.find_element(By.ID, "input-telephone")
        telephone.send_keys(line[3])
        password = browser.find_element(By.ID, "input-password")
        password.send_keys(line[4])
        password_confirm = browser.find_element(By.ID, "input-confirm")  
        password_confirm.send_keys(line[5])
        newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-no']")
        newsletter.click()
        terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
        terms.click()	
        continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
        continue_button.click()