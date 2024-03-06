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

### gets list of courses
# related_courses = driver.find_element(By.ID, "block-slices-slice-slice-related-courses-2")
# courses = related_courses.find_elements(By.TAG_NAME, "a")
# for course in courses:
#     print(course.text)


### gets list of departments
# department = driver.find_elements(By.CSS_SELECTOR, "#block-slices-slice-slice-related-courses-2 .related-items-title h4")
# for department in department:
#     print(department.text)


###gets list of courses from predefined department
# department = driver.find_element(By.XPATH, '//div[h4[text()="Computing & Informatics"]]/following-sibling::div')
# courses = department.find_elements(By.TAG_NAME, "a")
# for course in courses:
#     print(course.text)


### Asks user what department they would like to search for
# while True:
#     select_department = input("What department would you like to search for: ")
#     if select_department != "":
#         break

# department = driver.find_element(By.XPATH, '//div[h4[contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"),"' + select_department.lower() + '")]]/following-sibling::div')
# courses = department.find_elements(By.TAG_NAME, "a")
# for course in courses:
#     print(course.text)

time.sleep(60)
driver.quit()