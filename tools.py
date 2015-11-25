# !/usr/bin/env python
# encoding: utf-8


__author__ = 'STAR'

import json
import urllib2
import urllib
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


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
    return json.dumps(kk["subjects"][0]["rating"]["average"], ensure_ascii=False, indent=4, separators=(',', ':'))
