# -*- coding: utf-8 -*-

# Author： fangfu


from scrapy.cmdline import execute
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 追加一个脚本所在的路径作为环境变量，注意sys.path的用法
# os.path.abspath(__file__) 获取当前文件路径,这个命令只能在脚本中使用，os.path.dirname获取文件的父目录,
# 通常这两个都是结合使用，来获取文件所在的父路径

execute(["scrapy", "crawl", "jobbole"])



