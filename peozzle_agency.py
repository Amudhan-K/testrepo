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
driver=driver.get('https://www.peozzle.com/agency')
time.sleep(10)



expected_texts = {
    'Catalyst for Building your Business Network':'wpb_wrapper',
    'Digitalizes your staffing agency workflows to accelerate the hiring cycle and drive business growth.':'wpb_wrapper',
    'LAUNCH NOW':'wpb_wrapper',
    'Request Demo':'wpb_wrapper',
    'Agency Business Network':'wpb_wrapper',
    'Build and Manage your private business network connecting your staffing partners, candidates, and job boards to source your talent at speed and scale.':'wpb_wrapper',
    'Intelligent Tools':'wpb_wrapper',
    "AI/ML fueled tools empower placement officers and employers to identify the best-qualified university talent that meets the individual organization's needs.":'wpb_wrapper',
    'Agency Mobile App':'wpb_wrapper',
    'Peozzle Mobile App allows the Agency staffing team, candidates, and staffing partners to connect, collaborate, view, track, and process hiring actions.':'wpb_wrapper',
    'Video Resumes':'wpb_wrapper',
    'Patented* Peozzle Multi-Media resume tool, supports reception, storing, screening, and processing of Video Resumes, an emerging trend.':'wpb_wrapper',
    '360 Assessment':'wpb_wrapper',
    'The holistic Assessment view depicts the graphical view of the candidate profile, skills, experience fit, and Peozzle Match Score*.':'wpb_wrapper',
    'Time Management':'wpb_wrapper',
    'Integrated Timesheet tool allows candidates, recruiters, and hiring managers to capture, track and report time workflow.':'wpb_wrapper',
    'A Digital Staffing Agency Solution':'wpb_wrapper',
    'The staffing team needs to consider a fresh intelligence-driven hiring approach to address the evolving ecosystem changes and meet emerging trends. ':'wpb_wrapper',
    'Candidate-driven marketplace, increasing and sometimes unrealistic customer expectation on finding the right candidate, difficulty in balancing the speed of hire with the right quality, and lack of integrated tools add increased pressure to the staffing teams and affect their respective firm’s revenue bottom line.':'wpb_wrapper',
    "Staffing teams have responded with more spending on Job Ads, increasing job board subscriptions, and endless email marketing efforts only offer interim solutions but do not enable them to scale, adapt, and address current and emerging challenges. PeozzleAgency offers a fresh hiring approach to connect, collaborate, source, engage and hire the right talent for your customer.":'wpb_wrapper',
    'Hiring is a Team Sport ! Synchronized Execution is the KEY for Hiring the Right Talent !':'wpb_wrapper',
    'Connect':'wpb_wrapper',
    'Our team of creatives, designers & developers work alongside our SEO & content teams.':'wpb_wrapper',
    'Collaborate':'wpb_wrapper',
    'Communicate':'wpb_wrapper',
    'Network':'wpb_wrapper',
    'Explore PeozzleAgency Solution':'wpb_wrapper',
    'Role-based portal and Context-driven Workflow provide seamless Experience to Hiring Team and Candidates.':'wpb_wrapper',
    'SOURCE':'wpb_wrapper',
    'SCREEN':'wpb_wrapper',
    'ASSESS':'wpb_wrapper',
    'ENGAGE':'wpb_wrapper',
    'SUBMIT':'wpb_wrapper',
    'Source':'wpb_wrapper',
    'Manage Job Requisition':'wpb_wrapper',
    'Manage Candidates Profiles':'wpb_wrapper',
    'Execute Internal Sourcing':'wpb_wrapper',
    'Manage and Engage Partners':'wpb_wrapper',
    'Push and Publish Job Requisitions':'wpb_wrapper',
    'Receive Candidate Resume':'wpb_wrapper',
    'HOW PEOZZLE CAN HELP YOUR HIRING TRANSFORMATION JOURNEY':'wpb_wrapper',
    'We are bringing a fresh , network based, and data driven Hiring Automation approach to the Hiring Teams and Candidates':'wpb_wrapper',
    'Peozzle Platform':'wpb_wrapper',
    'Uses cloud-native technologies to offer modular, scalable business, staffing, hiring, and career services workflows.':'wpb_wrapper',
    'Patented Peozzle Technology':'wpb_wrapper',
    'The approved USPTO patents are powering the Peozzle platform. 1)Resource Distribution System and 2)Multimedia Resume Distribution System.':'wpb_wrapper',
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
            # elements = driver.find_elements(By.CLASS_NAME, class_name)
            elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'wpb_wrapper')))
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