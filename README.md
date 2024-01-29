# AdvancedWebScraper

Welcome to AdvancedWebScraper, your ultimate companion for web data extraction! Our mission is to offer flexible and efficient solutions tailored to suit diverse web scraping needs. With our powerful duo of scripts – `GeneralScraper.py` and `AdvancedScraper.py` – we cater to both beginners and experts alike. Let's dive into what makes each script unique and indispensable.

## GeneralScraper.py

Our entry-level scraper, perfect for those starting their journey in web data extraction. Built on top of popular libraries like `requests`, `BeautifulSoup`, and `urllib`, this script provides essential functionality while maintaining simplicity.

### Features
- Easy-to-use interface guiding users through every step
- Supports four primary data extraction modes:
	+ Post content extraction (<p> tags)
	+ Internal and external link collection (<a> tags with href attributes)
	+ All visible text content aggregation
	+ Query-based search throughout the entire website

### Getting Started
To start using [GeneralScraper.py](https://github.com/mshojaei77/AdvancedWebScraper/blob/main/GeneralScraper.PY), follow these steps:

1. Ensure you have Python installed.
2. Install necessary packages:
```bash
pip install requests beautifulsoup4
```
3. Run the script:
```bash
python GeneralScraper.py
```

### Required Packages
- [`requests==2.31.0`](https://pypi.org/project/requests/)
- [`beautifulsoup4==4.12.2`](https://pypi.org/project/beautifulsoup4/)

### Usage
1. Provide the target URL when prompted, ensuring it includes either "http://" or "https://".
2. Select a data extraction method based on the options presented:
	* 0: Extract post contents (typically <p> tags)
	* 1: Gather internal & external links (<a> tags with href attribute)
	* 2: Collect all visible text contents
	* 3: Perform a query-based search across the whole website; input the desired query upon request
3. View the extracted results according to your selection. No matching data? Don't worry—we display helpful messages too!

Happy responsible scraping! Always remember to adhere to site owners' terms and conditions. Explore wisely! 😊✨

---

## AdvancedScraper.py

Unleash the full potential of web scraping with our cutting-edge solution powered by the renowned [Playwright library](https://github.com/microsoft/playwright-python). Designed specifically for experienced developers seeking intricate control over their projects, this script delivers unparalleled performance and adaptability.

### Features ✨

- Comprehensive support for five data extraction techniques:
	+ Extract posts `(DataType.POSTS)`
	+ Extract all links `(DataType.LINKS)`
	+ Extract all texts `(DataType.ALL_TEXTS)`
	+ Search by query `(DataType.SEARCH_QUERY)`
	+ Custom tag extraction `(DataType.CUSTOM_TAG)`
- Multiple output formats available:
	+ Print `(OutputFormat.PRINT)`
	+ Text File `(OutputFormat.TEXT_FILE)`
	+ Json `(OutputFormat.JSON)`
	+ CSV `(OutputFormat.CSV)`

[AdvancedScraper](https://github.com/mshojaei77/AdvancedWebScraper/blob/main/AdvancedScraper.PY)

### Requirements 📋

- Python >= 3.7 or upper
- [`playwright 1.41.1`](https://github.com/microsoft/playwright-python) package installed

### Setup Instructions
1. Meet the prerequisites:
	* Python installation
	* Access to the internet for downloading the required package
2. Set up the environment:
```bash
pip install -U playwright
```
```bash
playwright install
```

---

## Contribution Guidelines
We welcome contributions from anyone interested in enhancing our web scraping tools! To ensure seamless collaboration, please review our contribution guidelines carefully.

## License
Distributed under the MIT license. For more information, see [LICENSE](./LICENSE).
