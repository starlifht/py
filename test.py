#!/usr/bin/env python
# -*-coding:UTF-8-*-

""" a test module """

__author__ = 'STAR'

import urllib2
import re
from bs4 import BeautifulSoup
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')

domain = 'http://www.xixihd.com'


def getHtml(url):
    r = urllib2.Request(url)
    page = urllib2.urlopen(r, timeout=5)
    html = page.read()
    return html


hh = '<ul class="cont_l_d_ul"><li><span class="d_bt">' \
     '<a href="/?mod=content&id=31000">最好的敌人 Best.of.Enemies.2015.DOCU.720p.BluRay.x264-PSYCHD-xixiHD</a></span>' \
     '<span class="d_form">720P</span>' \
     '<span class="d_size">4.39GB</span>' \
     '<span class="d_size">abcnnt</span>' \
     '</li>' \
     '</ul>'
soup=BeautifulSoup(hh)
print(str(soup.select('.cont_l_d_ul')[0].a['href']))