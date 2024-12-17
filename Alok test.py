from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# User credentials
USERNAME = "admin"
PASSWORD = "admin@123"

# Scholar number
SCHOLAR_NO = "12345"

# Target URL (login portal)
LOGIN_URL = "http://13.232.204.65/schoolerp_test/"

# Initialize WebDriver
try:
    driver = webdriver.Chrome()  # Assumes ChromeDriver is in PATH
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to load

    # Step 1: Open the login page
    print("Opening login page...")
    driver.get(LOGIN_URL)

    # Step 2: Login Process
    print("Entering username...")
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.clear()
    username_field.send_keys(USERNAME)

    print("Entering password...")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(PASSWORD)

    print("Submitting the login form...")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']")))
    login_button.click()

    # Step 3: Verify Dashboard
    print("Verifying dashboard...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dashh2']")))
    print("Login successful! Dashboard loaded.")

    # Step 4: Navigate to Accounts Section
    print("Navigating to Accounts section...")
    accounts_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Accounts")))  # Adjust if necessary
    accounts_link.click()

    # Step 5: Navigate to Monthly Fee Page
    print("Navigating to Monthly Fee page...")
    monthly_fee_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Monthly Fee")))  # Adjust if necessary
    monthly_fee_link.click()

    # Step 6: Enter Scholar Number
    print("Entering Scholar Number...")
    scholar_input = wait.until(EC.presence_of_element_located((By.NAME, "scholar_no")))  # Update locator if needed
    scholar_input.clear()
    scholar_input.send_keys(SCHOLAR_NO)

    # Step 7: Wait for results to load after entering Scholar Number
    print("Waiting for results to load after entering Scholar Number...")
    # Wait for an element that confirms the page updated (could be a fee table or confirmation)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='fee-details']")))  # Update with the relevant element
    print("Scholar Number processed. Results displayed.")

    # Optional: Take a screenshot to verify the result
    driver.save_screenshot("monthly_fee_result.png")
    print("Screenshot saved as 'monthly_fee_result.png'")

    # Pause to observe the results
    time.sleep(5)  # Wait to observe the page after scholar number is entered

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Step 8: Close the browser
    print("Closing the browser...")
    driver.quit()
