import re
re.M

#BASIC REGEXES
d4 = "(\d{4})"
d2 = "(\d{2})"
titleword = "([A-Z][a-z]+)"

#BUILT REGEXES    
class slashdate_d4:
    regex = "%s/%s/%s".format(d2, d2, d4)

class slashdate_d2:
    regex = "%s/%s/%s".format(d2, d2, d2)

class worddate_md:
    regex = "%s %s, %s".format(titleword, d2, d4)

class worddate_dm:
    regex = "%s %s, %s".format(d2, titleword, d4)

class bc_year:
    regex  = "%s (BC|BCE)".format(d4)

data = [[[0 for x in range(-4000, 4000)] for x in range(1, 13)] for x in range(1, 32)]
#data[D][M][Y]

def parse(data, para, regex):
