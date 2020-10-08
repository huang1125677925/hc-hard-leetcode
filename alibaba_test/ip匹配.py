import re

line = "55.255.255.255"

matchObj = re.match(r'^([0-9]{1}?|[1-9]{1}[0-9]{1}?|[1]{1}[0-9]{2}?|[2]{1}[0-5]{2})\.(\d+?)\.(\d+?)\.(\d+?)$', line)

if matchObj:
    print "matchObj.group() : ", matchObj.groups()
else:
    print "No match!!"