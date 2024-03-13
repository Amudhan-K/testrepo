
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
# Initialize Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()  # Maximize the window 

# Navigate to the website
driver.get('https://www.peozzle.com/')

# time.sleep(3)

#----------------------------------------------------------------
#check counter value and counter title

# try:
    
#     counter_title_elements = driver.find_elements(By.CLASS_NAME, "counter_title")
    
    
#     counter_value_elements = driver.find_elements(By.CLASS_NAME, "counter_value")

    
#     if len(counter_title_elements) >= 2 and len(counter_value_elements) >= 2:
        
#         first_counter_title = counter_title_elements[0].text
#         first_counter_value = counter_value_elements[0].text

        
#         second_counter_title = counter_title_elements[1].text
#         second_counter_value = counter_value_elements[1].text

        
#         print("First Counter Title:", first_counter_title)
#         print("First Counter Value:", first_counter_value)
#         print("Second Counter Title:", second_counter_title)
#         print("Second Counter Value:", second_counter_value)
#     else:
#         print("counter title or value elements not found on the webpage.")

# except NoSuchElementException:
#     print("Counter title or value elements not found on the webpage.")


#----------------------------------------------------------------


# # Wait for the flipboxes to be present
# flipboxes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'flipbox_wrapper')))

# # Check if at least one flipbox is present
# if flipboxes:
#     print("Flipboxes are present on the webpage.")
    
#     for idx, flipbox in enumerate(flipboxes, start=1):
#         flipbox_front = flipbox.find_element(By.CLASS_NAME, 'flipbox_front')
#         flipbox_back = flipbox.find_element(By.CLASS_NAME, 'flipbox_back')
        
#         flipbox_title = flipbox_front.find_element(By.CLASS_NAME, 'flipbox_title').text
#         flipbox_content = flipbox_back.find_element(By.CLASS_NAME, 'flipbox_content').text
        
#         
#         print(f"Flipbox {idx}:")
#         print("Title:", flipbox_title)
#         print("Content:", flipbox_content)
#         print()
        
# else:
#     print("Flipboxes are not present on the webpage.")

#----------------------------------------------------------------


# #first flipbox
# flipbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'flipbox_wrapper')))
# if flipbox:
#     print("Flipbox is present on the webpage.")
    
    
#     flipbox_front = flipbox.find_element(By.CLASS_NAME, 'flipbox_front')
#     flipbox_back = flipbox.find_element(By.CLASS_NAME, 'flipbox_back')
    
#     flipbox_title = flipbox_front.find_element(By.CLASS_NAME, 'flipbox_title').text
#     flipbox_content = flipbox_back.find_element(By.CLASS_NAME, 'flipbox_content').text
    
    
#     print("Title:", flipbox_title)
#     print("Content:", flipbox_content)
    
# else:
#     print("Flipbox is not present on the webpage.")


#--------------------------------
# try:
#     # Find the paragraph element
#     paragraph_element = driver.find_element_by_css_selector(".text_mobile p")

#     # Check if the copyright text is present
#     if "Copyright © 2024 Peozzle Corporation. Patented. All Rights Reserved." in paragraph_element.text:
#         print("Copyright text is present on the page.")
#     else:
#         print("Copyright text is not present on the page.")

# except NoSuchElementException:
#     print("Paragraph element not found on the page.")
#--------------
# try:
#     # Find all anchor elements
#     anchor_elements = driver.find_elements_by_css_selector(".seofy_module_text a")

#     # Iterate over each anchor element and print its href attribute
#     for anchor in anchor_elements:
#         print("Link:", anchor.get_attribute("href"))

#     print("All links are present on the page.")
# except NoSuchElementException:
#     print("Links not found on the page.")


#-----------
# try:
#     # Check if the image element is present
#     image_element = driver.find_element_by_css_selector("img.alignnone.size-medium.wp-image-4814")
#     print("Image found on the page.")
# except NoSuchElementException:
#     print("Image not found on the page.")

#----------------------------------------------------------------
#social media icons    
# try:
#     # Check if the social media icons are present
#     social_media_icons = driver.find_elements(By.XPATH, "//div[@class='seofy_module_social clearfix aleft with_bg']//a")
#     if social_media_icons:
#         print("Social media icons found:")
#         for icon in social_media_icons:
#             print(icon.get_attribute("title"), ":", icon.get_attribute("href"))
#     else:
#         print("No social media icons found on the page.")
# except NoSuchElementException:
#     print("Social media icons not found on the page.")


#---------------
# try:
#     paragraph_element = driver.find_element(By.XPATH, "//div[@class='wpb_wrapper']/p")
    
#     print(paragraph_element.text)
# except NoSuchElementException:
#     print("Paragraph element not found on the page.")
#-------
#image

# try:
#     # Find the image element
#     image = driver.find_element_by_class_name("vc_single_image-img")

#     # Check if the image element is present
#     if image:
#         print("Image is present.")
#     else:
#         print("Image is not present.")

# except Exception as e:
#     print("An error occurred:", e)


#------------

#infobox

# try:
#     # Find the infobox element
#     infobox = driver.find_element_by_class_name("infobox_wrapper")

#     # Find the icon element within the infobox
#     icon = infobox.find_element_by_class_name("infobox_icon")

#     # Find the title element within the infobox
#     title = infobox.find_element_by_class_name("infobox_title")

#     # Find the content element within the infobox
#     content = infobox.find_element_by_class_name("infobox_content")

#     # Check if all elements are present
#     if infobox and icon and title and content:
#         print("Icons and text are present in the infobox.")
#     else:
#         print("Icons and/or text are not present in the infobox.")

# except Exception as e:
#     print("An error occurred:", e)


#------------------

# try:
    
#     flipbox_wrapper = driver.find_element_by_class_name("flipbox_wrapper")

    
#     flipbox_front_text = flipbox_wrapper.find_element_by_class_name("flipbox_front").text

    
#     flipbox_back_text = flipbox_wrapper.find_element_by_class_name("flipbox_back_content").text

#     # Print the text content of the flipbox front and back
#     print("Front text:", flipbox_front_text)
#     print("Back text:", flipbox_back_text)

# except NoSuchElementException:
#     # If the flipbox wrapper element is not found, print a message 
#     print("Flipbox element is not present on the webpage.")

#------------


# # Text content to check hire quotes
# text_content = "Hiring is a Team Sport ! Synchronized Execution is the KEY for Hiring the Right Talent !"


# try:
#     element = driver.find_element_by_xpath(f'//*[contains(text(), "{text_content}")]')
#     print(f"Text content '{text_content}' is present on the webpage.")
# except NoSuchElementException:
#     print(f"Text content '{text_content}' is not present on the webpage.")

#-------

# #Peozzle para Text content to check
# text_contents = [
#     "PeozzleHire enables the Hiring team to orchestrate the talent acquisition journey from engagement to talent onboarding. This journey adopts a process-centric approach to automate the workflow steps effectively.",
#     "PeozzleAgency offers a fresh hiring approach to connect, collaborate, source, engage and hire the right talent for your customer.",
#     "PeozzleCampus powers universities to unify the student, alumni, placement officer, and talent seeker’s engagements and campus hiring workflows through enabling a private career services network.",
#     "PeozzleConnect enables professionals and consultants to connect and engage with Employers, Staffing Agencies,and Universities. AI-powered workflows, Mobile and Timesheet tools allow professionals to match jobs, manage/share profiles and manage the workplace time.",
#     "PeozzleServe enables Non-Profits to build a global volunteer network, unifying non-profit Administrators and volunteers’ engagement and Volunteer Management workflows."
# ]

# for text_content in text_contents:
#     try:
#         element = driver.find_element_by_xpath(f'//*[contains(text(), "{text_content}")]')
#         print(f"Text content '{text_content}' is present on the webpage.")
#     except NoSuchElementException:
#         print(f"Text content '{text_content}' is not present on the webpage.")


#----------

# # Check if the peozzle tree image is present
# try:
#     image_element = driver.find_element_by_xpath('//img[@src="https://www.peozzle.com/wp-content/uploads/2023/08/Draft-Main-3-1536x1024-1.jpg"]')
#     print("The peozzle tree image is present on the webpage.")
# except NoSuchElementException:
#     print("The peozzle tree image is not present on the webpage.")

#---------


# # Check if the "LAUNCH NOW" box is present
# try:
#     launch_now_box = driver.find_element_by_id('slider-12-slide-24-layer-26')
#     print("The 'LAUNCH NOW' box is present on the webpage.")
# except NoSuchElementException:
#     print("The 'LAUNCH NOW' box is not present on the webpage.")



#--------

# Check if the "Request Demo" box is present
# try:
#     request_demo_box = driver.find_element_by_id('slider-12-slide-24-layer-19')
#     print("The 'Request Demo' box is present on the webpage.")
# except NoSuchElementException:
#     print("The 'Request Demo' box is not present on the webpage.")

#---------   

# Find the Background image is present or not
# rs_slide_element = driver.find_element_by_css_selector('rs-slide')

# canvas_element = rs_slide_element.find_elements_by_tag_name('canvas')

# if canvas_element:
#     print("Background image is present.")
# else:
#     print("Background image is not present.")



#--------
# # Get the Peozzle text content
# rs_layer_id = "slider-12-slide-24-layer-2"

# try:
#     rs_layer_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, rs_layer_id)))
# except NoSuchElementException:
#     print("rs-layer element with ID '{}' not found on the webpage.".format(rs_layer_id))
#     driver.quit()
#     exit()
 
# rs_layer_text = rs_layer_element.text.strip()

# # expected text content
# expected_text = "Integrated Networking Platform for Hiring, Staffing, Campus Hiring, Job Searching, and Volunteering"

# # Validate if the text content matches the expected text
# if rs_layer_text == expected_text:
#     print("Text content matches with the text in peozzle webpage")
# else:
#     print("Text content does not match with the peozzle webpage")

#----------------

# # header tab container
# header_tab_container_locator = (By.CLASS_NAME, 'wgl-container')

# # Wait for the header tab container to be present on the page
# try:
#     header_tab_container_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(header_tab_container_locator))
# except TimeoutException:
#     print("Header tab container is not present on the webpage.")
#     driver.quit()
#     exit()

# # Check if the header tab container is present
# if header_tab_container_element:
#     print("Header tab container is present on the webpage.")
#     # Find the element using the XPath
#     span_element = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[1]/div/div/div[1]/div/div[3]/div/span")

#     # Get the text content of the element
#     text_content = span_element.text
#     print("Text content:", text_content)

#     # Define the expected phone number
#     expected_phone_number = "(763) 442-8468"

#     # Validate if the text content matches the expected phone number
#     if text_content == expected_phone_number:
#         print("Phone number is verified:", expected_phone_number)
#     else:
#         print("Phone number does not match :", text_content)

# else:
#     print("Header tab container is not present on the webpage.")


# # Define the XPath
# element_xpath = '/html/body/header/div[1]/div/div[1]/div'


# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))


# # Check if the Peozzle logo is present
# logo_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="default_logo"]')))

# if logo_element:
#     print("Logo is present on the webpage.")
# else:
#     print("Logo is not present on the webpage.")

# # Wait for the element to be visible
# product_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Products")))

# # Perform mouseover action to Products
# ActionChains(driver).move_to_element(product_element).perform()
# time.sleep(5)

# #Next from Product Dropdown navigate to Peozzle hire portal 
# a = ActionChains(driver)

# hire = driver.find_element_by_link_text("Peozzle Hire")
# a.move_to_element(hire).click().perform()
# time.sleep(5)





