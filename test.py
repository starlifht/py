#!/usr/bin/env python
# -*-coding:UTF-8-*-

""" a test module """

__author__ = 'STAR'

import hashlib
import time
ISOTIMEFORMAT = '%Y-%m-%d %X'
print(time.strftime(ISOTIMEFORMAT, time.localtime()))
m2 = hashlib.md5()
m2.update("tangfuqiangs")
print m2.hexdigest()