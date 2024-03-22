from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select  # This is the missing import
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "jhanc67"
password = "Hanchiew12"


guest_name = "committ"
business_name = "BM Alliance Operation Pty Ltd"
alt_con = "assigned room"
check_in_date = "20-APR-2024"
check_out_date = "21-APR-2024"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.rezexpert.com/")

def wait(int):
	return time.sleep(int)

wait(2)  # Consider using WebDriverWait here instead

username_field = driver.find_element(By.ID, "txtUserName")
username_field.send_keys(username)

wait(2)  # Consider using WebDriverWait here instead

password_field = driver.find_element(By.ID, "txtPassword")  # Adjust based on actual ID
password_field.send_keys(password)
wait(2)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'LOGIN')]")
login_button.click()
wait(10)  # Consider using WebDriverWait here instead


# Using XPath by button text
login_button = driver.find_element(By.ID, "grid_clientsearch0")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//li[a[text()='Business']]")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.ID, "txtBus_personsearch_Name1")
login_button.click()
login_button.send_keys(business_name)

wait(10)  # Consider using WebDriverWait here instead

login_button = driver.find_element(By.ID, "btnSearch1")
login_button.click()
wait(2)

login_button = driver.find_element(By.XPATH, "//*[@id='divMainResults1']/div[2]/div[2]")
login_button.click()
wait(2)

login_button = driver.find_element(By.XPATH, "//*[@id='divMainResults1']")
login_button.click()
wait(2)

# Using XPath by button text
row_element = driver.find_element(By.XPATH, "//*[@id='tblResults1']/tbody/tr[2]")
row_element.click()

wait(10)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.ID, "btnSNSubmit0")
login_button.click()
wait(10)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.ID, "txtCheckInDate99")
login_button.clear()
login_button.send_keys(check_in_date)

wait(2)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.ID, "txtCheckOutDate99")
login_button.clear()
wait(0.5)
login_button.send_keys(check_out_date)

wait(5)  # Consider using WebDriverWait here instead


print("assigne room type")

wait(5)



login_button = driver.find_element(By.ID, "btnSubmit99")
login_button.click()
wait(5)



radio_button = driver.find_element(By.XPATH, "//*[@id='radRezSelect54']")
radio_button.click()
wai(2)


login_button = driver.find_element(By.ID, "divSearchClient")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead


login_button = driver.find_element(By.ID, "txtPer_personsearch_ClientName1")
login_button.click()
login_button.send_keys(guest_name)
wait(5)  # Consider using WebDriverWait here instead



login_button = driver.find_element(By.ID, "btnSearch1")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead


login_button = driver.find_element(By.ID, "txtGuestFolioAltConfirmationNumber")
login_button.click()
login_button.send_keys(alt_con)
wait(5)  # Consider using WebDriverWait here instead

# Locate the select element
select_element = driver.find_element(By.ID, "cboGuestFolioAlert")
select_object = Select(select_element)
select_object.select_by_value("4926")


login_button = driver.find_element(By.ID, "setuppage_submit3")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead


login_button = driver.find_element(By.XPATH, "//*[@id='the_body']/div[9]/div[1]/button")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead

login_button = driver.find_element(By.XPATH, "//*[@id='dashboard_body_head_funcs']/div[2]/div")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead

