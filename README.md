# AdvancedWebScraper

## Overview

**AdvancedWebScraper** is a comprehensive web scraping tool designed to empower users with versatile data extraction capabilities. This project consists of two robust scripts: `GeneralScraper.py` and `AdvancedScraper.py`. Each script offers distinct features and levels of customization, providing users with flexibility and efficiency for various web scraping tasks.

### 1. GeneralScraper.py

#### Description

The `GeneralScraper.py` script simplifies web scraping tasks with an intuitive user interface. Key features include improved network resilience, support for multiple data types, and the ability to handle search queries. Users can extract text, links, or specific content from a webpage effortlessly.

#### Usage

1. **Run the script:**
   ```bash
   python GeneralScraper.py
   ```
2. **Enter the URL of the webpage.**
3. **Choose the data type:**
   - `0`: Extract all paragraphs (posts).
   - `1`: Extract all links.
   - `2`: Extract all text content.
   - `3`: Search for a specific query in the text content.
4. **For data type 3, enter the search query.**
5. **View the scraped data.**

### 2. AdvancedScraper.py

#### Description

The `AdvancedScraper.py` script elevates web scraping with asynchronous data extraction using Playwright. It supports various data types, custom HTML tags, and flexible output formats (print, text file, JSON, CSV). Users can input parameters for a highly customizable scraping experience.

#### Usage

1. **Run the script:**
   ```bash
   python AdvancedScraper.py
   ```
2. **Enter the URL of the webpage.**
3. **Choose the data type:**
   - `0`: Extract all paragraphs (posts).
   - `1`: Extract all links.
   - `2`: Extract all text content.
   - `3`: Search for a specific query in the text content.
   - `4`: Extract content based on a custom HTML tag.
4. **For data types 3 and 4, enter the search query or custom HTML tag, respectively.**
5. **Choose the output format:**
   - `0`: Print results.
   - `1`: Save results to a text file.
   - `2`: Save results to JSON.
   - `3`: Save results to CSV.
6. **View or save the scraped data.**

## Enhancing Output with DataSpeakGPT

Users can further enhance and summarize their scraped data by feeding it into [DataSpeakGPT](https://github.com/mshojaei77/DataSpeakGPT), a powerful language model. DataSpeakGPT leverages GPT-3.5 Turbo for advanced natural language understanding and can provide valuable insights into the extracted content.

## Dependencies

- `requests`
- `bs4` (Beautiful Soup)
- `urllib.parse`
- `time`
- `asyncio`
- `json`
- `csv`
- `enum`
- `re`
- `playwright`

## Installation

1. **Install Python (if not already installed).**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Examples

### GeneralScraper.py

```bash
python GeneralScraper.py
```

### AdvancedScraper.py

```bash
python AdvancedScraper.py
```

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Enhance your web scraping capabilities with **AdvancedWebScraper**. Choose the level of customization that suits your needs and efficiently extract valuable data from web pages. After scraping, leverage the power of [DataSpeakGPT](https://github.com/mshojaei77/DataSpeakGPT) to further understand and summarize your extracted content. Happy scraping!
