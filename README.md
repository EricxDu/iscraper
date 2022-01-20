# Table Scraper

a Python module to scrape information from HTML tables.

## Requirements

    pip install beautifulsoup
    pip install requests

## Usage

Table Scraper can download the HTML from any URL and save it for later, 
so you don't have to query the website every time you parse the file.

- python3 scraper.py --url="https://en.wikipedia.org/wiki/List_of_Cheers_episodes" --save-html=page.html

To do anything with the data, the page must have at least one "table" 
tag and you must provide a table number and a column number to lookup.

- python3 scraper.py --html=page.html --table=1 --column=1 --print-data

<pre>
Give Me a Ring Sometime
Sams Women
The Tortelli Tort
Sam at Eleven
Coachs Daughter
Any Friend of Dianes
Friends, Romans, Accountants
Truce or Consequences
Coach Returns to Action
Endless Slumper
One for the Book
The Spy Who Came In for a Cold One
Now Pitching, Sam Malone
Let Me Count the Ways
Father Knows Last
The Boys in the Bar
Dianes Perfect Date
No Contest
Pick a Con... Any Con
Someone Single, Someone Blue
Showdown, Part 1
Showdown, Part 2
</pre>

You can save the table data to a file with one line per field found.

- python3 scraper.py --html=page.html --table=1 --column=1 --save-data=filename.txt

<pre>
tabscraps: saving fields to file filename.txt
</pre>

- cat filename.txt

<pre>
Give Me a Ring Sometime
Sams Women
The Tortelli Tort
Sam at Eleven
Coachs Daughter
Any Friend of Dianes
Friends, Romans, Accountants
Truce or Consequences
Coach Returns to Action
Endless Slumper
One for the Book
The Spy Who Came In for a Cold One
Now Pitching, Sam Malone
Let Me Count the Ways
Father Knows Last
The Boys in the Bar
Dianes Perfect Date
No Contest
Pick a Con... Any Con
Someone Single, Someone Blue
Showdown, Part 1
Showdown, Part 2
</pre>
