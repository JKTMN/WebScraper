from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.bournemouth.ac.uk/study/undergraduate/courses/undergraduate-course-list")
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="ccc-notify-accept"]'))
    )
element.click()

# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.send_keys("Bournemouth University" + Keys.ENTER)

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Bournemouth University")
# link.click()


related_courses = driver.find_element(By.ID, "block-slices-slice-slice-related-courses-2")
courses = related_courses.find_elements(By.TAG_NAME, "a")

for course in courses:
    print(course.get_attribute("href"))

time.sleep(60)
driver.quit()