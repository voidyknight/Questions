import re
re.M

#BASIC REGEXES
d4 = "(\d{4})"
d2 = "(\d{2})"
titleword = "([A-Z][a-z]+)"

#MONTHS
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#data[D][M][Y]
data = [[[0 for x in range(1, 3001)] for x in range(1, 14)] for x in range(1, 33)]


def main(freq, string):
    slashdate_d4(string)
    slashdate_d2(string)
    worddate_md(string)
    worddate_dm(string)
    for y in range(1, 3000):
        for m in range(1, 13):
            for d in range(1, 32):
                if data[d][m][y] > 0:
                    freq["{0}/{1}/{2}".format(d,m,y)] = data[d][m][y]

#BUILT REGEXES    
def slashdate_d4(string):
    regex = re.compile("{0}/{1}/{2}".format(d2, d2, d4))
    for match in regex.findall(string):
        print "Match found: " + str(match)
        for index in range(0,2):
            try:
                data[int(match[index])][int(match[1 - index])][int(match[2])] += 1
            except IndexError:
                pass

def slashdate_d2(string):
    regex = re.compile("{0}/{1}/{2}".format(d2, d2, d2))
    for match in regex.findall(string):
        print "Match found: " + str(match)
        for index in range(1,3):
            for yr_offset in [1900, 2000]:
                try:
                    data[int(match[index])][int(match[1 - index])][int(match[2]) + yr_offset] += 1
                except IndexError:
                    pass

def worddate_md(string):
    regex = re.compile("{0} {1}, {2}".format(titleword, d2, d4))
    for match in regex.findall(string):
        print "Match found: " + str(match)
        for index in range(len(months)):
            if match[0][:3] == months[index]:
                try:
                    data[int(match[1])][index + 1][int(match[2])] += 1
                except IndexError:
                    pass
                break
                

def worddate_dm(string):
    regex = re.compile("{0} {1} {2}".format(d2, titleword, d4))
    for match in regex.findall(string):
        print "Match found: " + str(match)
        for index in range(len(months)):
            if match[1][:3] == months[index]:
                try:
                    data[int(match[0])][index + 1][int(match[2])] += 1 #M/D/Y
                except IndexError:
                    pass
                break

