from bs4 import BeautifulSoup
import lxml
import os
import re
from pprint import pprint


# Done
def parse(path_to_file):
    html = open(path_to_file, 'r', encoding='utf-8')
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find(id='bodyContent')

    imgs = 0
    images = body.find_all('img')
    for i in range(len(images)):
        try:
            curr_img = images[i]['width']
            if int(curr_img) >= 200:
                imgs += 1
        except KeyError:
            pass

    headers_count = 0
    list_of_tags_h = ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')
    for h in list_of_tags_h:
        headers = body.find_all(h)
        for _ in headers:
            letters = list(_.text)
            if letters[0] in ['E', 'T', 'C']:
                headers_count += 1

    lists = 0
    all_lists = body.find_all(['ul', 'ol'])
    for tag in all_lists:
        if not tag.find_parents(['ul', 'ol']):
            lists += 1

    max_count = 0
    all_links = body.find_all('a')
    for link in all_links:
        current_count = 1
        siblings = link.find_next_siblings()
        for sibling in siblings:
            if sibling.name == 'a':
                current_count += 1
                max_count = max(current_count, max_count)
            else:
                current_count = 0

    return [imgs, headers_count, max_count, lists]
