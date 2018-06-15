# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:16:49 2018

Taken From Web Scraping, O'Rielly

@author: SIDHARTH
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
    
title = getTitle('http://www.reddit.com/r/linux')
if title ==None:
    print('Title could not be found')
else:
    print(title)


    

