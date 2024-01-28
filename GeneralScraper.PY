#GeneralScraper.PY

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class AdvancedWebScraper:
    def __init__(self):
        self.results = []

    def extract_data(self, url, data_type, query=None):
        try:
            # Improved network resilience with exponential backoff for retries
            max_retries = 3
            for retry in range(max_retries):
                response = requests.get(url, allow_redirects=True, timeout=10)
                if response.status_code == 200:
                    break
                else:
                    print(f"Failed to fetch the page. HTTP Status Code: {response.status_code}. Retrying in {2 ** retry} seconds...")
                    time.sleep(2 ** retry)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                if data_type == 0:
                    # Extract all text content from the page
                    self.results = [paragraph.text.strip() for paragraph in soup.find_all("p")]
                elif data_type == 1:
                    # Extract all links from the page, handling relative URLs
                    self.results = [urljoin(url, link.get("href")) for link in soup.find_all("a") if link.get("href")]
                elif data_type == 2:
                    # Extract all text content from the page
                    self.results = [text.strip() for text in soup.stripped_strings]
                elif data_type == 3 and query:
                    # Extract all text content that includes the search query, case-insensitive
                    self.results = [text for text in soup.stripped_strings if query.lower() in text.lower()]
                else:
                    print("Invalid data type or missing query.")
                    return
            else:
                print(f"Failed to fetch the page. HTTP Status Code: {response.status_code}")
                return

        except requests.RequestException as e:
            print(f"Error during request: {e}")
            return

    def display_results(self):
        print("Scraped Data:")
        if self.results:
            for result in self.results:
                print(result)
                print()
        else:
            print("No data found based on the specified criteria.")

if __name__ == "__main__":
    scraper = AdvancedWebScraper()

    # User input validation
    while True:
        url = input("Please enter the URL: ")
        if url:
            break
        else:
            print("Invalid URL. Please try again.")

    # Validate and handle data type input
    while True:
        try:
            data_type = int(input("Please enter data type (0: posts, 1: links, 2: all texts, 3: search query): "))
            if data_type in {0, 1, 2, 3}:
                break
            else:
                print("Invalid data type. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if data_type == 3:
        while True:
            query = input("Enter the query: ")
            if query:
                break
            else:
                print("Invalid query. Please try again.")

        print(f"Extracting all texts including '{query}'...")
        scraper.extract_data(url, data_type, query)
    else:
        print(f"Extracting data type {data_type}...")
        scraper.extract_data(url, data_type)

    scraper.display_results()
