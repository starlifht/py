# !/usr/bin/env python
# encoding: utf-8


__author__ = 'STAR'

import json
import urllib2
import urllib
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')
ISOTIMEFORMAT = '%Y-%m-%d %X'

def getTime():
    return time.strftime(ISOTIMEFORMAT, time.localtime())

def getHtml(url, data):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    # url=urllib2.quote(url.encode('utf-8'))
    data = urllib.urlencode(data)
    r = urllib2.Request(url)
    r.add_header('User-Agent', user_agent)
    page = urllib2.urlopen(r, data, timeout=6)
    htmltest = page.read()
    return htmltest


def getRating(kw):
    data = {"q": kw}
    jsonqw = getHtml('https://api.douban.com/v2/movie/search?', data)
    kk = json.loads(jsonqw)
    rating = kk["subjects"][0]["rating"]["average"]
    url = kk["subjects"][0]["alt"]
    jsonre = {'rating':rating, 'url':url}
   # respo = {'douban':jsonre}
    return json.dumps(jsonre, ensure_ascii=False, separators=(',', ':'))


#print(getRating("火星"))