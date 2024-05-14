import re

pattern1 = (r'\d-\d$')
pattern2 = (r'Friendly')

with open ('./data.txt') as f:
    for line in f:
        res2 = re.search(pattern2, line)
        if res2:
            res1 = re.findall(pattern1, line)
            if res1:
                print(res1)

                