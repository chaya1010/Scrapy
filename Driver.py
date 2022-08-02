from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def createDriver(site = 'https://www.google.com/', results = False, size = None, infobar = True, timeout = 0):
    options = webdriver.ChromeOptions()
    if size == "max":
        options.add_argument("start-maximized")
    if not infobar:
        options.add_argument("disable-infobars")
        
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
    site = site
    if results:
        driver = webdriver.Chrome(executable_path='chrome_driver\chromedriver.exe')
    else:
        driver = webdriver.Chrome(executable_path='chrome_driver\chromedriver.exe', options=options)
    
    if timeout:
        driver.set_page_load_timeout(timeout)
        
    driver.get(site)
    
    return driver

def scroll():
    return

def find_class(driver, class_name):
    if not driver or not class_name:
        if not driver:
            print("driver input is empty")
        if not class_name:
            print("class input is empty")
            
    try:
        dv = driver.find_elements(By.CLASS_NAME,class_name)
        return dv
    except Exception as e:
        print(e)
        
    return "error"

def link():
    return