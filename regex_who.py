import re

def main(freq, string):
    re_caps = re.compile('[A-Z][a-z]+')
    for match in re_caps.findall(string):
        print "Match found: " + match
        if not match in freq:
            freq[match] = 0
        freq[match] += 1
