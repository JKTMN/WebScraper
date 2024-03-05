from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = input("Enter URL: ")

driver.get(url)

html = driver.page_source

next_page = driver.find_element(By.TAG_NAME, "a")

driver.close()

soup = BeautifulSoup(html, "html.parser")

email_elements = soup.find_all(string=lambda text: "@" in text)

for email in email_elements:
    print(email.text)

