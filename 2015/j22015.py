__author__ = 'robuntu'
import sys

line = sys.stdin.readline()

happy_count = 0
sad_count = 0

emoticon = ""
i = 0

while i < len(line):
    if line[i] == ":":
        if line[i:i+3] == ":-)":
            happy_count += 1
            i += 3
        elif line[i:i+3] == ":-(":
            sad_count += 1
            i += 3
        else:
            i+=1
    else:
        i += 1

if happy_count == 0 and sad_count == 0:
    print "none"
elif happy_count > sad_count:
    print "happy"
elif sad_count > happy_count:
    print "sad"
else:
    print "unsure"

