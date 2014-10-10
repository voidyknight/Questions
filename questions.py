#regex: [0-9]{1-2}/[0-9]{1-2}/
#just dates Sept. 22, 2014 or 09/09/09 or 09.09.09 or 09-09-09
#pythonhosted.org//google/

import re
import google
from bs4 import BeautifulSoup

re.M #Enable multiline searching

question = "When did World War II begin?"
query_types = ["when", "who"]

regex = re.compile("[0,9]{1,2}/[0,9]{1,2}/[0,9]{2,4}");

pages = google.search(question,
              start=1,
              stop=7,
              pause=.2
                  );

pages.next()
rawHTML = google.get_page(pages.next())
soup = BeautifulSoup(rawHTML)
paragraph = soup.find_all('p')


for index in range(0, len(paragraph)):
    paragraph[index] = paragraph[index].string


numCount = {}

for item in paragraph:
    list = regex.findall(unicode(item))
    print item
    for date in list:
        if date not in numCount:
            numCount[date] = 0
        numCount[date] += 1

print numCount
    
    
