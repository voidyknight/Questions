#pythonhosted.org//google/
import google
from urllib import urlopen
from bs4 import BeautifulSoup

import regex_who
import regex_when

question = "When did World War II start?"

def main(question):
    query_type = get_query_type(question)
    if query_type == "":
        return {}

    print "Query Type: " + query_type
    freq = {}
    pages = google.search(question, start=1, stop=20, pause=.2)
    for page in pages:
        try:
            print "Reading " + page + "..."
            fil = urlopen(page)
            parse(fil.read(), freq, query_type)
            fil.close()
        except Exception as e:
            print e
    return freq

def get_query_type(question):
    query_types = ["when", "who"]
    for query_type in query_types:
        if query_type in question.lower():
            return query_type
    return ""

def parse(page, freq, query_type):
    text = get_text(page)
    if query_type == 'who':
        regex_who.main(freq, text)
    elif query_type == 'when':
        regex_when.main(freq, text)

def get_text(page):
    soup = BeautifulSoup(page)
    return soup.body.get_text(strip=True)

if __name__ == "__main__":
    print main(question)
