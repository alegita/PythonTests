from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 	
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
browser.maximize_window()
first_name = browser.find_element(By.ID, "input-firstname")
last_name = browser.find_element(By.ID, "input-lastname")
telephone = browser.find_element(By.ID, "input-telephone")
email = browser.find_element(By.ID, "input-email")
password = browser.find_element(By.ID, "input-password")
password_confirm = browser.find_element(By.ID, "input-confirm")
first_name.send_keys("FirstName")
last_name.send_keys("LastName")
email.send_keys("erybzc2fss@exa1.com")
telephone.send_keys("+351999888777")
password.send_keys("123456")
password_confirm.send_keys("123456")
newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-no']")
newsletter.click()
terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
terms.click()	
continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
continue_button.click() 	
assert browser.title == "Your Account Has Been Created!" 
