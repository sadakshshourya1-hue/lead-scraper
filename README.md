# Public Business Lead Scraper

## Overview

This project is a simple lead generation scraper built using Python. It extracts publicly available business information from company websites and saves the results to a CSV file.

## Features

- Extracts company name (website title)
- Extracts email addresses
- Finds LinkedIn profile links
- Finds Instagram profile links
- Finds Facebook profile links
- Detects contact page links
- Exports the collected data to `leads.csv`

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- Regular Expressions (re)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sadakshshourya1-hue/lead-scraper.git
```

2. Navigate to the project folder:

```bash
cd lead-scraper
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python scraper.py
```

When prompted, enter a company website URL, for example:

```
python.org
```

The extracted information is automatically saved in a file named `leads.csv`.

## Example Output

| Company | Website | Emails | LinkedIn | Instagram | Facebook | Contact Page |
|---------|---------|---------|----------|-----------|----------|--------------|
| Welcome to Python.org | https://python.org | Not Found | https://www.linkedin.com/company/python-software-foundation/ | Not Found | Not Found | Not Found |

## Project Structure

```
lead-scraper/
│── scraper.py
│── README.md
│── requirements.txt
│── urls.txt
│── .gitignore
```

## Disclaimer

This project only collects publicly available information from company websites for educational purposes.