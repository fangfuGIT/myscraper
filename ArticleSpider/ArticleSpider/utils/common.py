# -*- coding: utf-8 -*-

# Author： fangfu

import hashlib

def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()  #返回摘要，作为十六进制数据字符串值


# def md5(str):
#     m = hashlib.md5()
#     m.update(str)
#     return m.digest()  #返回摘要，作为二进制数据字符串值
#
# def hexmd5(str):
#     m = hashlib.md5()
#     m.update(str)
#     return m.hexdigest()  #返回摘要，作为十六进制数据字符串值



if __name__ == "__main__":
    print(get_md5("fangfu"))

    # str = "abcd"
    # str = str.encode("utf8")
    # print(md5(str))
    # print(hexmd5(str))



