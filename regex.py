import re
re.M

#BASIC REGEXES
d4 = "(\d{4})"
d2 = "(\d{2})"
titleword = "([A-Z][a-z]+)"

#BUILT REGEXES
slashdate_d2 = "%s/%s/%s".format(d2, d2, d2)
slashdate_d4 = "%s/%s/%s".format(d2, d2, d4)
worddate_md = "%s %s, %s".format(titleword, d2, d4)
worddate_dm = "%s %s, %s".format(d2, titleword, d4)
bc_year = "%s (BC|BCE)".format(d4)

data = [[[0 for x in range(-4000, 4000)] for x in range(1, 13)] for x in range(1, 32)]
#data[D][M][Y]

def parse(data, para, regex):
    
