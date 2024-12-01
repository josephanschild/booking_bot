from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select  # This is the missing import
import csv
from selenium.webdriver.common.keys import Keys



username = "jhanc67"
password = "Hanchiew21"

#WHC
billing_number = 1
#PO and Account Detail
PO_number = "4500035244"
account_id = "82499" #general PO
group_rate = "2.BMA 2023-24 HOLD ROOM"
policy_type = "//*[@id='cboBillPolicyType']/option[3]"


"""
#Yarrabee
billing_number = 1
#PO and Account Detail
PO_number = "YARRABEE"
account_id = "10183" #general PO
group_rate = "Yarrabee FY 2024-2025"
policy_type = "//*[@id='cboBillPolicyType']/option[4]"
"""


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.rezexpert.com/")

def wait(int):
	return time.sleep(int)

wait(2)  # Consider using WebDriverWait here instead

username_field = driver.find_element(By.ID, "txtUserName")
username_field.send_keys(username)

password_field = driver.find_element(By.ID, "txtPassword")  # Adjust based on actual ID
password_field.send_keys(password)
wait(0.5)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'LOGIN')]")
login_button.click()
wait(10)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//*[@id='mnuAdmin']/a")
login_button.click()
wait(2)  # Consider using WebDriverWait here instead

# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//*[@id='tbAdmin_Periodic_Billing']/tr[1]/td[2]")
login_button.click()
wait(10)  # Consider using WebDriverWait here instead

billing_type = driver.find_element(By.XPATH, "//*[@id='cboBillPolicyType']")  # Adjust based on actual ID
billing_type.click()
wait(0.5)  # Consider using WebDriverWait here instead

billing_type = driver.find_element(By.XPATH, f"{policy_type}")  # Adjust based on actual ID
billing_type.click()
wait(10)  # Consider using WebDriverWait here instead


# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//*[@id='tbActiveBillingPolicies']/tr[1]")
login_button.click()
wait(5)  # Consider using WebDriverWait here instead



# Using XPath by button text
login_button = driver.find_element(By.XPATH, "//*[@id='btnCancel0']")
login_button.click()
wait(25)  # Consider using WebDriverWait here instead


# Open and read the CSV file
with open('billing_to_add.csv', newline='') as csvfile:
	csvreader = csv.DictReader(csvfile)

	for row in csvreader:
		# For each row in the CSV, extract data
		unit_number = row['unit label']
		rez_number = row['rez number']
		start_date = row['check in date']
		end_date = row['check out date']


		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='btnAdd782']")
		login_button.click()
		wait(3)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='divUnitLabel']")
		login_button.click()
		wait(2)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59501']/i")
		login_button.click()
		wait(0.5)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59502']/i")
		login_button.click()
		wait(0.5)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59503']/i")
		login_button.click()
		wait(0.5)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59504']/i")
		login_button.click()
		wait(0.5)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59505']/i")
		login_button.click()
		wait(0.5)  # Consider using WebDriverWait here instead

		# Using XPath by button text
		login_button = driver.find_element(By.XPATH, "//*[@id='59506']/i")
		login_button.click()
		wait(1)  # Consider using WebDriverWait here instead

		select_unit = driver.find_element(By.XPATH, f"//li[@label='{unit_number}']")
		select_unit.click()
		wait(1) 


		select_unit = driver.find_element(By.XPATH, "//*[@id='divUnitSelected']")
		select_unit.click()
		wait(3) 

		select_unit = driver.find_element(By.XPATH, "//*[@id='divRezNumber']")
		select_unit.click()
		wait(2) 


		radio_button = driver.find_element(By.XPATH, f"//input[@class='radRezList'][@rez_number='{rez_number}']")
		radio_button.click()
		wait(1) 


		select_unit = driver.find_element(By.XPATH, "//*[@id='divRezSelected']")
		select_unit.click()
		wait(1) 

		password_field = driver.find_element(By.ID, "txtStartDate")  # Adjust based on actual ID
		password_field.send_keys(start_date)						

		password_field = driver.find_element(By.ID, "txtEndDate")  # Adjust based on actual ID
		password_field.send_keys(end_date)


		password_field = driver.find_element(By.ID, "txtNextInvoiceDate")  # Adjust based on actual ID
		password_field.send_keys(start_date)


		select_unit = driver.find_element(By.XPATH, "//*[@id='divRight']/div[1]/div[3]/table/thead/tr/th[2]")
		select_unit.click()
		wait(1) 

		select_unit = driver.find_element(By.XPATH, "//*[@id='divAccount']")
		select_unit.click()
		wait(2) 

		radio_button = driver.find_element(By.XPATH, f"//input[@class='radAccountList'][@account_id='{account_id}']")
		radio_button.click()
		wait(2) 


		select_unit = driver.find_element(By.ID, "btnAccountSelect")
		select_unit.click()
		wait(1) 

		password_field = driver.find_element(By.ID, "txtPONumber")  # Adjust based on actual ID
		password_field.send_keys(PO_number)
		wait(2)  # Consider using WebDriverWait here instead


		select_unit = driver.find_element(By.ID, "divAdd")
		select_unit.click()
		wait(1) 


		dropdown = Select(driver.find_element(By.ID, "cboProductGroup"))
		dropdown.select_by_visible_text("Reservation Products")
		wait(0.5) 

		dropdown = Select(driver.find_element(By.ID, "cboProduct"))
		dropdown.select_by_visible_text("Terrace")
		wait(1) 


		dropdown = Select(driver.find_element(By.ID, "cboRateType"))
		dropdown.select_by_visible_text("Pull from Product Rates")
		wait(0.5) 


		dropdown = Select(driver.find_element(By.ID, "cboProductRateGroup"))
		dropdown.select_by_visible_text(group_rate)
		wait(1) 

		select_unit = driver.find_element(By.XPATH, "//*[@id='divProductSetup']/div[2]")
		select_unit.click()
		wait(1) 

		select_unit = driver.find_element(By.ID, "btnSubmit782")
		select_unit.click()
		wait(3) 

		select_unit = driver.find_element(By.ID, "spanBillingStatus")
		select_unit.click()
		wait(2) 

		select_unit = driver.find_element(By.ID, "btnYes")
		select_unit.click()
		wait(2) 

		billing_number += 1

		print(f"{billing_number}, {unit_number}, {rez_number}, {start_date}, {end_date}")

print("DONE")

	# Consider implementing a wait here to ensure the next page loads or your action completes

	# Proceed with further actions or close the browser
	# driver.quit()
	# Adjust time.sleep as needed, or implement more sophisticated wait strategies

	# Your script continues from here