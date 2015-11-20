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
    page = urllib2.urlopen(r, timeout=6)
    html = page.read()
    return html


try:
    conn = MySQLdb.connect(host='172.27.2.26', user='star', passwd='asd123', db='movie', port=3306, charset="utf8")
    cur = conn.cursor()
    mainHtml = getHtml(domain)
    an = re.findall(r'href="(/content-.*?html)"', mainHtml)
    s = set(an)
    for i in s:
        print(domain+i)
        html = getHtml(domain+i)
        soup = BeautifulSoup(html)
        newtitle = soup.select('.newtitle h1')[0].string
        imdbinfo = repr(soup.select('.imdbinfo')[0])
        soup.select('.cont_l_d_ul')[0].a['href'] = domain+str(soup.select('.cont_l_d_ul')[0].a['href'])
        download = soup.select('.cont_l_d_ul')[0]
        post_content = (newtitle, imdbinfo+repr(download), domain+i)
        cur.execute("replace into film(label,title,content,origin) VALUES('xixi',%s,%s,%s)", post_content)

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()
    conn.close()
