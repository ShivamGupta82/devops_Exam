from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "file:////views/index.html"

# Configuring Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Creating a WebDriver instance
driver = webdriver.Chrome(options=options)

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

# Close the WebDriver
driver.quit()
