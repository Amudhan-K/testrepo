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
driver.get('https://www.peozzle.com/campus')
time.sleep(10)

expected_texts = {
    'Career Services Network for Campus Hiring ':'wpb_wrapper',
    'Unifies Student, Alumni, Placement officer, and Employer workflows to improve career hiring experience and democratize access to opportunities.':'wpb_wrapper',
    'LAUNCH NOW':'wpb_wrapper',
    'Request Demo':'wpb_wrapper',
    'Career Network':'wpb_wrapper',
    'Build and Manage your private career services network connecting your students and employers to global jobs, Internships, and Volunteering Opportunities.':'wpb_wrapper',
    'Intelligent Tools':'wpb_wrapper',
    "AI/ML fueled tools empower placement officers and employers to identify the best-qualified university talent that meets the individual organization's needs.":'wpb_wrapper',
    'Campus Mobile App':'wpb_wrapper',
    'PeozzleCampus Mobile App allows placement officers, students, alumni, and employers partners to connect and realize their individual needs.':'wpb_wrapper',
    'Video Resumes':'wpb_wrapper',
    'Patented* Peozzle Multi-Media resume tool, supports reception, storing, screening, and processing of Video Resumes, an emerging trend.':'wpb_wrapper',
    '360 Assessment':'wpb_wrapper',
    'The holistic Assessment view depicts the graphical view of the candidate profile, skills, experience fit, and Peozzle Match Score.':'wpb_wrapper',
    'Time Management':'wpb_wrapper',
    'Integrated Timesheet tool allows students, placement officers, hiring managers, and nonprofit administrators to capture, track and report the timesheet workflow.':'wpb_wrapper',
    'PeozzleCampus – An Automated Campus Hiring !':'wpb_wrapper',
    'Placement Officers and Employers need to adopt a networked hiring approach to connect and build a healthy Early Talent Pipeline to optimize Campus Hiring.':'wpb_wrapper',
    'The resource-intensive campus hiring process, limited employer engagement with the student, lack of talent insights constraints both career service officer and talent manager to hire the right candidate and build a healthy early talent pipeline.':'wpb_wrapper',
    'Campus and Employer hiring teams’ responses with siloed brand improvement, student engagement, and executing in-person/virtual job fairs and endless email marketing efforts, but they cannot fully realize the expected outcomes. Further, both campus and hiring teams lack insights on the student population, outreach performance.':'wpb_wrapper',
    'PeozzleCampus powers universities to unify the student, alumni, placement officer, and talent seeker’s engagements and campus hiring workflows through enabling a private career services network. Student Portal and custom Mobile App would allow students to connect seamlessly to global job and internship opportunities.':'wpb_wrapper',
    'Hiring is a Team Sport ! Synchronized Execution is the KEY for Hiring The Right Talent !':'wpb_wrapper',
    'Network Approach':'wpb_wrapper',
    'Enables Employers, Staffing Agencies, Universities to build a purpose-built business network, which accelerates hiring the right talent.':'wpb_wrapper',
    'Mobile Application':'wpb_wrapper',
    'Peozzle Mobile App allows Peozzle stakeholders to connect, engage and collaborate on hiring, onboarding, and employment workflows.':'wpb_wrapper',
    'Intelligent Automation':'wpb_wrapper',
    'AI/ML fueled tools empower staffing agencies and job seekers to identify and Hire the best-fit candidates for the Organization.':'wpb_wrapper',
    'Peozzle Analytics':'wpb_wrapper',
    'Empower the recruitment teams across employers, Agencies, and universities with real-time performance, sourcing, and market data insights.':'wpb_wrapper',
    'Explore PeozzleCampus Solution':'wpb_wrapper',
    'Role-based portals and Context-driven Workflows provide seamless Experience to Placement Officers, the Hiring Team, and Students.':'wpb_wrapper',
    'ENROLL':'wpb_wrapper',
    'ENGAGE':'wpb_wrapper',
    'SCREEN':'wpb_wrapper',
    'ASSESS':'wpb_wrapper',
    'PLACE':'wpb_wrapper',
    'MANAGE':'wpb_wrapper',
    'Enroll':'wpb_wrapper',
    'Invite/Enlist Current Students':'wpb_wrapper',
    'Invite/Enlist Alumni Students':'wpb_wrapper',
    'Invite/Enlist Engage Employees':'wpb_wrapper',
    'HOW PEOZZLE CAN HELP YOUR HIRING TRANSFORMATION JOURNEY':'wpb_wrapper',
    'We are bringing a fresh, network-based, and data-driven Talent acquisition approach to the Hiring Teams and Candidates.':'wpb_wrapper',
    'Peozzle Platform':'wpb_wrapper',
    'Cloud-native technologies enable modular, scalable hiring and career services workflow automation.':'wpb_wrapper',
    'Patented Peozzle Technology':'wpb_wrapper',
    'The approved USPTO patents are powering the Peozzle platform. 1)Resource Distribution System 2)Multimedia Resume Distribution System.':'wpb_wrapper',
    'Peozzle Connect':'wpb_wrapper',
    'Help to build scalable enterprise solutions to broaden the talent management solutions.':'wpb_wrapper',
    'Peozzle Marketplace':'wpb_wrapper',
    'Peozzle marketplace includes technology and solution that help to build scalable enterprise solutions to broaden the talent management solutions.':'wpb_wrapper',
    'Peozzle AI/ML Model':'wpb_wrapper',
    'Purpose-driven screening and AI/ML model provide insights into the data-driven hiring process.':'wpb_wrapper',
    'Why Peozzle Platform?':'wpb_wrapper',
    'We are grounded in People First Approach; Peozzle Platform empowers the hiring team, candidates, students, university placement office, partners, and individuals in between to realize their fullest potential.':'wpb_wrapper',
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