# Advanced Web Scraper

 Welcome to Advanced Web Scraper, your ultimate companion for web data extraction! We provide flexible and powerful solutions tailored to meet various web scraping requirements. Our toolkit consists of two robust scripts: `GeneralScraper.py` and `AdvancedScraper.py`. This README will introduce you to their unique features and capabilities.

 ## Comparison Table

 Here's a feature comparison between the two scripts in a tabular format:

| Feature / Aspect           | GeneralScraper.py   | AdvancedScraper.py     |
|---|---|---|
| Framework                | Requests & Beautiful Soup | Playwright             |
| Network Resilience       | Exponential Backoff | Handled by Playwright  |
| Scraping Method          | HTML Parser         | Browser Automation      |
| Relative Links Handling  | urljoin() Function  | Built-in Functionality  |
| Real-time Rendering      | No                  | Yes                    |
| JavaScript Support       | Limited             | Full                   |
| Data Types               | Posts, Links, Texts, Query | Enumerated types       |
| Custom Tag Selection     | No                  | Yes                    |
| Error Handling           | Print Statements    | Print Statements        |
| Result Display            | Console Printing    | Console Printing        |
| Saving Results           | Not Implemented     | Multiple Formats Supported |
| Usage                    | Simple, Less Powerful | More Complex, More Powerful |

## GeneralScraper.py

Our beginner-friendly scraper designed for individuals new to web data extraction. It leverages popular libraries such as `requests`, `BeautifulSoup`, and `urllib` to deliver essential functionalities while keeping things simple.

**Features:**

- User-friendly interface guiding users through each step
- Four primary data extraction methods:
  - Extract post contents (`<p>` tags)
  - Collect internal and external links (`<a>` tags with `href` attributes)
  - Aggregate all visible text contents
  - Perform query-based searches across the entire website

**Getting Started:**

1. Make sure you have Python installed.
2. Install necessary packages:
   ```
   pip install requests beautifulsoup4
   ```
3. Run the script:
   ```
   python GeneralScraper.py
   ```

**Required Packages:**

- [`requests==2.31.0`](https://pypi.org/project/requests/)
- [`beautifulsoup4==4.12.2`](https://pypi.org/project/beautifulsoup4/)

**Usage:**

1. Enter the target URL when prompted, making sure it starts with 'http://' or 'https://'.
2. Choose a data extraction method based on the provided options:
   * 0: Extract post contents (typically `<p>` tags)
   * 1: Gather internal & external links (`<a>` tags with `href` attribute)
   * 2: Collect all visible text contents
   * 3: Conduct a query-based search across the whole website; enter the desired query when requested
3. Review the extracted results corresponding to your selection. If no matches are found, don't worry—helpful messages will be displayed!

Happy responsible scraping! Remember always to abide by site owners' terms and conditions. Explore wisely! 😊✨

---

## AdvancedScraper.py

Unlock advanced web scraping capabilities with our state-of-the-art solution driven by the acclaimed [Playwright library](https://github.com/microsoft/playwright-python). Specifically crafted for seasoned developers demanding fine-grained project control, this script offers superior performance and versatility.

**Features ✨:**

- Five comprehensive data extraction techniques:
  - Extract posts (`DataType.POSTS`)
  - Extract all links (`DataType.LINKS`)
  - Extract all texts (`DataType.ALL_TEXTS`)
  - Search by query (`DataType.SEARCH_QUERY`)
  - Custom tag extraction (`DataType.CUSTOM_TAG`)
- Multiple output formats available:
  - Print (`OutputFormat.PRINT`)
  - Text File (`OutputFormat.TEXT_FILE`)
  - JSON (`OutputFormat.JSON`)
  - CSV (`OutputFormat.CSV`)

**Requirements 📋:**

- Python >= 3.7 or higher
- [`playwright 1.41.1`](https://github.com/microsoft/playwright-python) package installed

**Setup Instructions:**

1. Fulfill the prerequisites:
   - Python installation
   - Internet access for downloading the required package
2. Install Playwright Library: Once inside the activated virtual environment, install the playwright library:
```bash
pip install playwright
```
3. Install Required Browsers: With the playwright library installed, go ahead and include the supported browsers:
```bash
playwright install
```
5. Run the Script: Finally, execute the AdvancedScraper.py script within the active virtual environment:
```bash
python AdvancedScraper.py
```
---

## Contribution Guidelines

We appreciate any contributions towards improving our web scraping tools! Please familiarize yourself with our [contribution guidelines](CONTRIBUTING.md) before getting started.

## License

This project is distributed under the [MIT License](LICENSE).
