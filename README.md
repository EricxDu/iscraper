# Table Scraper

a Python module to scrape information from HTML tables.

## Requirements

    pip install beautifulsoup
    pip install requests

## Usage

Table Scraper can download the HTML from any URL and save it for later, 
so you don't have to query the website every time you parse the file.

- <code>python3 scraper.py --url="https://en.wikipedia.org/wiki/List_of_Cheers_episodes" --save-html=page.html</code>

To do anything with the data, the page must have at least one "table" 
tag and you must provide a table number and a column number to lookup.

- <code>python3 scraper.py --html=page.html --table=1 --column=1 --print-data</code>

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

- <code>python3 scraper.py --html=page.html --table=3 --column=1 --save-data=filename.txt</code>

<pre>
tabscraps: saving fields to file filename.txt
</pre>

- <code>cat filename.txt</code>

<pre>
Power Play
Lil Sister Dont ChaLittle Sister Dont Cha
Personal Business
Homicidal Ham
Sumners Return
Affairs of the Heart
Old Flames
Manager Coach
They Called Me Mayday
How Do I Love Thee, Let Me Call You Back
Just Three Friends
Where Theres a Will...
Battle of the Exes
No Help Wanted
And Coachie Makes Three
Cliffs Rocky Moment
Fortune and Mens Weight
Snow Job
Coach Buries a Grudge
Normans Conquest
Ill Be Seeing You, Part 1
Ill Be Seeing You, Part 2
</pre>

## To Do

- customize how the perser strips whitespace and characters from the
  table data
- automatically save columns to files named after column header
