#AdvancedScraper.PY

import re
import asyncio
import json
import csv
from enum import Enum
from playwright.async_api import async_playwright

class DataType(Enum):
    POSTS = 0
    LINKS = 1
    ALL_TEXTS = 2
    SEARCH_QUERY = 3
    CUSTOM_TAG = 4

class OutputFormat(Enum):
    PRINT = 0
    TEXT_FILE = 1
    JSON = 2
    CSV = 3

class AdvancedWebScraper:
    def __init__(self):
        self.results = []

    async def extract_data(self, page, url, data_type, query=None, custom_tag=None):
        try:
            await page.goto(url)

            if data_type == DataType.POSTS.value:
                self.results = await self._extract_paragraphs(page)
            elif data_type == DataType.LINKS.value:
                self.results = await self._extract_links(page, url)
            elif data_type == DataType.ALL_TEXTS.value:
                self.results = await self._extract_all_texts(page)
            elif data_type == DataType.SEARCH_QUERY.value and query:
                self.results = await self._search_by_query(page, query)
            elif data_type == DataType.CUSTOM_TAG.value and custom_tag:
                self.results = await self._extract_custom_elements(page, custom_tag)
            else:
                print("Invalid data type or missing query.")
                return

        except Exception as e:
            print(f"Error during request: {e}")
            return

    async def _extract_paragraphs(self, page):
        return await page.eval_on_selector_all("p", "(paragraphs) => paragraphs.map(p => p.textContent.trim())")

    async def _extract_links(self, page, base_url):
        return await page.eval_on_selector_all("a[href]", f"(links, base) => links.map(link => new URL(link.href, base).toString())", base_url)

    async def _extract_all_texts(self, page):
        return await page.eval_on_selector_all("*", "(elements) => elements.map(element => element.textContent.trim())")

    async def _search_by_query(self, page, query):
        return await page.eval_on_selector_all("*", f"(elements, query) => elements.filter(element => element.textContent.lower().includes(query.lower())).map(element => element.textContent.trim())", query)

    async def _extract_custom_elements(self, page, custom_tag):
        return await page.eval_on_selector_all(custom_tag, f"(customElements) => customElements.map(element => element.textContent.trim())")

    def clean_text(self, text):
        cleaned_text = re.sub(r'\s+', ' ', text)
        return cleaned_text.strip()

    def display_results(self, clean=False):
        print("\nResults:")

        if self.results:
            for result in self.results:
                cleaned_result = self.clean_text(result) if clean else result
                print(f"{cleaned_result}\n")
        else:
            print("No data found based on the specified criteria.")

    def save_results(self, output_format):
        if output_format == OutputFormat.TEXT_FILE.value:
            self.save_results_to_text_file()
        elif output_format == OutputFormat.JSON.value:
            self.save_results_to_json()
        elif output_format == OutputFormat.CSV.value:
            self.save_results_to_csv()
        elif output_format == OutputFormat.PRINT.value:
            pass  # Results are already printed

    def save_results_to_text_file(self):
        with open('output.txt', 'w', encoding='utf-8') as file:
            for result in self.results:
                file.write(result + '\n')
        print("Data saved to output.txt")

    def save_results_to_json(self):
        with open('output.json', 'w', encoding='utf-8') as file:
            json.dump(self.results, file, indent=2)
        print("Data saved to output.json")

    def save_results_to_csv(self):
        with open('output.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Result'])
            for result in self.results:
                csv_writer.writerow([result])
        print("Data saved to output.csv")

async def main():
    scraper = AdvancedWebScraper()

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        url = input("Please enter the URL: ")

        while True:
            try:
                data_type = int(input(f"Please enter data type {', '.join([f'({dt.value}: {dt.name})' for dt in DataType])}: "))
                if data_type in DataType._value2member_map_:
                    break
                else:
                    print("Invalid data type. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        query = input("Enter the query: ") if data_type == DataType.SEARCH_QUERY.value else None
        custom_tag = input("Enter Custom Tag: ") if data_type == DataType.CUSTOM_TAG.value else None

        try:
            await scraper.extract_data(page, url, data_type, query, custom_tag)
            scraper.display_results(clean=True)

            # Offer user choice to print, save as a text file, JSON, or CSV
            output_format = int(input("Save output as (1: text file, 2: json, 3: csv): "))
            if 0 <= output_format <= 3:
                scraper.save_results(output_format)

        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
