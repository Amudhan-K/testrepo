import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Chrome WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Set the service object
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)



results = {}
# Navigate to the website
driver.get('https://www.peozzle.com/datasheets/')
results["TC1-Home page"] = "Present"
# # Wait for the element to be visible

product_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Resources")))

# Perform mouseover action to Products
ActionChains(driver).move_to_element(product_element).perform()

# Next, from Product Dropdown navigate to Peozzle hire portal
try:
    Datasheets1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Datasheets")))
    Datasheets1.click()
    #print("Navigationti hire")
    results["TC2-Navigation Datasheets page"] = "Present"
except (NoSuchElementException, TimeoutException):
    results["TC2-Element 'Peozzle Datasheets"] = "Not present"

 ###################VIEW PDF #################   
# Click on the link that leads to the PDF file//*[@id="seofy_button_65e7edb52533d"]/a
pdf_link=driver.find_element(By.CSS_SELECTOR, 'a[href="http://www.peozzle.com/wp-content/uploads/2023/08/Peozzle-Business-Brochure-1.pdf"]')
# pdf_link = driver.find_element(By.XPATH, 'https://www.peozzle.com/wp-content/uploads/2023/08/Peozzle-Business-Brochure-1.pdf')

pdf_link.click()

# Wait for the PDF to load (you may need to adjust the wait time based on your network speed and the size of the PDF)
time.sleep(5)

# Switch to the new window or tab that opened with the PDF
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])  # Assuming the PDF opened in a new tab, adjust index if necessary

# You can now interact with the PDF using browser controls. For example, to close the PDF viewer:
# Close the PDF viewer tab or window
driver.close()

# Switch back to the main window
driver.switch_to.window(window_handles[0])

# Now you are back on the main page. Continue with your automation tasks as needed.

# Quit the driver when done
df = pd.DataFrame(results.items(), columns=["Element", "Status"])
#df = pd.DataFrame.from_dict(results, orient='index', columns=['Results'])
# Save the DataFrame to an Excel file
output_file = "Peozzle_Connect_Report.xlsx"
df.to_excel(output_file, index=False)










# # Your sequence of commands
# commands = [
#     {"selector": "Peozzle Business Brochure > .connectButton > span", "action": "click"},
#     {"selector": "#seofy_button_65e7e933bd9ed > .wgl_button_link", "action": "click_and_hold"},
#     {"selector": "#seofy_button_65e7553e83626 > .wgl_button_link", "action": "move_to_element"},
#     # Add more commands as needed
# ]
# ####seofy_button_65e7e933bd9ed > a
# # Execute commands
# for command in commands:
#     selector = command["selector"]
#     action = command["action"]

#     try:
#         if action == "click":
#             element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
#             element.click()
#         elif action == "click_and_hold":
#             element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
#             actions = ActionChains(driver)
#             actions.click_and_hold(element).perform()
#         elif action == "move_to_element":
#             element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
#             actions = ActionChains(driver)
#             actions.move_to_element(element).perform()
#     except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
#         print(f"Action failed for selector: {selector}")

# After executing commands, handle windows and perform necessary actions
# For example:
# window_handles = driver.window_handles
# driver.switch_to.window(window_handles[-1])  # Switch to the last opened window

# Continue with more actions if needed

# Quit the driver
### Check for the presence of specific elements for TC37

df = pd.DataFrame(results.items(), columns=["Element", "Status"])
#df = pd.DataFrame.from_dict(results, orient='index', columns=['Results'])
# Save the DataFrame to an Excel file
output_file = "Peozzle_Connect_Report.xlsx"
df.to_excel(output_file, index=False)

# Quit the driver
driver.quit()