#!/usr/bin/env python
# -*-coding:UTF-8-*-


__author__ = 'STAR'

import urllib2
import re
from bs4 import BeautifulSoup
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getHtml(url):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    r = urllib2.Request(url)
    r.add_header('User-Agent', user_agent)
    page = urllib2.urlopen(r)
    htmltest = page.read()
    return htmltest


try:
    conn = MySQLdb.connect(host='172.27.2.26', user='star', passwd='asd123', db='movie', port=3306, charset="utf8")
    cur = conn.cursor()
    mainHtml = getHtml('http://gaoqing.la/')
    # print(mainHtml)

    an = re.findall(r'href="(http://gaoqing\.la/.*?html)"', mainHtml)
    s = set(an)
    for i in s:
        html = getHtml(i)

        soup = BeautifulSoup(html)

        post_content = (str(soup.title.string).replace('中国高清网', ''), repr(soup.find('div', id="post_content")), i)
        # post_content = (str('不是wre啊'),)
        # print(type(str(soup.find('div', id="post_content"))))
        # print(type(post_content))
        # post_content = (u'sdfsdfsdf',)
        # #test=(u'sdf6sd',u'hhhhh')
        cur.execute("replace into film(label,title,content,origin) VALUES('gaoqing',%s,%s,%s)", post_content)

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cur.close()
    conn.commit()
    conn.close()
