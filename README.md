# Table Scraper

a Python module to scrape information from HTML tables.

## Requirements

    pip install beautifulsoup
    pip install requests

## Usage

Table Scraper can download the HTML from any URL and save it for later, 
so you don't have to query the website every time you parse the file.

- python3 scraper.py --url="https://a.website.url/page_name" --save-html=page.html

To do anything with the data, the page must have at least one <table> 
tag and you must provide a table number and a column number to lookup.

- python3 scraper.py --html=page.html --table=0 --column=1 --print-data

You can save the table data to a file with one line per field found.

- python3 scraper.py --html=page.html --table=1 --column=0 --save-data=filename.txt
