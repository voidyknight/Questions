#regex: [0-9]{1-2}/[0-9]{1-2}/
#just dates Sept. 22, 2014 or 09/09/09 or 09.09.09 or 09-09-09
import re
import google
re.M

question = "When did World War II begin?"

num_slash = re.compile("[0,9]{1,2}/[0,9]{1,2}/[0,9]{2,4}");
google.search(question);
