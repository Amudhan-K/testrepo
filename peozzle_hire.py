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
driver=driver.get('https://www.peozzle.com/hire')
time.sleep(10)




expected_texts = {
    'Networked Approach for Building a Healthy Talent Pipeline': 'wpb_wrapper',
    'Empowers your recruiting teams to engage, source, screen, assess, and hire the right talent for your organization.': 'wpb_wrapper',
    'LAUNCH NOW':'wpb_wrapper',
    'Request Demo':'wpb_wrapper',
    'Talent Network': 'wpb_wrapper',
    'Build and Manage your private Talent Network connecting your staffing vendors, candidates, and job boards to source your talent at speed and scale.': 'wpb_wrapper',
    'Video Resumes': 'wpb_wrapper',
    'The patented Peozzle multi-media resume tool supports reception, storing, screening, and processing video resumes, an emerging trend.':'wpb_wrapper',
    'Intelligent Tools':'wpb_wrapper',
    'AI/ML fueled tools empower recruiters and hiring managers to identify the best fit and diverse talent aligned with organization needs.':'wpb_wrapper',
    '360 Assessment':'wpb_wrapper',
    'The holistic Assessment view describes the graphical view of the candidate profile, skills, experience, along with the Peozzle Match Score.':'wpb_wrapper',
    'Mobile Platform':'wpb_wrapper',
    'Peozzle Mobile App allows the hiring team, candidates, and staffing partners to connect, collaborate, view, track, and disposition hiring actions.':'wpb_wrapper',
    'Campus Recruiting':'wpb_wrapper',
    'Combining with PeozzleCampus module, PeozzleHire supports university partners, student engagement, and Campus Hiring workflows.':'wpb_wrapper',
    'PeozzleHire - An Intelligent Hiring Solution':'wpb_wrapper',
    'We believe hiring the right talent is a Team Sport. Peozzle’s solutions adopt a Network-centric approach to empower the Hiring Manager, Recruiter, and Partners to seamlessly connect, collaborate, and form a purpose-built talent network. That helps with their individual needs where  Employers acquire suitable Job seekers with optimal talent, and Job Seekers get the right jobs aligned with their career goals and aspirations.':'wpb_wrapper',
    'Peozzle’s solution enables the Hiring team to orchestrate the talent acquisition journey from engagement to talent onboarding. This journey adopts a process-centric approach to automate the workflow steps effectively. The workflow includes Requisition submission, Sourcing talent, Screening, Assessment, Pipeline management, Partner management, Offer management, and Timesheet management.':'wpb_wrapper',
    'Hiring is a Team Sport ! Synchronized Execution is the KEY for Hiring the Right Talent !':'wpb_wrapper',
    'Explore PeozzleHire Solution':'wpb_wrapper',
    'Role-based portal and Context-driven Workflow provide seamless Experience to Hiring Team and Job seekers.':'wpb_wrapper',
    'SOURCE':'wpb_wrapper',
    'Source':'wpb_wrapper',
    'Manage Job Requisition':'wpb_wrapper',
    'Manage Candidates Profiles':'wpb_wrapper',
    'Execute Internal Sourcing':'wpb_wrapper',
    'Manage and Engage Partners':'wpb_wrapper',
    'Push and Publish Job Requisitions':'wpb_wrapper',
    'Receive Candidate Resume':'wpb_wrapper',
    'SCREEN':'wpb_wrapper',
    'Screen':'wpb_wrapper',
    # 'Screen Text and Video Resume':'seofy_check',
    # 'Shortlist Candidates':'seofy_check',
    'ASSESS':'wpb_wrapper',

    'HIRE':'wpb_wrapper',
    'AUTOMATION':'wpb_wrapper',
    'HOW PEOZZLE CAN HELP YOUR HIRING TRANSFORMATION JOURNEY':'wpb_wrapper',
    'We are bringing a fresh, network-based, and data-driven Hiring Automation approach to the Hiring Teams and Job seekers.':'wpb_wrapper',
    'Peozzle Platform':'wpb_wrapper',
    'Uses Cloud-native technologies to offer modular, scalable business, staffing, hiring, and career services workflows.':'wpb_wrapper',
    'Patented Peozzle Technology':'wpb_wrapper',
    'The approved USPTO patents are powering the Peozzle platform. 1)Resource Distribution system and 2)Multimedia Resume distribution system.':'wpb_wrapper',
    'Peozzle Marketplace':'wpb_wrapper',
    'Peozzle marketplace includes technology and solution that help to build scalable enterprise solutions to broaden the talent management solutions.':'wpb_wrapper',
    'Peozzle Analytics':'wpb_wrapper',
    'Cloud-native analytics technologies make the reporting & analytics of Agency, Campus, Hire, Connect, and Serve products easier.':'wpb_wrapper',
    'Peozzle AI/ML Model':'wpb_wrapper',
    'Purpose-driven screening and AI/ML model provide insights into the data-driven hiring process.':'wpb_wrapper',
    'Why Peozzle Platform?':'wpb_wrapper',
    'We are grounded in People First Approach. Peozzle Platform intends to empower the Job seekers, Hiring team, Partners, and everybody in between to realize their fullest potential.':'wpb_wrapper',
    '1098+':'wpb_wrapper',
    'GROWING NETWORK':'wpb_wrapper',
    '2300+':'wpb_wrapper',
    'ACTIVE USERS':'wpb_wrapper',
    'Connect with':'wpb_wrapper',
    'Products':'wpb_wrapper',
    'Peozzle Hire':'wpb_wrapper',
    'Peozzle Agency':'wpb_wrapper',
    'Peozzle Campus':'wpb_wrapper',
    'Peozzle Connect':'wpb_wrapper',
    'Peozzle Serve':'wpb_wrapper',
    'Solutions':'wpb_wrapper',
    'Staffing Automation':'wpb_wrapper',
    'Recruitment':'wpb_wrapper',
    'Campus Recruitment':'wpb_wrapper',
    'Volunteer Management':'wpb_wrapper',
    'Alumni Management':'wpb_wrapper',
    'Peozzle Mobile':'wpb_wrapper',
    'Resources':'wpb_wrapper',
    'Datasheet':'wpb_wrapper',
    'Mission':'wpb_wrapper',
    'Contact us':'wpb_wrapper',
    'Copyright © 2024 Peozzle Corporation. Patented.':'wpb_wrapper',
   
}

with open('output.txt', 'w') as f:

    for expected_text, class_name in expected_texts.items():
        try:
            elements = driver.find_elements(By.CLASS_NAME, class_name)
            if elements:
                found = False
                for element in elements:
                    text_content = element.text.strip()
                    if expected_text in text_content:
                        output = f"Expected text '{expected_text}' found in element with class name '{class_name}'\n"
                        f.write(output)
                        found = True
                        break
                if not found:
                    output = f"Expected text '{expected_text}' not found in any element with class name '{class_name}'\n"
                    f.write(output)
            else:
                output = f"No elements found with class name '{class_name}'\n"
                f.write(output)
        except Exception as e:
            output = f"An error occurred: {e}\n"
            f.write(output)

# with open('output.txt', 'w') as f:

#     for expected_text, class_name in expected_texts.items():
#         try:
#             elements = driver.find_elements(By.CLASS_NAME, class_name)
#             if elements:
#                 found = False
#                 for element in elements:
#                     text_content = element.text.strip()
#                     if expected_text in text_content:
#                         output = f"Expected text '{expected_text}' found in element with class name '{class_name}'\n"
#                         f.write(output)
#                         found = True
#                         break
#                 if not found:
#                     output = f"Expected text '{expected_text}' not found in any element with class name '{class_name}'\n"
#                     f.write(output)
#             else:
#                 output = f"No elements found with class name '{class_name}'\n"
#                 f.write(output)
#         except Exception as e:
#             output = f"An error occurred: {e}\n"
#             f.write(output)

# #----------------------------------------------------------------
# # Iterate over each expected text and its corresponding class name
# for expected_text, class_name in expected_texts.items():
#     # Find elements with the specified class name
#     elements = driver.find_elements(By.CLASS_NAME, class_name)
    
#     # Check if any elements with the class name are found
#     if elements:
#         found = False
#         # Iterate over each element and check its text content
#         for element in elements:
#             text_content = element.text.strip()
#             # Check if the expected text is present in the element's text content
#             if expected_text in text_content:
#                 print(f"Expected text '{expected_text}' found in element with class name '{class_name}'")
#                 found = True
#                 break
        
#         if not found:
#             print(f"Expected text '{expected_text}' not found in any element with class name '{class_name}'")
#     else:
#         print(f"No elements found with class name '{class_name}'")