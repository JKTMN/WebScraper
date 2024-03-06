from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#URL = "https://www.solent.ac.uk/courses/undergraduate/education-ba/2024/ba-hons-education-3-years-2024"

class webCrawler():
    def __init__(self, service, driver, URL, pagesList, emailAddressList):
        self.service = service
        self.driver = driver
        self.URL = URL
        self.pagesList = pagesList
        self.emailAddressList = emailAddressList
        self.pagesOpened = 0

    def firstWebpage(self):
        self.URL = input("Enter the target webpage: ")

    def getNextPage(self):
        self.driver.get(self.URL)
        pages = self.driver.find_elements(By.TAG_NAME, "a")
        for page in pages:
            href = page.get_attribute("href")
            if href and not href.startswith("#") and href not in self.pagesList:
                self.pagesList.append(href) 
                self.pagesOpened += 1
            if self.pagesOpened >= 10:  # Check if 10 pages are visited
                break
        return self.pagesList
    
    def scrapeEmailAddresses(self):
        self.driver.get(self.URL)
        html = self.driver.page_source  # Fixed: Changed 'driver' to 'self.driver'
        soup = BeautifulSoup(html, "html.parser")
        emailAddresses = soup.find_all(string=lambda text: "@" in text)
        for emailAddress in emailAddresses:
            if emailAddress and emailAddress not in self.emailAddressList:
                self.emailAddressList.append(emailAddress.text)

    def openPageList(self):
        for page in self.pagesList:
            self.URL = page
            self.scrapeEmailAddresses()
            self.getNextPage()

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

pagesList = []
emailAddressList = []

Crawler = webCrawler(service, driver, "", pagesList, emailAddressList)
Crawler.firstWebpage()
Crawler.getNextPage()
Crawler.openPageList()
print("Email addresses are:")
print(str(Crawler.emailAddressList))

### above is old code which stopped working

### trying to fix ciode below

# class webCrawler():
#     def __init__(self, service, driver, URL, pagesList, emailAddressList):
#         self.service = service
#         self.driver = driver
#         self.URL = URL
#         self.pagesList = pagesList
#         self.emailAddressList = emailAddressList

#     def firstWebpage(self): #sets the url to a user input
#         self.URL = input("Enter the target webpage: ")

#     def getNextPage(self):
#         self.driver.get(self.URL) #searches for anchors within the loaded webpage
#         pages = self.driver.find_elements(By.TAG_NAME, "a")

#         for page in pages: #filters through anchors
#             href = page.get_attribute("href") #finds anchors with links
#             if href and href.startswith("#") == False and href not in self.pagesList: #checks to see if link is true and 
#                 #checks to see if the link starts with a "#" finally checks to see if duplicate
#                 self.pagesList.append(href) #adds link to the list of webpages
#             else:
#                 break 
#         return self.pagesList
    
#     def scrapeEmailAddresses(self):
#         self.driver.get(self.URL)
#         html = driver.page_source
#         driver.close()
#         soup = BeautifulSoup(html, "html.parser")
#         emailAddresses = soup.find_all(string=lambda text: "@" in text)
#         for emailAddress in emailAddresses:
#             if emailAddress and emailAddress not in self.emailAddressList:
#                 self.emailAddressList.append(emailAddress.text)
#         return self.emailAddressList


# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# pagesList = []
# emailAddressList = []

# Crawler = webCrawler(service, driver, "", pagesList, emailAddressList)
# Crawler.firstWebpage()
# print(Crawler.scrapeEmailAddresses())