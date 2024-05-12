#!/usr/bin/python

import re

# pattern = re.compile(r'^(\d{4,4})\-\d\d-\d\d,(.*),Friendly,.*$')

# # ^(\d{4,4})\-\d\d-\d\d,(.*),Friendly,.*$

# # 2018-06-04,Serbia,Chile,0,1,Friendly,Graz,Austria,TRUE
# with open("/home/francisco/Documents/expresiones_regulares/results_proyecto.csv", "r") as f:
#     # for line in f: 
#     #     print(line)
#     for line in f: 
#         res = re.match(pattern, line)
#         if res:
#             print(f'{res.group(2)}\n')

pattern = re.compile(r'^.*,.*,.*,(\d),(\d).*$')

# ^.*,.*,.*,(\d),(\d).*$

# 2018-06-04,Serbia,Chile,0,1,Friendly,Graz,Austria,TRUE
with open("/home/francisco/Documents/expresiones_regulares/results_proyecto.csv", "r") as f:
    for line in f:
        res = re.match(pattern, line)
        if res:
            sum = int(res.group(1)) + int(res.group(2))
            if sum > 10:
                print(sum)