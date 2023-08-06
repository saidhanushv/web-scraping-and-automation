# Zillow Property Data Scraper and Form Submission🤖

This Python script fetches property data from Zillow, including property prices, addresses, and links to individual property pages, and submits the data to a Google Form using Selenium.

## Requirements

- Python 3.x
- Chrome WebDriver (compatible with the installed Chrome browser version)
- Google Chrome browser
- Libraries:
  - os
  - time
  - requests
  - BeautifulSoup (from bs4)
  - selenium

## Installation

1. Install Python 3.x from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Download the Chrome WebDriver that matches your Chrome browser version from: [Chrome WebDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place it in a directory included in your system's PATH variable.
3. Install required libraries using pip:

```bash
pip install requests beautifulsoup4 selenium
```
## How It Works
1. The script starts by making a request to the Zillow URL specified in the environment variable URL, using the requests library. It pretends to be a user agent using the headers dictionary.
2. The fetched HTML content is parsed using BeautifulSoup to extract property data, including prices, addresses, and property page links.
3. The script then uses Selenium to automate the Google Form submission. It opens the Google Form specified in the environment variable FORM_LINK using the Chrome WebDriver.
4. For each property, the script fills out the corresponding form fields (property rent, address, and link) and submits the form data.
5. After each submission, the script waits for a brief period to avoid overloading the server.
6. The process continues until all properties' data is submitted.
7. Finally, the Chrome WebDriver is closed using driver.quit().

## Usage
1. Set up the environment variables:
  - URL: The Zillow URL to scrape property data from.
  - FORM_LINK: The Google Form link to submit the data to.
2. Run the Python script:
  ```python your_script_name.py```

### Quick Note
I am looking for a collaborator to work with Selenium automation challenges in this project. If you have experience in Selenium or any suggestions for improvements, feel free to reach out to me. You can find my contact information in my profile xD. Looking forward to connecting with potential collaborators!

## Disclaimer
This script is only a personal project to understand how web scraping works ie.., for educational purposes only. The usage of this script may violate Zillow's terms of service, and scraping websites without permission may be illegal in some jurisdictions. Use it responsibly and at your own risk.

Please note that web scraping may put a strain on the target website's servers. Be considerate and use reasonable scraping rates to avoid overwhelming the server and causing any inconvenience.
