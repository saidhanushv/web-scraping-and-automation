import requests
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22usersSearchTerm%22%3A%22Los%20Angeles%20CA%22%2C%22mapBounds%22%3A%7B%22north%22%3A34.60748837229978%2C" \
      "%22east%22%3A-117.68388826171875%2C%22south%22%3A33.430572537010455%2C%22west%22%3A-119.13957673828125%7D%2C" \
      "%22mapZoom%22%3A9%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C" \
      "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A514132%7D%2C" \
      "%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rad%22%3A%7B%22value%22%3A" \
      "%222023-09-01%22%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2600%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D" \
      "%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url=URL, headers=headers)
data = response.content
soup = BeautifulSoup(data, "html.parser")

ul_xpath = '//*[@id="grid-search-results"]/ul'

if response.status_code == 200:
    '''
        first class being all cards
        second class being "li"'s class
        third class being div element's class
    '''
    all_cards = soup.select(".List-c11n-8-84-3__sc-1smrmqp-0 .ListItem-c11n-8-84-3__sc-10e22w8-0 "
                            ".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 "
                            ".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
    prices = []
    addresses = []
    home_links = []
    for card in all_cards:
        money_obj = soup.find_all("div", {"class": "PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0"})
        for money in money_obj:
            price = money.get_text()
            price = price.replace("$", "").replace(",", "").replace("+ 1 bd", "").replace("/mo", "")
            price = int(price)
            prices.append(price)
    # print(prices)
    for card in all_cards:
        address_obj = soup.find_all("address")
        for address in address_obj:
            addresses.append(address.get_text())
    # print(addresses)
    for card in all_cards:
        address_links = soup.find_all("a", {"data-test": "property-card-link"})
        for link in address_links:
            href = link["href"]
            if not href.startswith("https://www.zillow.com/"):
                href = "https://www.zillow.com/"+href
            home_links.append(href)
    print(home_links)


else:
    print(response.status_code)