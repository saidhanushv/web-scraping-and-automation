import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = os.environ["URL"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url=URL, headers=headers)
data = response.content
soup = BeautifulSoup(data, "html.parser")

if response.status_code == 200:
    all_cards = soup.select(".List-c11n-8-84-3__sc-1smrmqp-0 .ListItem-c11n-8-84-3__sc-10e22w8-0 "
                            ".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 "
                            ".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")

    prices = [int(card.get_text().replace("$", "").replace(",", "").replace("+ 1 bd", "").replace("/mo", ""))
              for card in all_cards]

    addresses = [address.get_text() for address in soup.find_all("address")]

    home_links = [link["href"] if link["href"].startswith("https://www.zillow.com/") else "https://www.zillow.com/" + link["href"]
                  for link in soup.find_all("a", {"data-test": "property-card-link"})]
    time.sleep(3)
    driver.get(url=os.environ["FORM_LINK"])
    driver.fullscreen_window()

    property_rent = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    for rent, address, link in zip(prices, addresses, home_links):
        property_rent.send_keys(rent)
        property_address.send_keys(address)
        property_link.send_keys(link)
        submit_btn.click()
        driver.get(url=os.environ["FORM_LINK"])
        time.sleep(1)
    driver.quit()
else:
    print(response.status_code)