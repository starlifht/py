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
    page = urllib2.urlopen(r, timeout=10)
    htmltest = page.read()
    return htmltest


def getGaoQing(name):
    try:
        conn = MySQLdb.connect(host='172.27.2.26', user='star', passwd='asd123', db='movie', port=3306, charset="utf8")
        cur = conn.cursor()
        mainHtml = getHtml('http://gaoqing.la/')
        mainsoup = BeautifulSoup(mainHtml)
        an = re.findall(r'href="(http://gaoqing\.la/.*?html)"', str(mainsoup.find('ul', id='post_container')))
        s = set(an)
        for i in s:
            print i
            html = getHtml(i)
            soup = BeautifulSoup(html)
            title = str(soup.title.string).replace('中国高清网', '')
            douban = tools.getRating(title.split(' ')[1])
            content = repr(soup.find('div', id="post_content"))
            post_content = (title, content, i, douban, content, tools.getTime())
            cur.execute("insert into film(label,title,content,origin,douban) VALUES('gaoqing',%s,%s,%s,%s) ON DUPLICATE KEY UPDATE content=%s, datetime=%s", post_content)
            time.sleep(5)

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    except :
        print("error")
    finally:
        cur.close()
        conn.commit()
        conn.close()

getGaoQing('sdf')