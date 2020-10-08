temp = set(values[0])
for item in values[1:]:
    temp = temp.intersection(set(item))
from collections import defaultdict
a = defaultdict()


return list(temp)