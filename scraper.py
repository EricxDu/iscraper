import re
import requests
import sys

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("invoked:", sys.argv[0])
    print("usage:")
    print("  --url=<url>            download page at <url>")
    print("  --html=<filename>      use <filename> as page")
    print("  --table=<n>            select the <n>th table in the page")
    print("  --column=<n>           select the <n>th column in the table")
    print("  --print-data           print the text of each field selected")
    print("  --save-data=<filename> save the text of each field to <filename>")
    print("  --save-html=<filename> save downloaded page as <filename>")

def main():
    for arg in sys.argv:
        if arg[0:9] == "--column=":
            cnum = int(arg[9:])
        elif arg[0:7] == "--html=":
            filename = arg[7:]
            with open(filename) as file:
                text = file.read()
        elif arg == "--print-data":
            for line in get_data(text, tnum, cnum):
                print(line)
        elif arg[0:12] == "--save-data=":
            filename = arg[12:]
            print("scraper: saving fields to file", filename)
            with open(filename, "w") as file:
                for line in get_data(text, tnum, cnum):
                    file.write(line + "\n")
        elif arg[0:12] == "--save-html=":
            filename = arg[12:]
            soup = BeautifulSoup(text, 'html.parser')
            with open(filename, "w") as file:
                file.write(soup.prettify())
        elif arg[0:8] == "--table=":
            tnum = int(arg[8:])
        elif arg[0:6] == "--url=":
            url = arg[6:]
            r = requests.get(url)
            text = r.text

def get_data(text, tnum, cnum, patterns=(r'\[[^\]]*\]',)):
    datum = []
    soup = BeautifulSoup(text, 'html.parser')
    for i, table in enumerate(soup.find_all('table')):
        if i == tnum:
            for trow in table.find_all('tr'):
                for k, tdata in enumerate(trow.find_all('td')):
                    if k == cnum:
                        cat = ""
                        for string in tdata.strings:
                            string = string.replace("\"", "")
                            string = string.replace("'", "")
                            string = string.replace("(", "")
                            string = string.replace(")", "")
                            string = string.replace("\n", "")
                            for pattern in patterns:
                                string = re.sub(pattern, '', string)
                            cat = cat + string.strip()
                        datum.append(cat)
    return datum

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("Keyboard Interrupt (Control-C)...")
    sys.exit()
