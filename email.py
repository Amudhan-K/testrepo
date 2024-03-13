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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Initialize Chrome WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Set the service object
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)
results = {}

# Function to send email with the report
def send_email(filename):
    sender_email = "gracewilliam2010@gmail.com"
    receiver_email = "gracewilliam2010@gmail.com"
    password = "nibr razx ckbn epse"  # Use your actual 16-digit password here

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Peozzle Hire Report"

    body = """\
    Hi,

    Please find attached the Peozzle Hire report.

    Best regards,
    Your Name"""
    message.attach(MIMEText(body, "plain"))

    # Open the file to be sent
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    # Create SMTP session for sending the mail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Enable security
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully")

try:
    # Navigate to the website
    driver.get('https://www.peozzle.com/')
    results["TC1-Home page"] = "Present"
    # Wait for the element to be visible
    product_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Products")))

    # Perform mouseover action to Products
    ActionChains(driver).move_to_element(product_element).perform()

    # Next, from Product Dropdown navigate to Peozzle hire portal
    try:
        hire = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Peozzle Hire")))
        hire.click()
        results["TC2-Navigation hire page"] = "Present"
    except (NoSuchElementException, TimeoutException):
        results["TC2-Element 'Peozzle Hire"] = "Not present"

    # Check Slider image
    slider_ids = ["slider-19-slide-45-layer-28", "slider-19-slide-46-layer-28", "slider-19-slide-47-layer-28"]

    for i, slider_id in enumerate(slider_ids, start=1):
        time.sleep(30)  # Adjust sleep time as needed
        elements = driver.find_elements(By.ID, slider_id)
        if len(elements) > 0:
            results[f"TC5-Slider Image {i} is found"] = "Present"
        else:
            results[f"TC5-Slider Image {i} is found"] = "Not Present"
        time.sleep(10)  # Add delay before next iteration

    # Remaining testing steps...

    # Create DataFrame and save to Excel
    df = pd.DataFrame(results.items(), columns=["Element", "Status"])
    output_file = "Peozzle_Hire_Report.xlsx"
    df.to_excel(output_file, index=False)
    print("Report generated successfully")

    # Send email with the report
    send_email(output_file)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the driver
    driver.quit()