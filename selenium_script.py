from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "view/index.html"  

# Configuring Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = None
try:
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=options, executable_path='chromedriver')

    # Open the web page
    driver.get(url)

    # Get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Check if the HTML structure is appropriate
    if soup.find('html') and soup.find('head') and soup.find('body'):
        print("Test Passed: HTML file has appropriate format.")
    else:
        print("Test Failed: HTML file does not have appropriate format.")
finally:
    # Close the WebDriver
    if driver:
        driver.quit()
