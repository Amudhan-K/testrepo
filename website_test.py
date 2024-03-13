import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # Import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Set the service object
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get('https://www.peozzle.com/')
time.sleep(10)


# Open the output file in write mode
with open("output.txt", "w") as file:
    try:
        # Find the paragraph element
        paragraph_element = driver.find_element(By.CSS_SELECTOR, ".text_mobile p")

        # Check if the copyright text is present
        if "Copyright © 2024 Peozzle Corporation. Patented. All Rights Reserved." in paragraph_element.text:
            output_text = "Copyright text is present on the page."
        else:
            output_text = "Copyright text is not present on the page."
        
        # Write output to the file
        file.write(output_text + "\n")
        print("Output written to output.txt")

        # Find all anchor elements
        anchor_elements = driver.find_elements(By.CSS_SELECTOR, ".seofy_module_text a")

        
        for anchor in anchor_elements:
            href = anchor.get_attribute("href")
            
            file.write(f"Link: {href}\n")

        
        file.write("All links are present on the page and stored in 'output.txt'.\n")

    except NoSuchElementException:
        # If any element is not found, write an error message to the file
        file.write("Element not found on the page.\n")

    # Check if the image element is present
    try:
        # Find the image element
        image_element = driver.find_element(By.CSS_SELECTOR, "img.alignnone.size-medium.wp-image-4814")
        file.write("Image found on the page.\n")
        print("Image found on the page.")
    except NoSuchElementException:
        file.write("Image not found on the page.\n")
        print("Image not found on the page.")

    # Find social media icons
    try:
        
        social_media_icons = driver.find_elements(By.XPATH, "//div[@class='seofy_module_social clearfix aleft with_bg']//a")
        if social_media_icons:
            file.write("Social media icons found:\n")
            print("Social media icons found:")
            for icon in social_media_icons:
                icon_title = icon.get_attribute("title")
                icon_href = icon.get_attribute("href")
                file.write(f"{icon_title}: {icon_href}\n")
                print(icon_title, ":", icon_href)
        else:
            file.write("No social media icons found on the page.\n")
            print("No social media icons found on the page.")
    except NoSuchElementException:
        file.write("Social media icons not found on the page.\n")
        print("Social media icons not found on the page.")

    
    try:
    # Find the image element
        image = driver.find_element(By.CLASS_NAME, "vc_single_image-img")

        # Write the output to the file
        file.write("Image is present.\n")

    except NoSuchElementException:
        # If the image element is not found, write the output to the file
        file.write("Image is not present on the page.\n")

    
    try:
        # Find counter title elements
        counter_title_elements = driver.find_elements(By.CLASS_NAME, "counter_title")

        # Find counter value elements
        counter_value_elements = driver.find_elements(By.CLASS_NAME, "counter_value")

        # Check if both counter titles and counter values are present
        if len(counter_title_elements) >= 2 and len(counter_value_elements) >= 2:
            # Get the text of the first counter title and value
            first_counter_title = counter_title_elements[0].text
            first_counter_value = counter_value_elements[0].text

            # Get the text of the second counter title and value
            second_counter_title = counter_title_elements[1].text
            second_counter_value = counter_value_elements[1].text

            # Print the results
            print("First Counter Title:", first_counter_title)
            print("First Counter Value:", first_counter_value)
            print("Second Counter Title:", second_counter_title)
            print("Second Counter Value:", second_counter_value)

            # Write the results to the file
            file.write("First Counter Title: " + first_counter_title + "\n")
            file.write("First Counter Value: " + first_counter_value + "\n")
            file.write("Second Counter Title: " + second_counter_title + "\n")
            file.write("Second Counter Value: " + second_counter_value + "\n")
        else:
            print("Counter title or value elements not found on the webpage.")
            file.write("Counter title or value elements not found on the webpage.\n")

    except NoSuchElementException:
        print("Counter title or value elements not found on the webpage.")
        file.write("Counter title or value elements not found on the webpage.\n")


    try:
        # Wait for the flipboxes to be present
        flipboxes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'flipbox_wrapper')))
        
        # Check if at least one flipbox is present
        if flipboxes:
            file.write("Flipboxes are present on the webpage.\n")
            
            for idx, flipbox in enumerate(flipboxes, start=1):
                flipbox_front = flipbox.find_element(By.CLASS_NAME, 'flipbox_front')
                flipbox_back = flipbox.find_element(By.CLASS_NAME, 'flipbox_back')

                flipbox_title = flipbox_front.find_element(By.CLASS_NAME, 'flipbox_title').text
                flipbox_content = flipbox_back.find_element(By.CLASS_NAME, 'flipbox_content').text

                file.write(f"Flipbox {idx}:\n")
                file.write("Title: " + flipbox_title + "\n")
                file.write("Content: " + flipbox_content + "\n\n")
            
        else:
            file.write("Flipboxes are not present on the webpage.\n")
    
    except TimeoutException:
        file.write("Timed out waiting for flipboxes to be present.\n")
    
    except NoSuchElementException:
        file.write("One or both flipboxes are not present on the webpage.\n")


    try:
        # Find the infobox element
        infobox = driver.find_element(By.CLASS_NAME, "infobox_wrapper")

        # Find the icon element within the infobox
        icon = infobox.find_element(By.CLASS_NAME, "infobox_icon")

        # Find the title element within the infobox
        title = infobox.find_element(By.CLASS_NAME, "infobox_title")

        # Find the content element within the infobox
        content = infobox.find_element(By.CLASS_NAME, "infobox_content")

        # Check if all elements are present within the infobox
        if icon and title and content:
            file.write("Icons and text are present in the infobox.\n")
        else:
            file.write("Icons and/or text are not present in the infobox.\n")

    except NoSuchElementException:
        file.write("One or more elements within the infobox are not found.\n")

    except Exception as e:
        file.write(f"An error occurred: {e}\n")

    
    text_content = "Hiring is a Team Sport ! Synchronized Execution is the KEY for Hiring the Right Talent !"

    # Text content to check hire quotes
    try:
        # Try to find the element containing the specified text content
        element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
        file.write(f"Text content '{text_content}' is present on the webpage.\n")
    except NoSuchElementException:
        file.write(f"Text content '{text_content}' is not present on the webpage.\n")

    # Text content to check "HOW PEOZZLE CAN HELP"
    # Text content to check
    text_contents = [
        "HOW PEOZZLE CAN HELP YOUR HIRING TRANSFORMATION ",
        "JOURNEY",
        "We are bringing a fresh , network based, and data driven Talent acquisition approach to the Hiring Teams and Candidates"
    ]

    # Iterate over each text content to check
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")

    # # Text content to check "Peozzle Platform"
    # Text content to check
    text_contents = [
        "Peozzle Platform",
        "Uses Cloud-native technologies to ",
        "offer modular, scalable business,",
        "hiring, and career services workflow",
        "automation."
    ]

    # Iterate over each text content to check
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")

    # Text content to check "Patented Technology"
            
    # # Text content to check
    # text_contents = [
    #     "Peozzle Platform",
    #     "Uses Cloud-native technologies to ",
    #     "offer modular, scalable business,",
    #     "hiring, and career services workflow",
    #     "automation."
    # ]

    # # Iterate over each text content to check
    # for text_content in text_contents:
    #     try:
    #         # Try to find the element containing the specified text content
    #         element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
    #         file.write(f"Text content '{text_content}' is present on the webpage.\n")
    #     except NoSuchElementException:
    #         file.write(f"Text content '{text_content}' is not present on the webpage.\n")

    # Text content to check "Peozzle Marketplace"
            
    # Text content to check
    text_contents = [
        "Peozzle Marketplace",
        "Help to build scalable enterprise solutions to broader the talent management solutions. ",
    ]

    # Iterate over each text content to check
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")

            
    # Text content to check "Peozzle Analytics"
    
    # Iterate over each text content to check
    
        
    text_contents = [
        "Peozzle Analytics",
        "Cloud-native analytics technologies make the reporting & analytics of Agency, Campus, Hire, Connect, and Serve products easier. ",
        
        
    ]
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")
    

    # Text content to check "Peozzle AI/ML Model"
            
    # Iterate over each text content to check
    text_contents = [
        "Peozzle AI/ML Model",
        "Purpose-driven screening and AI/ML model provide insights into the data-driven hiring process. ",
        
        
    ]
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
            print(f"Text content '{text_content}' is present on the webpage.")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")
            print(f"Text content '{text_content}' is not present on the webpage.")


    # Text content to check "Why Peozzle Platform?"
    # Iterate over each text content to check
    text_contents = [
        "Why Peozzle Platform?",
        "We are grounded in People First Approach. Peozzle Platform intends to empower the Job seekers, Hiring team, Partners, and everybody in between to realize their fullest potential."
        
        
    ]
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
            print(f"Text content '{text_content}' is present on the webpage.")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")
            print(f"Text content '{text_content}' is not present on the webpage.")

    
    # Iterate over each text content to check
    text_contents = [
        "PeozzleHire enables the Hiring team to orchestrate the talent acquisition journey from engagement to talent onboarding. This journey adopts a process-centric approach to automate the workflow steps effectively.",
        "PeozzleAgency offers a fresh hiring approach to connect, collaborate, source, engage and hire the right talent for your customer.",
        "PeozzleCampus powers universities to unify the student, alumni, placement officer, and talent seeker’s engagements and campus hiring workflows through enabling a private career services network.",
        "PeozzleConnect enables professionals and consultants to connect and engage with Employers, Staffing Agencies,and Universities. AI-powered workflows, Mobile and Timesheet tools allow professionals to match jobs, manage/share profiles and manage the workplace time.",
        "PeozzleServe enables Non-Profits to build a global volunteer network, unifying non-profit Administrators and volunteers’ engagement and Volunteer Management workflows."
    ]
    for text_content in text_contents:
        try:
            # Try to find the element containing the specified text content
            element = driver.find_element(By.XPATH, f'//*[contains(text(), "{text_content}")]')
            file.write(f"Text content '{text_content}' is present on the webpage.\n")
            print(f"Text content '{text_content}' is present on the webpage.")
        except NoSuchElementException:
            file.write(f"Text content '{text_content}' is not present on the webpage.\n")
            print(f"Text content '{text_content}' is not present on the webpage.")

    # Check if the peozzle tree image is present
            
    try:
        # Try to find the image element
        image_element = driver.find_element(By.XPATH, '//img[@src="https://www.peozzle.com/wp-content/uploads/2023/08/Draft-Main-3-1536x1024-1.jpg"]')
        file.write("The peozzle tree image is present on the webpage.\n")
        print("The peozzle tree image is present on the webpage.")
    except NoSuchElementException:
        file.write("The peozzle tree image is not present on the webpage.\n")
        print("The peozzle tree image is not present on the webpage.")

    # Try to find the 'LAUNCH NOW' box element
    try:
        
        launch_now_box = driver.find_element(By.ID, 'slider-12-slide-24-layer-26')
        file.write("The 'LAUNCH NOW' box is present on the webpage.\n")
        print("The 'LAUNCH NOW' box is present on the webpage.")
    except NoSuchElementException:
        file.write("The 'LAUNCH NOW' box is not present on the webpage.\n")
        print("The 'LAUNCH NOW' box is not present on the webpage.")

    # Check if the "Request Demo" box is present
    try:
        # Try to find the 'Request Demo' box element
        request_demo_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'slider-12-slide-24-layer-19')))
        file.write("The 'Request Demo' box is present on the webpage.\n")
        print("The 'Request Demo' box is present on the webpage.")
    except TimeoutException:
        file.write("The 'Request Demo' box is not present on the webpage.\n")
        print("The 'Request Demo' box is not present on the webpage.")

    rs_layer_id = "slider-12-slide-24-layer-2"
    try:
        # Try to find the element with the specified ID
        rs_layer_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, rs_layer_id)))
        file.write("rs-layer element with ID '{}' found on the webpage.\n".format(rs_layer_id))
    except NoSuchElementException:
        file.write("rs-layer element with ID '{}' not found on the webpage.\n".format(rs_layer_id))
    

    rs_layer_id = "slider-12-slide-24-layer-2"
    try:
        # Try to find the element with the specified ID
        rs_layer_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, rs_layer_id)))
        file.write("rs-layer element with ID '{}' found on the webpage.\n".format(rs_layer_id))
        
        # Get the text content of the element and strip any leading or trailing whitespace
        rs_layer_text = rs_layer_element.text.strip()

        # Expected text content
        expected_text = "Integrated Networking Platform for Hiring, Staffing, Campus Hiring, Job Searching, and Volunteering"

        # Validate if the text content matches the expected text
        if rs_layer_text == expected_text:
            file.write("Text content matches with the text in peozzle webpage\n")
        else:
            file.write("Text content does not match with the peozzle webpage\n")
            
    except NoSuchElementException:
        file.write("rs-layer element with ID '{}' not found on the webpage.\n".format(rs_layer_id))
 
    header_tab_container_locator = (By.CLASS_NAME, 'wgl-container')
    try:
        # Wait for the header tab container to be present on the page
        header_tab_container_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(header_tab_container_locator))
        file.write("Header tab container is present on the webpage.\n")
    except TimeoutException:
        file.write("Header tab container is not present on the webpage.\n")


        # Check if the header tab container is present
    if header_tab_container_element:
        try:
            # Find the element using the XPath
            span_element = driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[1]/div/div/div[1]/div/div[3]/div/span")

            # Get the text content of the element
            text_content = span_element.text
            print("Text content:", text_content)

            # Define the expected phone number
            expected_phone_number = "(763) 442-8468"

            # Validate if the text content matches the expected phone number
            if text_content == expected_phone_number:
                print("Phone number is verified:", expected_phone_number)
            else:
                print("Phone number does not match :", text_content)

        except NoSuchElementException:
            error_message = "Element not found for header tab container."
            print(error_message)

            
            with open("output.txt", "a") as file:
                file.write(error_message + "\n")

    else:
        print("Header tab container is not present on the webpage.")


    try:
        # Define the XPath
        element_xpath = '/html/body/header/div[1]/div/div[1]/div'

        
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))

        
        
        # Check if the Peozzle logo is present
        logo_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="default_logo"]')))

        if logo_element:
            print("Logo is present on the webpage.")
            
            file.write("Logo is present on the webpage.\n")
        else:
            print("Logo is not present on the webpage.")
            
            file.write("Logo is not present on the webpage.\n")

    except NoSuchElementException:
        error_message = "Element not found."
        print(error_message)

        
        file.write(error_message + "\n")

    try:
        # Define the XPath
        element_xpath = '/html/body/header/div[1]/div/div[1]/div'

        # Wait for the element to be present
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))

        

        # Check if the Peozzle logo is present
        logo_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="default_logo"]')))

        if logo_element:
            print("Logo is present on the webpage.")
            
            file.write("Logo is present on the webpage.\n")
        else:
            print("Logo is not present on the webpage.")
            
            file.write("Logo is not present on the webpage.\n")

    except NoSuchElementException:
        error_message = "Element not found."
        print(error_message)
        file.write(error_message + "\n")

file.close()


import pandas as pd

with open("output.txt", "r") as file:
    lines = file.readlines()

data = []

for line in lines:
    line = line.strip()  
    if line:  
        data.append([line])  

df = pd.DataFrame(data, columns=["Data"])
excel_filename = "output1.xlsx"
df.to_excel(excel_filename, index=False)

print("Data has been successfully written to", excel_filename)
