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

#target_div = driver.find_element_by_css_selector("div.main.page-content.wrapper div.region.region-content section.block.block-slices.block-content-slices.block-slices-slice-slice-related-courses-2.clearfix div.related-items.view-mode-summary-only div:has(h4:contains('Computing & Informatics'))")
# parent_div = target_div.find_element_by_xpath("..")
# links = parent_div.find_elements_by_tag_name("a")

# for link in links:
#     print(link.get_attribute("href"))

time.sleep(60)

# driver.quit()
