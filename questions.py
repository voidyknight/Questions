#regex: [0-9]{1-2}/[0-9]{1-2}/
#just dates Sept. 22, 2014 or 09/09/09 or 09.09.09 or 09-09-09
#pythonhosted.org//google/

import re
import google
from bs4 import BeautifulSoup

re.M #Enable multiline searching

question = "When did World War II begin?"
query_types = ["when", "who"]

num_slash = re.compile("[0,9]{1,2}/[0,9]{1,2}/[0,9]{2,4}");

pages = google.search(question,
              start=1,
              stop=7,
              pause=.2
                  );

pages.next()
print google.get_page(pages.next())
