#!/usr/bin/env python
# -*-coding:UTF-8-*-


__author__ = 'STAR'

import urllib2
import re
from bs4 import BeautifulSoup
import MySQLdb
import sys
import time
import tools

reload(sys)
sys.setdefaultencoding('utf8')

domain = 'http://www.xixihd.com'

def getHtml(url):
    r = urllib2.Request(url)
    page = urllib2.urlopen(r, timeout=6)
    html = page.read()
    return html

def getXiXi(name):
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
            # print(title.split(' ')[1])
            # print(tools.getRating(str(title.split(' ')[1])))
            rating = tools.getRating(newtitle.split(' ')[0])

            soup.select('.cont_l_d_ul')[0].a['href'] = domain+str(soup.select('.cont_l_d_ul')[0].a['href'])
            soup.select('.infoimg')[0].img['src']=domain+str(soup.select('.infoimg')[0].img['src'])
            # print(soup.select('.infoimg')[0].img['src'])
            download = soup.select('.cont_l_d_ul')[0]
            imdbinfo = repr(soup.select('.imdbinfo')[0])
            post_content = (newtitle.replace('-xixiHD', ''), imdbinfo+repr(download), domain+i,rating)
            cur.execute("replace into film(label,title,content,origin,rating) VALUES('xixi',%s,%s,%s,%s)", post_content)
            time.sleep(5)

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    except urllib2.HTTPError, e:
        print "urllib Error %d: %s" % (e.args[0], e.args[1])
    except :
        print("error")
    finally:
        cur.close()
        conn.commit()
        conn.close()
