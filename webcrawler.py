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

    def firstWebpage(self): #sets url to user input
        self.URL = input("Enter the target webpage: ")

    def getNextPage(self):
        self.driver.get(self.URL)
        anchors = self.driver.find_elements(By.TAG_NAME, "a") #finds all anchors within the loaded webpage
        for anchor in anchors: #filters through the webpages
            link = anchor.get_attribute("href") #checks to see if anchor has 
            if link and not link.startswith("#") and link not in self.pagesList: #check to see if link is true
                #then checks to see if the link starts with a "#" and then checks to see if the link is already stored
                self.pagesList.append(link) #adds link to list
                self.pagesOpened += 1 #increments counter
            if self.pagesOpened >= 10:  #check to see if 10 pages are visited
                break
        return self.pagesList
    
    def scrapeEmailAddresses(self):
        self.driver.get(self.URL)
        html = self.driver.page_source  #sets a variable to be the webpage source
        soup = BeautifulSoup(html, "html.parser") #uses bs4 to parse the html
        emailAddresses = soup.find_all(string=lambda text: "@" in text) #searches the html to find strings containing "@"
        for emailAddress in emailAddresses: #filters through found email address
            if emailAddress and emailAddress != "" and emailAddress not in self.emailAddressList:
                #checks to see if emailadress is true, it is not empty and not already stores
                self.emailAddressList.append(emailAddress.text) #stores email adress

    def openPageList(self):
        for page in self.pagesList: #filters through the links 
            self.URL = page #sets the new url to the next link stored in the list
            self.scrapeEmailAddresses() #calls the scrapeEmailAddress function
            self.getNextPage() #calls the getNextPage function

#inititating selenium objects
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#initiating empty lists
pagesList = []
emailAddressList = []

#initiating object and calling functions
Crawler = webCrawler(service, driver, "", pagesList, emailAddressList)
Crawler.firstWebpage()
Crawler.getNextPage()
Crawler.openPageList()
print("Email addresses are:")
print(Crawler.emailAddressList)
print(Crawler.pagesList)

#Issues
##duplicate links stored
##empty email addresses stored

#ideas
##create variation of this where it stores the links to the courses instead of any link to webpage