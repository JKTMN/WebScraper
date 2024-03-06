from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#URL = "https://www.solent.ac.uk/courses/undergraduate/education-ba/2024/ba-hons-education-3-years-2024"

# class webCrawler():
#     def __init__(self, service, driver, URL, pagesList, emailAddressList):
#         self.service = service
#         self.driver = driver
#         self.URL = URL
#         self.pagesList = pagesList
#         self.emailAddressList = emailAddressList


#     def firstWebpage(self):
#         self.pagesList.append(input("Enter the target webpage: "))

#     def getNextPage(self):
#         self.driver.get(self.URL)
#         pages = self.driver.find_elements(By.TAG_NAME, "a")
#         for page in pages:
#             href = page.get_attribute("href")
#             if href and href.startswith("#") == False and href not in self.pagesList:
#                 self.pagesList.append(href) 
#             else:
#                 break 
#         return self.pagesList
    
#     def scrapeEmailAddresses(self):
#         self.driver.get("https://www.solent.ac.uk/courses/undergraduate/accountancy-and-finance-bsc/2024/bsc-hons-accountancy-and-finance-3-years-2024")
#         html = self.driver.page_source
#         soup = BeautifulSoup(html, "html.parser")
#         emailAddresses = soup.find_all(string=lambda text: "@" in text)
#         for emailAddress in emailAddresses:
#             if emailAddress and emailAddress not in self.emailAddressList:
#                 self.emailAddressList.append(emailAddress)
    
#     def openPageList(self):
#         for page in pagesList:
#             self.URL = page
#             self.getNextPage()
#             self.scrapeEmailAddresses()
#             self.openPageList()




# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# pagesList = []
# emailAddressList = []

# Crawler = webCrawler(service, driver, "", pagesList, emailAddressList)
# Crawler.firstWebpage()
# print(Crawler.scrapeEmailAddresses())


# while not pagesList:
#     for pageList in pagesList:
#         Crawler.getNextPage()
#         Crawler.scrapeEmailAddresses()
#         Crawler.openPageList()

### above is old code which stopped working

### trying to fix ciode below

class webCrawler():
    def __init__(self, service, driver, URL, pagesList):
        self.service = service
        self.driver = driver
        self.URL = URL
        self.pagesList = pagesList

    def firstWebpage(self): #sets the url to a user input
        self.URL = input("Enter the target webpage: ")

    def getNextPage(self):
        self.driver.get(self.URL) #searches for anchors within the loaded webpage
        pages = self.driver.find_elements(By.TAG_NAME, "a")

        for page in pages: #filters through anchors
            href = page.get_attribute("href") #finds anchors with links
            if href and href.startswith("#") == False and href not in self.pagesList: #checks to see if link is true and 
                #checks to see if the link starts with a "#" finally checks to see if duplicate
                self.pagesList.append(href) #adds link to the list of webpages
            else:
                break 
        return self.pagesList


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
pagesList = []

Crawler = webCrawler(service, driver, "", pagesList)
Crawler.firstWebpage()
print(Crawler.getNextPage())