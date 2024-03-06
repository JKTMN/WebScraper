from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


def get_email(URL):
    driver.get(URL)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, "html.parser")
    email_elements = soup.find_all(string=lambda text: "@" in text)
    for email in email_elements:
        print(email.text)


get_email("https://www.solent.ac.uk/courses/undergraduate/education-ba/2024/ba-hons-education-3-years-2024")