#pythonhosted.org//google/
import google
import regex
from bs4 import BeautifulSoup

question = "When did World War II begin?"
query_types = ["when", "who"]

numCount = {}

def query(question):
    pages = google.search(question,
                          start=1,
                          stop=7,
                          pause=.2)
    return pages
        
def parse_all(pages, num_count):
    (parse(page, numcount) for page in pages)

def parse(page, num_count):
    paras = get_text(page)

def get_text(page):
    soup = BeautifulSoup(page)
    l_tags = soup.find_all('p')
    paras = [len(l_tags)]
    for index in range(0, len(l_tags)):
        paras[index] = unicode(l_tags[index].string)
    return paras
