# !/usr/bin/env python
# encoding: utf-8


__author__ = 'STAR'

import xixi
import gaoqing
from multiprocessing import Pool

import sys


reload(sys)
sys.setdefaultencoding('utf-8')


p = Pool()

p.apply_async(xixi.getXiXi, args=('a',))
#p.apply_async(gaoqing.getGaoQing, args=('b',))
p.close()
p.join()
