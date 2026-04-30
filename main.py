from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://www.scrapethissite.com/pages/simple/")
time.sleep(2)

# Wait for the page to load
WebDriverWait(driver,  10).until(
    expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".col-md-4"))
)

data = []

countries = driver.find_elements(By.CSS_SELECTOR, ".col-md-4")

for country in countries:
    name = country.find_element(By.CSS_SELECTOR, ".country-name").text.strip()
    capital = country.find_element(By.CSS_SELECTOR, ".country-capital").text.strip()
    population = country.find_element(By.CSS_SELECTOR, ".country-population").text.strip()

    data.append({
        "name" : name,
        "capital" : capital,
        "population" : population
        })

print(data)
driver.quit()