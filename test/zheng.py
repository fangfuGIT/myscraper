# ^ $ * ? + {2} {2,} {2,6} |
# [] [^] [a-z] () .
# \s \S \w \W
# [\u4E00-\u9FA5] \d

import re

# line = "python汉字2"
# str = "ppp"
# match = re.match(str, line)
# if match:
#     #print(match.group(1))
#     print("yes")
# else:
#     print("no")

match = re.match(".*?(\d+).*","23456 收藏 ")
if match:
    print(match.group(1))