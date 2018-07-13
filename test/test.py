# -*- coding: utf-8 -*-

# Author： fangfu

import re

list1 = ["abcd", "123456  ", "city", "job"]
list2 = [num for num in list1 if not num.strip().endswith("6")]
list3 = [num for num in list1 if num.strip().endswith("6")]
list = ",".join(list2)
#join是把字符串/列表/元组/字典中的所有元素转换为一个字符串，如上例，以","分隔
print(list2)
print(list3)
print(list)