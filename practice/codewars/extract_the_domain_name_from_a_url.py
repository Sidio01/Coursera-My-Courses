"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
from icecream import ic
import re
import requests
import copy


def domain_name(url):
    x = re.split(r'[/]+', url)
    if len(x) >= 2:
        x = x[1]
    else:
        x = x[0]
    x = re.split(r'\.', x)[::-1]
    y = requests.request(
        'GET', 'https://publicsuffix.org/list/public_suffix_list.dat').text.split('\n')
    li = []
    for i in y:
        z = re.findall(r'\/{2}', i)
        if i in ['', 'google', 'youtube']:
            continue
        if not z:
            li.append(i)
    x1 = copy.deepcopy(x)
    for i in x1:
        if i in li:
            x.remove(i)
    # print(y)
    return x[0]



li = ["http://github.com/carbonfive/raygun",
      "http://www.zombie-bites.com",
      "https://www.cnet.com",
      "www.xakep.ru",
      "http://google.com",
      "http://google.co.jp",
      "https://youtube.com",
      "https://img.www.youtube.com"]

for i in li:
    ic(domain_name(i))
