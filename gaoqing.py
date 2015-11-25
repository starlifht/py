#!/usr/bin/env python
# encoding: utf-8


__author__ = 'STAR'

import re
from bs4 import BeautifulSoup
import MySQLdb
import sys
import time
import tools
import urllib2


reload(sys)
sys.setdefaultencoding('utf8')


def getHtml(url):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    r = urllib2.Request(url)
    r.add_header('User-Agent', user_agent)
    page = urllib2.urlopen(r)
    htmltest = page.read()
    return htmltest


def getGaoQing(name):
    try:
        conn = MySQLdb.connect(host='172.27.2.26', user='star', passwd='asd123', db='movie', port=3306, charset="utf8")
        cur = conn.cursor()
        mainHtml = getHtml('http://gaoqing.la/')
        an = re.findall(r'href="(http://gaoqing\.la/.*?html)"', mainHtml)
        s = set(an)
        for i in s:
            print i
            html = getHtml(i)
            soup = BeautifulSoup(html)
            title = str(soup.title.string).replace('中国高清网', '')
            # print(title.split(' ')[1])
            # print(tools.getRating(str(title.split(' ')[1])))
            rating = tools.getRating(title.split(' ')[1])
            post_content = (title, repr(soup.find('div', id="post_content")), i, rating)
            cur.execute("replace into film(label,title,content,origin,rating) VALUES('gaoqing',%s,%s,%s,%s)", post_content)
            time.sleep(5)

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    finally:
        cur.close()
        conn.commit()
        conn.close()
        print('END')

